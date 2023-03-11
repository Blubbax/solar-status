FROM 3.9-slim
WORKDIR /app
COPY . /app
RUN pip --no-cache-dir install -r requirements.txt

CMD ["flask", "--app", "api", "run"]