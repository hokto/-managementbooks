import qrcode
import os,tkinter,tkinter.filedialog
import readqr,RWcsv
import pathlib
from PIL import ImageTk,Image
fTyp = [("","*")]
iDir = os.path.abspath(os.path.dirname(__file__))
img_tk=0;
def update_path(list,data):
    for i in range(len(list)):
        if list[i][0]==data[0][0]:    
            list[i]=data[0]
            return list
    list+=data
    return list
def select_file(_window):#画像選択関数
	global img_tk;
	cv=tkinter.Canvas(_window,width=100,height=200,bg='black')
	file = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)#画像を選択させて絶対パスを取得
	file_path=pathlib.Path(file)
	global relative_path
	relative_path=file_path.relative_to(file_path.cwd())
	book_img=Image.open(relative_path)#画像の絶対パスを相対パスに変換して画像読み込み
	img_tk=ImageTk.PhotoImage(book_img)
	cv.create_image(0,0,image=img_tk,anchor=tkinter.NW)#画像描画
	cv.pack()
def registration(_name):
	bookname=_name.get()
	booksdata=RWcsv.load_data()
	booksvalue=RWcsv.get_booksvalue()
	for i in range(booksvalue):
		if booksdata[i][0]==bookname:
			return -1
	RWcsv.write(bookname,"0","none",1);
	return 0
def QRcreatefun(_window,_name):#QRコード作成よう関数
	img=qrcode.make(_name.get())#QRコード作成
	img.save(_name.get()+'.png')
	success_num=registration(_name)
	filename="db/bookpath.csv"
	path_csv=RWcsv.read_csv(filename)
	data=[[_name.get(),relative_path]]

	path_csv2=update_path(path_csv,data)
	RWcsv.write_csv(filename,path_csv2)
	_window.destroy()#QRコード作成ウィンドウ削除