import os
import cv2
import sys


def check_if_slide(img):
    height, width, _ = img.shape
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # count non-zero (white) array elements
    # and having pixels_thershold set arbitrarily to 50%
    pixels_thershold = 0.5
    pixels = cv2.countNonZero(thresh)
    result = True if pixels >= (height * width * pixels_thershold) else False
    return result


if __name__ == "__main__":
    dir_name = sys.argv[1]
    if_delete = False
    if len(sys.argv) == 3:
        if sys.argv[2] == "delete":
            if_delete = True

    if os.path.exists(dir_name):
        for file in os.listdir(dir_name):
            if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
                img_path = os.path.join(dir_name, file)
                img = cv2.imread(img_path)
                result = check_if_slide(img)
                print(
                    "Image {} is slide".format(img_path)
                    if result is True
                    else "Image {} isn't slide".format(img_path)
                )
                if if_delete and not result:
                    os.remove(img_path)
