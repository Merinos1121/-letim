import random
from tkinter import *
from PIL import ImageTk, Image


def Doğru_kapı_seçme():
	Doğru_kapı = str(random.choice('abc'))

	if Doğru_kapı == 'a':
		Kapı_1 = 1
		Kapı_2 = 0
		Kapı_3 = 0
		Seçim_sayfası_açma(Kapı_1, Kapı_2, Kapı_3)

	if Doğru_kapı == 'b':
		Kapı_1 = 0
		Kapı_2 = 1
		Kapı_3 = 0
		Seçim_sayfası_açma(Kapı_1, Kapı_2, Kapı_3)

	if Doğru_kapı == 'c':
		Kapı_1 = 0
		Kapı_2 = 0
		Kapı_3 = 1
		Seçim_sayfası_açma(Kapı_1, Kapı_2, Kapı_3)


def Kullanıcı_kapı_seçme(Kapı_1, Kapı_2, Kapı_3, seçim):
	if seçim == 1:
		if 1 == Kapı_1:
			Kazanma_sayfası_açma()
		else:
			Kaybetme_sayfası_açma()
	else:
		if seçim == 2:
			if 1 == Kapı_2:
				Kazanma_sayfası_açma()
			else:
				Kaybetme_sayfası_açma()
		else:
			if seçim == 3:
				if 1 == Kapı_3:
					Kazanma_sayfası_açma()
				else:
					Kaybetme_sayfası_açma()


def Kazanma_sayfası_açma():
	Kazanma_sayfası = Tk()
	Kazanma_sayfası.title('Kazandınız')

	w = 400
	h = 340
	ws = Kazanma_sayfası.winfo_screenwidth()
	hs = Kazanma_sayfası.winfo_screenheight()
	x = (ws / 2) - (w / 2)
	y = (hs / 2) - (h / 2)

	Kazanma_sayfası.geometry('%dx%d+%d+%d' % (w, h, x, y))
	Kazanma_sayfası.resizable(False, False)

	Kapı_araba_canvas = Canvas(width=180, height=160)
	Kapı_araba_canvas.place(x=110, y=20)
	img_araba = ImageTk.PhotoImage(Image.open('araba.png'))
	Kapı_araba_canvas.create_image(1, 1, anchor=NW, image=img_araba)

	Label(text="Kazandınız", font=("Arial", 40)).place(x=70, y=180)

	Button(text='Tamam', bg='blue', font=("Arial", 20),
	       command=lambda: [Kazanma_sayfası_kapama(Kazanma_sayfası), Ana_sayfa()]).place(x=140, y=250)

	Kazanma_sayfası.mainloop()


def Kaybetme_sayfası_açma():
	Kaybetme_sayfası = Tk()
	Kaybetme_sayfası.title('Kaybettiniz')

	w = 400
	h = 340
	ws = Kaybetme_sayfası.winfo_screenwidth()
	hs = Kaybetme_sayfası.winfo_screenheight()
	x = (ws / 2) - (w / 2)
	y = (hs / 2) - (h / 2)

	Kaybetme_sayfası.geometry('%dx%d+%d+%d' % (w, h, x, y))
	Kaybetme_sayfası.resizable(False, False)

	Kapı_keçi_canvas = Canvas(width=180, height=160)
	Kapı_keçi_canvas.place(x=140, y=20)
	img_keçi = ImageTk.PhotoImage(Image.open('keçi.png'))
	Kapı_keçi_canvas.create_image(1, 1, anchor=NW, image=img_keçi)

	Label(text="Kaybettiniz", font=("Arial", 40)).place(x=70, y=180)

	Button(text='Tamam', bg='blue', font=("Arial", 20), command=lambda: [Kaybetme_sayfası_kapama(Kaybetme_sayfası),
	                                                                     Ana_sayfa()]).place(x=140, y=250)

	Kaybetme_sayfası.mainloop()


def Seçim_sayfası_açma(Kapı_1, Kapı_2, Kapı_3):
	Seçim_sayfası = Tk()
	Seçim_sayfası.title('Seçin')

	w = 500
	h = 370
	ws = Seçim_sayfası.winfo_screenwidth()
	hs = Seçim_sayfası.winfo_screenheight()
	x = (ws / 2) - (w / 2)
	y = (hs / 2) - (h / 2)

	Seçim_sayfası.geometry('%dx%d+%d+%d' % (w, h, x, y))
	Seçim_sayfası.resizable(False, False)

	Label(text="Bir kapı seçin", font=("Arial", 40)).place(x=90, y=10)

	Kapı_1_canvas = Canvas(width=80, height=160)
	Kapı_1_canvas.place(x=48, y=100)
	img1 = ImageTk.PhotoImage(Image.open('kapı.jpg'))
	Kapı_1_canvas.create_image(1, 1, anchor=NW, image=img1)

	Button(text="1.Kapı", bg="blue", height="1", width="10", font=("Arial", 17), command=lambda: [
		Seçim_sayfası_kapama(Seçim_sayfası), Kullanıcı_kapı_seçme(Kapı_1, Kapı_2, Kapı_3, 1)]).place(x=20, y=270)

	Kapı_2_canvas = Canvas(width=80, height=160)
	Kapı_2_canvas.place(x=205, y=100)
	img2 = ImageTk.PhotoImage(Image.open('kapı.jpg'))
	Kapı_2_canvas.create_image(1, 1, anchor=NW, image=img2)

	Button(text="2.Kapı", bg="blue", height="1", width="10", font=("Arial", 17), command=lambda: [
		Seçim_sayfası_kapama(Seçim_sayfası), Kullanıcı_kapı_seçme(Kapı_1, Kapı_2, Kapı_3, 2)]).place(x=180, y=270)

	Kapı_3_canvas = Canvas(width=80, height=160)
	Kapı_3_canvas.place(x=365, y=100)
	img3 = ImageTk.PhotoImage(Image.open('kapı.jpg'))
	Kapı_3_canvas.create_image(1, 1, anchor=NW, image=img3)

	Button(text="3.Kapı", bg="blue", height="1", width="10", font=("Arial", 17), command=lambda: [
		Seçim_sayfası_kapama(Seçim_sayfası), Kullanıcı_kapı_seçme(Kapı_1, Kapı_2, Kapı_3, 3)]).place(x=340, y=270)

	Seçim_sayfası.mainloop()


def Ana_sayfa():
	Main_Page = Tk()
	Main_Page.title("3 Kapı Oyunu")

	w = 500
	h = 300
	ws = Main_Page.winfo_screenwidth()
	hs = Main_Page.winfo_screenheight()
	x = (ws / 2) - (w / 2)
	y = (hs / 2) - (h / 2)

	Main_Page.geometry('%dx%d+%d+%d' % (w, h, x, y))
	Main_Page.resizable(False, False)

	Label(text="Oyuna başlayın", font=("Arial", 40)).place(x=65, y=10)

	Button(text="Başla", bg="blue", height="4", width="25", font=("Arial", 17),
	       command=lambda: [Ana_sayfa_kapama(Main_Page), Doğru_kapı_seçme()]).place(x=80, y=90)

	Main_Page.mainloop()


def Ana_sayfa_kapama(Main_Page):
	Main_Page.destroy()


def Seçim_sayfası_kapama(Seçim_sayfası):
	Seçim_sayfası.destroy()


def Kazanma_sayfası_kapama(Kazanma_sayfası):
	Kazanma_sayfası.destroy()


def Kaybetme_sayfası_kapama(Kaybetme_sayfası):
	Kaybetme_sayfası.destroy()


if __name__ == '__main__':
	Ana_sayfa()
