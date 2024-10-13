FROM python

WORKDIR /home/app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python3","manage.py", "runserver", "0.0.0.0:5000"]