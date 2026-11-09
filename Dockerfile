FROM python:3.11.10-slim

WORKDIR /app

COPY . .

CMD ["python", "books.py", "--help"]