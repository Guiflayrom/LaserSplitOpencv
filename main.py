import cv2
import numpy as np
from colordict import ColorDict
import pandas as pd
#test forky
def showImage(img: np.ndarray,title: str, resize: int = 20):
    width = int(img.shape[1] * resize / 100)
    height = int(img.shape[0] * resize / 100)
    dim = (width, height)
    
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

    cv2.imshow(title,resized)
    cv2.waitKey(0)

getPercentage = lambda gramsGot,gramsSplit: int((gramsSplit * 100) / gramsGot) / 100

def getImageFilename(filename): return cv2.imread(filename)

def getContours(img: np.ndarray,threshValue: int):
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    img = cv2.erode(img, kernel, cv2.BORDER_REFLECT) 
    _, thresh = cv2.threshold(imgray, threshValue, 255, 0,cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_KCOS)
    return contours, thresh

def main(WEIGHT: int,GRAMSPLIT: int, FILENAME: str, show: bool = True, *args, **kwargs):
    # """
    # width x height

    # 0 = x=0 y=0
    # 1 = x=1 y=0
    # 2 = x=1 y=1
    # 3 = x=0 y=1
    # """
    
    img = getImageFilename(FILENAME)

    GENERAL_THICKNESS = kwargs['thick'] if kwargs['thick'] else 0
    THRESH_VALUE = kwargs['thresh'] if kwargs['thresh'] else 235

    contours, thresh = getContours(img,THRESH_VALUE)
    
    cnts = contours[1]
    data_cnts = [[cnt[0][0],cnt[0][1]] for cnt in cnts]
    df = pd.DataFrame(data_cnts,columns=['width','height'])

    min_x = df['width'].min()
    max_x = df['width'].max()
    min_y = df['height'].min()
    max_y = df['height'].max()


    ret_start_point = (min_x,min_y)
    ret_end_point = (max_x,max_y)

    width = max_x - min_x

    img = cv2.rectangle(img,ret_start_point,ret_end_point,ColorDict()['yellow'],2 + GENERAL_THICKNESS)
    img = cv2.drawContours(img, [cnts], 0, ColorDict()['chocolate'], 2 + GENERAL_THICKNESS)

    p = getPercentage(WEIGHT,GRAMSPLIT)
    splitedStep = width * p
    
    lines = []
    
    for index,i in enumerate(list(np.arange(0, width, splitedStep, dtype=int))):
        if index == 0: continue
        line_start = (i + ret_start_point[0], ret_start_point[1])
        line_end = (i + ret_start_point[0],ret_end_point[1])
        lines.append([line_start,line_end])

    for line in lines:
        cv2.line(img,line[0],line[1],ColorDict()['aqua'],1 + GENERAL_THICKNESS)

    if show: showImage(img,title=kwargs['title'] if kwargs['title'] else 'Scanner',resize=kwargs['resize'] if kwargs['resize'] else 100)

if __name__ == '__main__':
    FILE = 'mortadela.jpg'
    WINDOW_TITLE = 'Scanner - GDA'
    SHOW_WINDOW = True

    if FILE == 'mortadela.jpg':
        WEIGHT = 1000 #1000g
        SPLITED = 500 #500g
        RESIZE = 180
        THICK = 2
        THRESH = 235

    elif FILE == 'resource.jpg':
        WEIGHT = 10000 #10kg
        SPLITED = 2000 #2kg
        RESIZE = 20
        THICK = 20  
        THRESH = 235

    main(WEIGHT,SPLITED,FILE,resize=RESIZE,thick=THICK,title=WINDOW_TITLE,show=SHOW_WINDOW,thresh=THRESH)
