FROM python:3
ENV USERNAME bismillahtraders
RUN mkdir -p /home/ca
WORKDIR /home/ca
COPY . /home/ca
EXPOSE 5000

RUN pip install -r requirements.txt
RUN pip install flask
CMD ["python","hello.py"]