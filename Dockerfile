FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 10000


CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port 10000 & streamlit run main.py --server.port 10000 --server.address 0.0.0.0"]