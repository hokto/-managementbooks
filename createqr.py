import qrcode
import os,tkinter,tkinter.filedialog
import pathlib
from PIL import ImageTk,Image
fTyp = [("","*")]
iDir = os.path.abspath(os.path.dirname(__file__))
def select_file(_window):#画像選択関数
	cv=tkinter.Canvas(_window,width=200,height=200,bg='black')
	file = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)#画像を選択させて絶対パスを取得
	file_path=pathlib.Path(file)
	print(file_path.relative_to(file_path.cwd()))
	book_img=Image.open(file_path.relative_to(file_path.cwd()))#画像の絶対パスを相対パスに変換して画像読み込み
	img_tk=ImageTk.PhotoImage(book_img)
	img_tk=ImageTk.PhotoImage(file="test.bmp")
	cv.create_image(0,0,image=img_tk,anchor=tkinter.NW)#画像描画
	cv.pack()
def QRcreatefun(_window,_name):#QRコード作成よう関数
	img=qrcode.make(_name.get())#QRコード作成
	img.save(_name.get()+'.png')
	_window.destroy()#QRコード作成ウィンドウ削除
def readbtn_click():
	print ("Read")
	#QRコード読み込み用関数
def createbtn_click():
	print("Create")
	Create_win=tkinter.Toplevel()#QRコード作成用ウィンドウ生成
	Create_win.title(u"Create QRcode Window")
	Create_win.geometry("700x700")
	#QR作成用関数
	name=tkinter.Entry(Create_win,width=20)#QRコード名をうちこませる
	name.place(x=100,y=100)
	Fileselectbtn=tkinter.Button(Create_win,text=u"File Select",command=lambda:select_file(Create_win))#ファイル選択させる関数にとぶボタン
	Fileselectbtn.pack()
	QRcreate=tkinter.Button(Create_win,text=u"Create QRcode",command=lambda:QRcreatefun(Create_win,name))#QRコードを作成する関数にとぶボタン
	QRcreate.pack()
window=tkinter.Tk()#mainWindow
window.title(u"Hello,world!!")
window.geometry("700x700")
Read_button=tkinter.Button(window,text=u"QRcode Read",command=readbtn_click)#QRコード読み取りウィンドウにとぶボタン
Make_button=tkinter.Button(window,text=u"QRcode Create",command=createbtn_click)#QRコード作成ウィンドウにとぶボタン
Read_button.pack()
Make_button.pack()
window.mainloop()