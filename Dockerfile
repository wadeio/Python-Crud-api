FROM python:3
# env
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

WORKDIR /app

COPY requirements.txt ./
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# app
COPY . .

CMD [ "python3", "./app.py" ]