import os
import pymupdf4llm
import pathlib

# faire la detection des nouveau pdf pour evite de tout refaire a cahque fois ?
def get_pdf_names(folder_path="data/pdf"):
    pdf_names = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_names.append(filename)
    return pdf_names

def get_pdf_paths(folder_path="data/pdf"):
    pdf_paths = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_paths.append(os.path.join(folder_path, filename))
    return pdf_paths
#print(get_pdf_paths())


# on cree les markdown qui ne sont pas deja cree et onr etourne tout les markdown qui n'on plus de source pdf pour les retirer des chunk
def extract_missing_markdown(pdf_folder="data/pdf", md_folder="data/markdown"):
    os.makedirs(md_folder, exist_ok=True)

    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]
    md_basenames = {os.path.splitext(f)[0] for f in os.listdir(md_folder) if f.endswith(".md")}

    for pdf_file in pdf_files:
        base_name = os.path.splitext(pdf_file)[0]

        if base_name not in md_basenames:
            pdf_path = os.path.join(pdf_folder, pdf_file)
            #md_text = pymupdf4llm.to_markdown(pdf_path)
            md_text = to_clean_markdown(pdf_path)

            md_path = os.path.join(md_folder, base_name + ".md")
            pathlib.Path(md_path).write_bytes(md_text.encode("utf-8"))
            print(f"Markdown créé : {md_path}")
        else:
            print(f"Markdown deja crée : {pdf_file}")
        md_basenames.discard(base_name)

    orphans = [os.path.join(md_folder, name + ".md") for name in md_basenames]
    return orphans


def to_clean_markdown(pdf_path):# pas ouf
    md_text = pymupdf4llm.to_markdown(pdf_path)

    cleaned_lines = []
    for line in md_text.splitlines():
        line = line.strip()
        if line.startswith("![") or line.startswith("|") or line.endswith("|"):
            continue
        cleaned_lines.append(line)

    return "\n".join(cleaned_lines)


def to_markdown(pdf_paths, output_folder="data/markdown"):
    os.makedirs(output_folder, exist_ok=True)

    for pdf_path in pdf_paths:
        filename = os.path.basename(pdf_path)
        base_name = os.path.splitext(filename)[0]
        md_text = pymupdf4llm.to_markdown(pdf_path)

        output_path = os.path.join(output_folder, f"{base_name}.md")

        pathlib.Path(output_path).write_bytes(md_text.encode("utf-8"))
        print(f" Markdown sauvegardé : {output_path}")


#to_markdown(get_pdf_paths())



PDF_DIR = "./data/pdf"
INDEX_FILE = "./data/indexe_pdf.txt"

def lister_pdfs_recurse(path=PDF_DIR):
    pdfs = []
    for root, _, files in os.walk(path):
        for file in files:
            if file.lower().endswith(".pdf"):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, PDF_DIR)
                pdfs.append(rel_path)
    return sorted(pdfs)

def charger_index(index_path=INDEX_FILE):
    if not os.path.exists(index_path):
        return []
    with open(index_path, "r", encoding="utf-8") as f:
        return sorted([line.strip() for line in f.readlines()])

def sauvegarder_index(pdf_list, index_path=INDEX_FILE):
    with open(index_path, "w", encoding="utf-8") as f:
        for path in sorted(pdf_list):
            f.write(path + "\n")

def detecter_changements():
    pdf_actuels = lister_pdfs_recurse()
    pdf_indexes = charger_index()

    nouveaux = sorted(set(pdf_actuels) - set(pdf_indexes))
    supprimes = sorted(set(pdf_indexes) - set(pdf_actuels))

    return nouveaux, supprimes



# on crée les nouveau markdown si on detecte de nouveau pdf, on retourne la liste a supprimer (car on veux aussi supp chunk ensuite)
def mise_a_jour():
    nouveaux, supprimes = detecter_changements()
    if nouveaux:
        print("Nouveaux PDF à traiter :")
        for pdf in nouveaux:
            to_markdown(pdf, output_folder="data/markdown")
            print(" +", pdf)

    if supprimes:
        return supprimes

    if not nouveaux and not supprimes:
        print("Aucun changement détecté.")
