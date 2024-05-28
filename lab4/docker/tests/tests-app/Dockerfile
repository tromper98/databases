FROM python:3.9

WORKDIR /app

COPY ./requirements.txt /app
RUN apt install wget ca-certificates; \
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -; \
    sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ bookworm-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'; \
    apt update;
RUN apt install unixodbc odbc-postgresql -y
RUN pip3 install --upgrade pip -r requirements.txt
EXPOSE 5000
