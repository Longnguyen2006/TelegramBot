FROM python:3.9.7
COPY requirement.txt ./
WORKDIR /app
RUN pip install -r requirement.txt
COPY . /app
CMD ["python" "./app/main.py"]
