# Morpher

Morpher is a simple microservice that converts XML strings to JSON.

Originally intended to be a reference project, additional methods have been added to handle BIS formatted documents, such as invoices.

## Build and Run

### Docker

Using the Flask (development) server:
```bash
docker build --target development -p 8888:8888 -t poetry
```

Using the Gunicorn (production) server:
```bash
docker run -p 8888:8888 -it poetry
```
