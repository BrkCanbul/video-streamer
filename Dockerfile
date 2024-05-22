FROM python:3.9-slim

WORKDIR /app

COPY ./ requirements.txt ./

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0
RUN pip install -r requirements.txt
COPY . .


EXPOSE 5000/udp

CMD ["python","main.py","--port","5000","--video","/app/input.mp4"]


