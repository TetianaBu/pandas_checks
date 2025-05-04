FROM python:3.10-slim

RUN pip install --no-cache-dir pandas pyarrow jupyter notebook

WORKDIR /app

COPY . /app

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]