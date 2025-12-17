FROM python:3.10-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY ml/requirements-ml.txt .
RUN pip install --no-cache-dir -r requirements-ml.txt

RUN python - <<EOF
import nltk
nltk.download('punkt')
nltk.download('stopwords')
EOF

COPY ml/batch/ ./notebooks

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
