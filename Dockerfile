FROM python:3.11-slim

WORKDIR /src

COPY requirements.txt .

COPY cli ./cli

RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src

ENV PORT=8080
EXPOSE 8080

CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8080"]