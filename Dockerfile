FROM ubuntu:18.04

RUN apt-get update && apt-get install -y python3-pip && apt-get clean

WORKDIR /djangoproject
ADD . /djangoproject
RUN pip3 install -r requirements.txt

# 파이썬 표준출력 과정에서 버퍼링을 지정하지않고 그때그때 출력하게됨
ENV PYTHONUNBUFFERED=1

EXPOSE 80
CMD ["python3", "manage.py", "runserver", "0.0.0.1:8000"]
#CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:80"]