FROM python:3.9

WORKDIR /app

COPY src/requirements.txt ./
RUN pip3 install -r requirements.txt

COPY src .

EXPOSE 8080

ENV FLASK_APP=main
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8080"]
