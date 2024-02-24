FROM python:3.13.0a4-bookworm
WORKDIR /app
COPY ./src ./
CMD ["python", "./__main__.py"]