FROM rasa/rasa
USER root 
ENV BOT_ENV=production
WORKDIR /app
COPY . /app
COPY ./data /app/data
RUN pip install --upgrade pip
RUN pip install rasa
RUN rasa train

ENTRYPOINT ["rasa", "run", "-m", "/app/models", "--enable-api", "--cors", "*","-p", "8080", "--debug"]
