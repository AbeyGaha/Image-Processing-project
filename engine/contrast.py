import cv2

class ContrastEngine:

    @staticmethod
    def to_rgb(img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    @staticmethod
    def to_gray(img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    @staticmethod
    def to_bw(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, bw = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        return bw

    @staticmethod
    def edges(img):
        blurred = cv2.GaussianBlur(img, (15, 15), 0)
        return cv2.Canny(blurred, 100, 200)
