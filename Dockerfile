FROM python:3.9.7
COPY requirement.txt ./
WORKDIR ./
RUN pip freeze > requirement.txt
#RUN pip install -r requirement.txt
#RUN  install -m --upgrade pip
RUN pip3 install --upgrade pip==20.0.1
COPY . /
CMD ["python" "./main.py"]
