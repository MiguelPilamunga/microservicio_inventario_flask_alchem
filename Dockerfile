FROM python:3.12.4-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5008

ENV DB_HOST={{DB_HOST}}
ENV DB_USER={{DB_USER}}
ENV DB_PASSWORD={{DB_PASSWORD}}
ENV DB_NAME={{DB_NAME}}

CMD ["python", "app.py"]