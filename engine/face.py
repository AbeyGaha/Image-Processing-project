import cv2

class FaceEngine:

    def __init__(self, model_path):
        self.face_cascade = cv2.CascadeClassifier(model_path)

    def detect_faces(self, gray_img):
        faces = self.face_cascade.detectMultiScale(gray_img, 1.3, 5)
        return faces
