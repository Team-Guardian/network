FROM python:3.5
MAINTAINER guardian-vision-team

EXPOSE 80

ADD server.py /opt/airserver/
ADD settings.py /opt/airserver/

CMD ["python", "/opt/airserver/server.py"]