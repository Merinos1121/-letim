import shutil
from tkinter import *
import promptlib


def Ana_sayfa():
	Main = Tk()
	Main.title = "Silme"

	w = 500
	h = 400
	ws = Main.winfo_screenwidth()
	hs = Main.winfo_screenheight()
	x = (ws / 2) - (w / 2)
	y = (hs / 2) - (h / 2)

	Main.geometry('%dx%d+%d+%d' % (w, h, x, y))

	Label(text="Silme", font=("Arial", 27)).pack()

	Button(text="Çalıştır", font=("Arial", 27), bg="blue", command=lambda: [Silme()]).pack()

	Main.mainloop()


def Silme():
	prompter = promptlib.Files()

	dosya = prompter.dir()
	uzunluk = len(dosya)

	if uzunluk > 0:
		shutil.rmtree(dosya)
	else:
		print('Çok kısa')


if __name__ == '__main__':
	Ana_sayfa()