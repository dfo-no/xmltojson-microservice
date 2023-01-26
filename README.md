# Morpher

Morpher is a simple microservice that converts XML strings to JSON.

Originally intended to be a reference project, additional methods have been added to handle BIS formatted documents, such as invoices.

## Build and Run

### Docker

Using the Flask (development) server:
```bash
docker build --target development -t morpher . && docker run -p 8888:8888 morpher 
```

Using the Gunicorn (production) server:
```bash
docker build -t morpher . && docker run -p 8888:8888 morpher 
```
