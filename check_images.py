import os
import cv2
import sys


def find_slide(img):
    height, width, _ = img.shape
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    pixels = cv2.countNonZero(thresh)
    result = True if pixels >= (height * width * 0.5) else False
    return result


if __name__ == "__main__":
    dir_name = sys.argv[1]

    if os.path.exists(dir_name):
        for file in os.listdir(dir_name):
            if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
                img_path = os.path.join(dir_name, file)
                img = cv2.imread(img_path)
                result = find_slide(img)
                print(
                    "Image {} is slide".format(file)
                    if result is True
                    else "Image {} isn't slide".format(file)
                )
