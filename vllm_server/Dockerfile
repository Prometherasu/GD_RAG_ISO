FROM nvidia/cuda:12.1.1-runtime-ubuntu22.04

# Installer Python et pip
RUN apt-get update && apt-get install -y python3 python3-pip git

# Installer vLLM et huggingface_hub (version avec CLI)
RUN pip3 install --upgrade pip
RUN pip3 install vllm huggingface_hub[cli]

WORKDIR /app

# Copier ton script d'entrée (si besoin)
COPY app.py .

# Exposer port 8000
EXPOSE 8000

CMD ["python3", "-m", "vllm.entrypoints.openai.api_server", "--model", "/models/falcon", "--host", "0.0.0.0", "--port", "8000"]

