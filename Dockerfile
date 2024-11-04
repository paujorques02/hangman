FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN if [ -f "requirements.txt" ]; then pip install --no-cache-dir -r requirements.txt; fi

COPY . .

EXPOSE 8000

CMD ["python", "hangman.py"]
