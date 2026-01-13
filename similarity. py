import face_recognition
import numpy as np

class SimilarityEngine:

    @staticmethod
    def face_similarity(img1_path, img2_path):
        img1 = face_recognition.load_image_file(img1_path)
        img2 = face_recognition.load_image_file(img2_path)

        enc1 = face_recognition.face_encodings(img1)[0]
        enc2 = face_recognition.face_encodings(img2)[0]

        distance = np.linalg.norm(enc1 - enc2)
        similarity = max(0, (1 - distance)) * 100

        return round(similarity, 2)
