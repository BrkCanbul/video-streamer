import cv2
import time
class VideoCapture:
    def __init__(self,video_address:any=0,fps:int=55) -> None:
        self.video_address = video_address
        self.cap = cv2.VideoCapture()
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        self.fps = fps
        
    
    def start(self):
        self.cap.open(self.video_address)
    
    def pause(self):
        self.cap.release()
    
    def get_frame(self):
        if not self.cap.isOpened():
            return
        while True:
            time.sleep(1/self.fps) 
            ret, frame = self.cap.read()
            if not ret:
                break
            encoded, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 35])
            print(len(buffer.tobytes()))
            yield buffer.tobytes() 
    