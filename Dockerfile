FROM python:3.9.7
COPY requirement.txt ./
WORKDIR ./
RUN pip freeze > requirement.txt
#RUN pip install -r requirement.txt
RUN pip install -m --upgrade pip
COPY . /
CMD ["python" "./main.py"]
