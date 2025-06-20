from elasticsearch import Elasticsearch
import os

#es = Elasticsearch("http://localhost:9200")
RAG_INDEX_NAME = "ragisochunks"

es = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", "XI4CLgWOT=JONdALQtsf"),
    verify_certs=False
)

def create_index(index_name=RAG_INDEX_NAME):
    if not es.indices.exists(index=index_name):
        print(f"L'index {index_name} n'existe pas, création en cours...")
        es.indices.create(
            index=index_name,
            body={
                "mappings": {
                    "properties": {
                        "content": {"type": "text"},
                        "embedding": {
                            "type": "dense_vector",
                            "dims": 384,
                            "index": True,
                            "similarity": "cosine"
                        },
                        "metadata": {
                            "properties": {
                                "source": {"type": "keyword"},
                                "page": {"type": "integer"}
                            }
                        }
                    }
                }
            }
        )

        print(f"Index '{index_name}' créé")
    else:
        print(f"Index '{index_name}' déjà existant")


def create_indexSave(index_name):
    if not es.indices.exists(index=index_name):
        es.indices.create(index=index_name)
        print(f" Index '{index_name}' créé")
    else:
        print(f" Index '{index_name}' déjà existant")

def index_chunks(index_name, chunks):
    for chunk in chunks:
        es.index(index=index_name, document=chunk)


def cleanup_orphan_documents(orphans, json_folder="data/chunks_json", index_name="rag_iso_chunks"):
    for md_path in orphans:
        base_name = os.path.splitext(os.path.basename(md_path))[0]
        print(f"Nettoyage : {base_name}")

        es.delete_by_query(index=index_name, query={
            "match": {
                "metadata.source": f"{base_name}.md"
            }
        })
        print(f"Index Elasticsearch supprimer : {base_name}")

        json_path = os.path.join(json_folder, base_name + ".json")
        if os.path.exists(json_path):
            os.remove(json_path)

        if os.path.exists(md_path):
            os.remove(md_path)


def delete_index(index_name=RAG_INDEX_NAME):
    if es.indices.exists(index=index_name):
        es.indices.delete(index=index_name)
        print(f"Index '{index_name}' supprimé.")
    else:
        print(f"L'index '{index_name}' n'existe pas.")