from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol
import cv2
import numpy as np
import csv,tkinter
from PIL import ImageTk,Image
import RWcsv
def check():
    bookname=read()
    booksdata=RWcsv.load_data();
    booksvalue=RWcsv.get_booksvalue();
    readflg=0;
    print("読み取ったデータは",bookname,"です")
    for i in range(booksvalue):
        if bookname==booksdata[i][0] and booksdata[i][1]=="0":
            print("借りることができます");
            readflg=1;
            break;
        elif bookname==booksdata[i][0] and booksdata[i][1]=="1":
            print("ほかの誰かが借りているため、借りることができません")
            print("借りている人は",booksdata[i][2],"です")
            readflg=1;
            break;

    if readflg==0:
        print("見つかりませんでした");
    return 0;

def edit_contrast(image, gamma):
    """コントラクト調整"""
    look_up_table = [np.uint8(255.0 / (1 + np.exp(-gamma * (i - 128.) / 255.)))
        for i in range(256)]
 
    result_image = np.array([look_up_table[value]
                             for value in image.flat], dtype=np.uint8)
    result_image = result_image.reshape(image.shape)
    return result_image
 
def read():
    print("カメラ起動中");
    if __name__ == "readqr":
        capture = cv2.VideoCapture(0)
        if capture.isOpened() is False:
            raise("IO Error")
    print("準備完了");
    while True:
        ret, frame = capture.read()
        if ret == False:
            continue
        # グレースケール化してコントラクトを調整する
        gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        image = edit_contrast(gray_scale, 5)
     
        # 加工した画像からフレームQRコードを取得してデコードする
        codes = decode(image)
        if len(codes) > 0:
            return codes[0][0].decode('utf-8', 'ignore')

def path_search(_filename,_bookname):
    list=RWcsv.read_csv(_filename)
    for i in range(len(list)):
        if list[i][0]==_bookname:
            return list[i][1]
    return -1
def borr_info(_window,_bookname):
    cv=tkinter.Canvas(_window,width=100,height=200)
    filename="db/bookpath.csv"
    book_path=path_search(filename,_bookname)
    book_img=Image.open(book_path)
    global img_tk2
    img_tk2=ImageTk.PhotoImage(book_img)
    cv.create_image(0,0,image=img_tk2,anchor=tkinter.NW)
    cv.pack()