#!/usr/bin/env python3

import argparse
import pathlib
import cv2
import numpy as np
from matplotlib import pyplot as plt

def calculate_canny():
    img = cv2.imread('test_data/2019-02-20/154.jpg',0)
    img2 = cv2.imread('test_data/2019-02-20/156.jpg',0)
    img = img.astype(np.uint8)
    edges = cv2.Canny(np.array(img),1,255)
    plt.subplot(221),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(222),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    img2 = img2.astype(np.uint8)
    edges2 = cv2.Canny(np.array(img2),1,255)
    plt.subplot(223),plt.imshow(img2,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(224),plt.imshow(edges2,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()

def calculate_gradients(file_path):
    mag_arr = np.zeros((921600, 0))
    for current_file in sorted(pathlib.Path(file_path).iterdir()):
        img = cv2.imread(str(current_file), flags=cv2.IMREAD_GRAYSCALE)
        img = np.float32(img) / 255.0
        img = cv2.bilateralFilter(img,5,75,75)
        #img = cv2.GaussianBlur(img,(5,5),0)
        gx = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=1) #higher ksize --> larger norms
        gy = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=1)
        mag, angle = cv2.cartToPolar(gx,gy, angleInDegrees=True)
        mag_ravel = np.expand_dims(np.ravel(mag), axis=1)
        mag_arr = np.append(mag_arr, mag_ravel, axis=1)

    np.save('mag_arr', mag_arr)
    mag_diff = np.diff(mag_arr)
    mag_norms = np.linalg.norm(mag_diff, axis=0)


def graph_histograms(file_path):
    bins = 200
    hist_arr = np.zeros((bins,0))
    mag_arr = np.zeros((921600, 0))
    angle_arr = np.zeros((921600, 0))
    image_diff = np.zeros((bins,0))
    for current_file in sorted(pathlib.Path(file_path).iterdir()):
        #current_file = '/Volumes/Snorlax/photos/2019-02-20/00.jpg'
        #current_file = 'output.jpg'
        print(str(current_file))
        img = cv2.imread(str(current_file), flags=cv2.IMREAD_GRAYSCALE)
        img = np.float32(img) / 255.0
        gx = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=1) #higher ksize --> larger norms
        gy = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=1)
        mag, angle = cv2.cartToPolar(gx,gy, angleInDegrees=True)
        mag_ravel = np.expand_dims(np.ravel(mag), axis=1)
        angle_ravel = np.expand_dims(np.ravel(angle), axis=1)
        mag_arr = np.append(mag_arr, mag_ravel, axis=1)
        angle_arr = np.append(angle_arr, angle_ravel, axis=1)

        # plt.subplot(2,1,1), plt.imshow(img)
        # plt.subplot(2,1,2), plt.imshow(mag)
        # plt.show()

        # laplacian = cv2.Laplacian(img, cv2.CV_32F)
        # plt.subplot(2,1,1), plt.imshow(img)
        # plt.subplot(2,1,2), plt.imshow(laplacian)
        # plt.show()

        # hist = cv2.calcHist([img], [0], None, [bins], [0,bins])
        # hist_arr = np.append(hist_arr, hist, axis=1)

        #brief = cv2.ORB.getFirstLevel(cv2.ORB(img))

        #plt.subplot(121), plt.imshow(img,'gray')
        #plt.subplot(122), plt.plot(arr[:,0]), plt.xlim([0,256]), plt.title("img")
        #plt.show()

    mag_diff = np.diff(mag_arr)
    mag_norms = np.linalg.norm(mag_diff, axis=0)
    angle_diff = np.diff(angle_arr)
    angle_norms = np.linalg.norm(angle_diff, axis=0)

    np.save('mag_arr', mag_arr)
    np.save('mag_norms', mag_norms)
    np.save('angle_arr', angle_arr)
    np.save('angle_diff', angle_diff)
    np.save('angle_norms', angle_norms)

    print(np.shape(mag_norms))
    print(mag_norms)

    mag_ord = np.argsort(-mag_norms)
    results = 20
    for i in range(results):
        offset = 0
        img1_str="{:03d}".format(mag_ord[offset+i])
        img2_str="{:03d}".format(mag_ord[offset+i]+1)
        print("{}/{}.jpg - {}".format(str(pathlib.Path(file_path)),img1_str, mag_norms[mag_ord[offset+i]]))
        img1 = cv2.imread("{}/{}.jpg".format(str(pathlib.Path(file_path)),img1_str))
        img2 = cv2.imread("{}/{}.jpg".format(str(pathlib.Path(file_path)),img2_str))
        plt.subplot(2, results, i+1), plt.imshow(img1)
        plt.xticks([]), plt.yticks([])
        plt.subplot(2, results, results+i+1), plt.imshow(img2)
        plt.xticks([]), plt.yticks([])
    plt.show()

    # hist_diff = np.diff(hist_arr)
    # hist_norms = np.linalg.norm(hist_diff, axis=0)
    # hist_selected = np.where((hist_norms>4000) & (hist_norms<12000), hist_norms, 0)
    # hist_ord = np.argsort(-hist_selected)

    #print(np.shape(hist_diff))
    # print(hist_norms[218])
    # print(hist_selected)
    # print(hist_ord)

    # plt.subplot(121), plt.plot(hist_arr), plt.xlim([0,bins])
    # plt.subplot(122), plt.plot(hist_diff), plt.xlim([0,bins])
    # plt.show()

def compare_cannys():
    img = cv2.imread('test_data/2019-02-20/154.jpg',0)
    img2 = cv2.imread('test_data/2019-02-20/155.jpg',0)
    img = img.astype(np.uint8)
    edges = cv2.Canny(np.array(img),1,255)
    plt.subplot(221),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(222),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    img2 = img2.astype(np.uint8)
    edges2 = cv2.Canny(np.array(img2),1,255)
    plt.subplot(223),plt.imshow(img2,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(224),plt.imshow(edges2,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path")
    args = parser.parse_args()
    print(args.file_path)
    graph_histograms(args.file_path)
