import cv2

class VideoCapture:
    def __init__(self,video_address:any=0) -> None:
        self.video_address = video_address
        self.cap = cv2.VideoCapture()
    
    def start(self):
        self.cap.open(self.video_address)
    
    def pause(self):
        self.cap.release()
    
    def get_frame(self):
        if not self.cap.isOpened():
            return
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            encoded, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 50])
            print(len(buffer.tobytes()))
            yield buffer.tobytes() 
    