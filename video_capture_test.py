from unittest import TestCase,loader
from video_capture import VideoCapture
class TestVideoCapture(TestCase):
    
    def test_frame_capture(self):
        vc=VideoCapture()
        vc.start()
        frame =  vc.get_frame()
        self.assertIsNotNone(frame)
    
    def test_open_camera_success(self):
        vc = VideoCapture()
        vc.start()
        self.assertTrue(vc.cap.isOpened())
    
    def test_open_camera_failure(self):
        vc = VideoCapture(video_address=1)
        vc.start()
        self.assertFalse(vc.cap.isOpened())
    
    def test_pause_camera(self):
        vc = VideoCapture()
        vc.start()
        vc.pause()
        self.assertFalse(vc.cap.isOpened())
        
    def test_frame_size(self):
        vc = VideoCapture()
        vc.start()
        for index,frame in enumerate(vc.get_frame()):
            if index == 10:
                break;
            self.assertGreater(len(frame),0)
    
    def test_fps(self):
        vc = VideoCapture(fps=60)
        vc.start()
        frame =  vc.get_frame()
        self.assertEqual(vc.fps,60)
    