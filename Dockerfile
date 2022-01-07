FROM python:3.9.7
COPY requirement.txt ./
WORKDIR ./
RUN pip install -r requirement.txt
RUN pip install -m --upgrade pip
COPY . /
CMD ["python" "./app/main.py"]
