# RAG

ES (ElasticSearch)
C'est un projet test le but etant de decouvrir avantage inconvenient des possibiliter actuelle 

les donnée seront quelques (environ 4-5) pdf dans un premier temps 
ils seront traiter puis indexe pour la recherche avec elasticsearch

On recupere la query du client qui est passea ES.search pour la recherche ce qui nous retourne les chunk pour cree le prompt 
on envoie le prompt dans un LLM et recupere la reponse

optionnel:
    faire une interface Streamlit ou FastAPI pour le RAG 


pour l'extraction des informatiion du pdf on a choisi [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/rag.html) (PyMuPDF4llm) qu'on format en markcown avec la methode `pymupdf4llm.to_markdown(pdf_path)` on va traiter ces markdown pour enlever tout ce qui ne se prete pas a une recherche textuel (ref image, tableau, ...) (a ameliorer)

Lancer ES:
```
docker run -d -p 9200:9200 -e "discovery.type=single-node" -e "xpack.security.enabled=false" docker.elastic.co/elasticsearch/elasticsearch:8.12.2
```

Elasticsearch tokenise (découpe) les mots et utilise un score de similarité (BM25) pour classer les documents.
a verifier ce que c'est et comment ca fonctionne

les question doivent etre poser dans la langue dont les document sont stocker dans elastic puisque c'est de la recherche mots a mots 
alors soit traduire les question (pas implementer pour le moments) soit pose les question en anglais

l'installation des model va dans:
~\.cache\huggingface\hub\models--tiiuae--falcon-7b-instruct


l'architecture du projet  
- data contient les pdf
- docs contient les chunk index
- embeddings vecteur faiss ou autre 


[ES-RAG](https://www.elastic.co/guide/en/elasticsearch/reference/current/_retrieval_augmented_generation.html)

[ES-semantic-search](https://www.elastic.co/guide/en/elasticsearch/reference/current/semantic-search.html)

Donc on a utilise elasticsearch avec notre propre NLP (Natural Language Processing) c'est a dire qu'on a utilise un model "all-MiniLM-L6-v2" pour cree un vecteur dense qui sera utilise dans une recherche hybride 
la recherche hybride commence par faire une recherche classique par mots clef puis une recherche  semantique sur les vecteur grace aux embeddings
les chunk retourner sont ajouter au prompt puis le prompt est envoyer un model de generation de text qui va y repondre

Dans l'etat fonctionnel mais on pourrais tester les different apramettre (taille des chunk, overlap, le nombre optimale de chunk a retourner, les model possible, ...) et si il est possible d'ameliorer les markdown les rendre plus "lisible" pour le model de generation


# GD_RAG_ISO
# GD_RAG_ISO
docker run --gpus all --shm-size 1g -p 8080:80 \
  -v ~/.cache/huggingface:/data \
  ghcr.io/huggingface/text-generation-inference:1.3 \
  --model-id tiiuae/falcon-7b-instruct \
  --quantize bitsandbytes

## cmd 

instller avec pip

cd /home/stage/Documents/Stage/projets/RAG/GD_RAG_ISO
python3 -m venv venv
source venv/bin/activate
pip install openai


docker build -t vllm-falcon .



docker run -d --name elasticsearch-dev -p 9200:9200 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.12.2


XI4CLgWOT=JONdALQtsf
