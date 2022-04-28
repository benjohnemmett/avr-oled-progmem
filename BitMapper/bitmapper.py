
import numpy as np 
import cv2 
import os

OUTPUT_SIZE_ROWS = 32
OUTPUT_SIZE_COLS = 32
BLUR_SIZE = 3
CANNY_THRESH1 = 100
CANNY_THRESH2 = 200

show_images = True

file_name = "smile.jpg"

def read_image_as_grayscale():
    file = os.path.join(".", file_name)

    img = cv2.imread(file)
    print("img shape {}".format(img.shape))

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    return img_gray

def get_edge_image(img_gray):
    img_blur = cv2.GaussianBlur(img_gray, (BLUR_SIZE, BLUR_SIZE), 0)
    edges = cv2.Canny(image=img_blur, threshold1=CANNY_THRESH1, threshold2=CANNY_THRESH2)

    return edges


def get_binary_image(edges):
    edge_fat = cv2.dilate(edges, np.ones((21,21)), iterations=1)

    small = cv2.resize(edge_fat, (OUTPUT_SIZE_COLS, OUTPUT_SIZE_ROWS))
    binary = np.where(small > 0, 1, 0).astype(np.uint8)

    return binary
    

def get_binary_image_code(binary):

    codeString = "uint8_t smile[{}][{}] = {{".format(OUTPUT_SIZE_ROWS, OUTPUT_SIZE_COLS)
    for r in range(binary.shape[0]):
        codeString += "\n{"
        for c in range(binary.shape[1]):
            codeString += "{}, ".format(binary[r,c])
        codeString += "},"
    codeString += "\n};"

    return codeString


def main():

    img_gray = read_image_as_grayscale()

    if show_images:
        cv2.imshow("img_gray", img_gray)
        cv2.waitKey(0)

    edges = get_edge_image(img_gray)

    if show_images:
        print("edges {}".format(edges))
        print("max edge {}".format(np.max(edges)))
        cv2.imshow("edges", edges)
        cv2.waitKey(0)

    binary = get_binary_image(edges)

    if show_images:
        cv2.imshow("binary", binary*255)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    code_string = get_binary_image_code(binary)

    print(code_string)

if __name__ == "__main__":
    main()
