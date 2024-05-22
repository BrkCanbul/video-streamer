import socket
import time
import threading
import argparse 
import sys
from video_capture import VideoCapture

def clear():
    print("\033[H\033[J")

def main(args):
    video_address = args.video
    port = args.port
    
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    host_ip = args.host
    server_address = (host_ip,port)


    try:
        pass
        #server.bind(server_address)
    except socket.error as e:
        print(f"error occured: {e}")
        return
    print(type(video_address))
    
    video_capture = VideoCapture(video_address)
    video_capture.start()
    print(server.getsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST))
    while True:
        #time.sleep(1)
        
        for frame in video_capture.get_frame():
            
            server.sendto(frame, server_address)
            
            
        video_capture.pause()


if __name__ =="__main__":
    parser = argparse.ArgumentParser(description="this is a streaming application for streaming videos or camera feed")
    parser.add_argument("--port", type=int, default=8000, help="port number")
    parser.add_argument("--video", type=int, default=0, help="video address")
    
    parser.add_argument("--host", type=str, default="localhost", help="host ip address")
    
    args = parser.parse_args()
    
    main(args)