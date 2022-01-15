from pidng.core import RPICAM2DNG
import os
import cv2


def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            if ".jpg" in file:
                yield os.path.join(path, file)


def channelSplit(data, file):
    file_name = os.path.splitext(file)[0]
    cv2.imwrite(file_name+"_blue.png", data[0::2, 0::2] << 4)
    cv2.imwrite(file_name+"_green1.png", data[1::2, 0::2] << 4)
    cv2.imwrite(file_name+"_green2.png", data[0::2, 1::2] << 4)
    cv2.imwrite(file_name+"_red.png", data[1::2, 1::2] << 4)
    return data


for file in files("C:/Users/matt/Documents/Astro_hobby/Python"):
    RPICAM2DNG().convert(file, process=channelSplit)