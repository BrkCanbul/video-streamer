import socket
import time
import threading
import argparse 
import sys
from video_capture import VideoCapture

def main(args,is_cam:bool):
    
    video_address = 0 if is_cam else args.video
    port = args.port
    if not is_cam and video_address == "":
        print("please provide a video address")
        return
    
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    host_ip = args.host
    server_address = (host_ip,port)


    try:
        pass
        #server.bind(server_address)
    except socket.error as e:
        print(f"error occured: {e}")
        return
    
    video_capture = VideoCapture(video_address)
    video_capture.start()
    print(server.getsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST))

    
    while True:        
        for frame in video_capture.get_frame():
            
            server.sendto(frame, server_address)
            
            
        video_capture.pause()


if __name__ =="__main__":
    parser = argparse.ArgumentParser(description="this is a streaming application for streaming videos or camera feed")
    parser.add_argument("--port", type=int, default=8000, help="port number")
    parser.add_argument("--video", type=str, default="", help="video address")
    parser.add_argument("--cam",action="store_true", help="use camera feed")
    parser.add_argument("--host", type=str, default="localhost", help="host ip address")
    
    args = parser.parse_args()

    main(args,args.cam)
