FROM python:3.10-slim-buster
WORKDIR /chess-app
COPY . .
RUN pip install -r requirements.txt
CMD [ "python3", "-m" , "flask", "--app", "app.py", "run", "--host=0.0.0.0"]
