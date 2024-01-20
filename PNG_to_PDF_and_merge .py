# coding: utf-8
import cv2 as cv
import os
from PIL import Image
from PyPDF2 import PdfMerger

def Image_Cut(path, index):
    img_left = cv.imread(path)
    img_right = cv.imread(path)

    h, w = int(img_left.shape[0]), int(img_left.shape[1]/2)
    x, y = 0, 0
    
    for i in range(3):
        img_left[(h-66):h, 0:w*2, i] = 255
        img_right[(h-66):h, 0:w*2, i] = 255
    # HERE!!!
    crop_img_left = img_left[y+32:h, x:w]
    crop_img_right = img_right[y+32:h, w:w*2]

    filename1 = str(index)
    filename2 = str(index + 1)
    
    filepath1 = "C:\\Users\\user\\Desktop\\DONE\\" + filename1 + ".png"
    filepath2 = "C:\\Users\\user\\Desktop\\DONE\\" + filename2 + ".png"

    cv.imwrite(filepath1, crop_img_left, [int(cv.IMWRITE_PNG_COMPRESSION), 0])
    cv.imwrite(filepath2, crop_img_right, [int(cv.IMWRITE_PNG_COMPRESSION), 0])
    
    PngToPdf1 = Image.open(filepath1)
    PngToPdf2 = Image.open(filepath2)
    PngToPdf1.convert("RGB")
    PngToPdf2.convert("RGB")
    PngToPdf1.save("C:\\Users\\user\\Desktop\\DONE\\" + filename1 + ".pdf")
    PngToPdf2.save("C:\\Users\\user\\Desktop\\DONE\\" + filename2 + ".pdf")
    
fileList = os.listdir("C:\\Users\\user\\Desktop\\RAW")

i = 1000000
"""
避免1~9會與後續二位數以上之數字
在PdfMerger()中會發生排序問題
預期：1, 2, 3, 4, 5, 6, ,7 ,8, 9, 10, 11, ...
實際：1, 10, 11, ..., 19, 2, 20, 21, ...
"""
for filename in fileList:
    path = "C:\\Users\\user\\Desktop\\RAW\\" + filename
    Image_Cut(path, i)
    os.remove(path)
    i +=2

print("完成裁切" + str(int((i + 1) / 2)) + "張圖片")

print("已將裁切完之圖片轉為PDF")
print("開始合併PDF")

mergeName = input("請輸入檔案名稱：")

path = "C:\\Users\\user\\Desktop\\DONE\\"
pdfList = os.listdir(path)
pdf_merge = PdfMerger()
for filename in pdfList:
    if filename.lower().endswith("pdf"):
        pdf_merge.append(path + filename)
pdf_merge.write("C:\\Users\\user\\Desktop\\" + mergeName + ".pdf")
pdf_merge.close()
print("PDF合併完成")

print("刪除原始檔")
pdfList = os.listdir(path)
for filename in pdfList:
    if filename != (mergeName + ".pdf"):
        os.remove(path + filename)
print("刪除完成")