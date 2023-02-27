FROM python:3.11.1
LABEL maintainer="Katie Gamanji"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

# Command to run on contaimer start
CMD [ "python", "app.py"]

