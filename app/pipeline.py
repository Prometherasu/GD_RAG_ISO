from .extract_pdf import extract_missing_markdown, mise_a_jour
from .chunking import  process_all_markdown
from .index_elastic import cleanup_orphan_documents, create_index, index_chunks
from .search import search_chunks
from .generate import generate_answer

import os
import json
RAG_INDEX_NAME = "ragisochunks"

def init(model=None, index_name=RAG_INDEX_NAME):
    print(model)
    print("Etape 1 — Extraction des nouveaux Markdown")
    #orphans = extract_missing_markdown()
    supprimes = mise_a_jour()

    if supprimes:
        print("Etape 2 — Nettoyage des documents orphelins")
        #cleanup_orphan_documents(orphans)
        cleanup_orphan_documents(supprimes)

    print("Etape 3 — Chunking des Markdown en JSON")
    #process_all_markdown(model)# modifier la logique pour faire seulement les nouveau doc



    print("Etape 4 — Indexation dans Elasticsearch")# a gere car on index a chaque fois il faut tenir la list a jours et faire passé l'etat (modifié)
    create_index(index_name)

    json_folder = "data/chunks_json"
    for json_file in os.listdir(json_folder):
        if json_file.endswith(".json"):
            with open(os.path.join(json_folder, json_file), encoding="utf-8") as f:
                chunks = json.load(f)
                index_chunks(index_name, chunks)

def pipeline(query, model=None, index_name=RAG_INDEX_NAME):
    print("Etape 5 — Recherche")
    retrieved_chunks = search_chunks(query, model, index_name=index_name)


    print("Etape 6 — Génération de réponse")
    answer = generate_answer(query, retrieved_chunks)

    print("\nRéponse :\n", answer)
