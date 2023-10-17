FROM python:3.8
RUN apt-get update -y
RUN apt-get install -y python3-pip
RUN mkdir /app/

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . /app/
WORKDIR /app/

ENV PRJPATH /app/
CMD ["python", "-um", "source.run"]