FROM python:3.11

WORKDIR /

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY startup.sh /
RUN chmod +x /startup.sh

WORKDIR /usr/src

EXPOSE 80

CMD ["/startup.sh"]