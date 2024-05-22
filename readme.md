# Quickstart

1. clone the repo 
```shell
git clone https://github.com/brkCanbul/video-streamer
```
2. initialize virtual environmnet
* for ubuntu 
```shell
python3 -m venv venv
soruce venv/bin/activate
```
* for windows
```shell
python -m venv venv
./venv/Scripts/Activate
```
3. install the requirements
```shell
pip install -r requirements.txt
```
4. start application
```shell
python3 ./main --host <Host_ip=localhost> --video <video_url=0> --port <port>
```
