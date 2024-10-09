FROM python
WORKDIR /app
ADD . /app
RUN apt update && apt install  -y \
 build-essential \
 curl \
 python3 \
 python3-pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE  8000
CMD python3 manage.py runserver 0.0.0.0:8000