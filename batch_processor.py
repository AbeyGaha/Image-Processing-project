import os
import cv2
from engine.contrast import ContrastEngine

class CollectionProcessor:

    def process_folder(self, folder_path, output_path):
        os.makedirs(output_path, exist_ok=True)

        for file in os.listdir(folder_path):
            img = cv2.imread(os.path.join(folder_path, file))
            edges = ContrastEngine.edges(img)
            cv2.imwrite(f"{output_path}/edges_{file}", edges)
