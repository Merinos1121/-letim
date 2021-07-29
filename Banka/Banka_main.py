from tkinter import *
from forex_python.converter import CurrencyRates

global w, h, x, y
global toplam_para


def Currency(CurrencyRates):
	c = CurrencyRates()
	a = float(c.get_rate('USD', 'TRY'))
	b = float(c.get_rate("EUR", "TRY"))
	Okuma(a, b)


def Okuma(a, b):
	file = open(r'C:\Users\EXCALIBUR\OneDrive\Masaüstü\Ben\Diğer\Python\İşletim\Banka\Para.txt', 'r')
	all_lines = file.readlines()

	satır_1 = (all_lines[0])
	satır_TRY = float(satır_1)

	satır_2 = (all_lines[1])
	satır_USD = float(satır_2)

	satır_3 = (all_lines[2])
	satır_EUR = float(satır_3)

	Çevirme(a, b, satır_TRY, satır_USD, satır_EUR)


def Çevirme(a, b, satır_TRY, satır_USD, satır_EUR):
	USD_TRY = satır_USD * a
	USD_TRY_düz = round(USD_TRY)

	EUR_TRY = satır_EUR * b
	EUR_TRY_düz = round(EUR_TRY)

	Toplama(satır_TRY, USD_TRY_düz, EUR_TRY_düz)


def Toplama(satır_TRY, USD_TRY_düz, EUR_TRY_düz):
	toplam_para = int(satır_TRY + USD_TRY_düz + EUR_TRY_düz)
	Ana_sayfa(toplam_para)


def Değiştirme(file_name, line_num, text):
	lines = open(file_name, 'r').readlines()
	lines[line_num] = text + '\n'
	out = open(file_name, 'w')
	out.writelines(lines)
	out.close()
	Ekleme_popup()


def Ekleme_karşılaştırma(value_inside, Miktar_entry):
	birim = format(value_inside.get())
	file = open(r'C:\Users\EXCALIBUR\OneDrive\Masaüstü\Ben\Diğer\Python\İşletim\Banka\Para.txt', 'r')
	all_lines = file.readlines()
	if birim == 'TRY':
		sıra = 0
		satır_1 = (all_lines[0])
		para = int(satır_1)
	else:
		if birim == 'USD':
			sıra = 1
			satır_2 = (all_lines[1])
			para = int(satır_2)
		else:
			if birim == 'EUR':
				sıra = 2
				satır_3 = (all_lines[2])
				para = int(satır_3)
			else:
				sıra = 'a'

	if isinstance(sıra, int):
		değer_önce = int(Miktar_entry.get())
		değer = str(değer_önce + para)
		try:
			int(değer)
			isInt = True
		except ValueError:
			isInt = False

		if isInt:
			Değiştirme('Para.txt', sıra, değer)
		else:
			print('Not an integer')
	else:
		print('Birim')


def Para_ekleme_sayfası(w, h, x, y):
	Ekleme = Tk()
	Ekleme.title = "Para ekleme"

	Ekleme.geometry('%dx%d+%d+%d' % (w, h, x, y))

	miktar = StringVar()

	options_list = ['USD', 'EUR', 'TRY']
	value_inside = StringVar(Ekleme)
	value_inside.set("Select an Option")
	OptionMenu(Ekleme, value_inside, *options_list).pack()

	Miktar_entry = Entry(Ekleme, textvariable=miktar, width="40", font="1")
	Miktar_entry.pack()

	Button(Ekleme, text='Submit', command=lambda: [Ekleme_karşılaştırma(value_inside, Miktar_entry)]).pack()

	Button(Ekleme, text='Ana sayfaya dön', command=lambda: [Para_ekleme_kapama(Ekleme), Currency(CurrencyRates)]).pack()

	Ekleme.mainloop()


def Çıkarma_karşılaştırma(value_inside, Miktar_entry):
	birim = format(value_inside.get())
	file = open(r'C:\Users\EXCALIBUR\OneDrive\Masaüstü\Ben\Diğer\Python\İşletim\Banka\Para.txt', 'r')
	all_lines = file.readlines()
	if birim == 'TRY':
		sıra = 0
		satır_1 = (all_lines[0])
		para = int(satır_1)
	else:
		if birim == 'USD':
			sıra = 1
			satır_2 = (all_lines[1])
			para = int(satır_2)
		else:
			if birim == 'EUR':
				sıra = 2
				satır_3 = (all_lines[2])
				para = int(satır_3)
			else:
				sıra = 'a'

	if isinstance(sıra, int):
		değer_önce = int(Miktar_entry.get())
		değer = str(para - değer_önce)
		try:
			int(değer)
			isInt = True
		except ValueError:
			isInt = False

		if isInt:
			Değiştirme('Para.txt', sıra, değer)
		else:
			print('Not an integer')
	else:
		print('Birim')


def Para_çıkarma_sayfası(w, h, x, y):
	Çıkarma = Tk()
	Çıkarma.title = "Para çıkarma"

	Çıkarma.geometry('%dx%d+%d+%d' % (w, h, x, y))

	miktar = StringVar()

	options_list = ['USD', 'EUR', 'TRY']
	value_inside = StringVar(Çıkarma)
	value_inside.set("Select an Option")
	OptionMenu(Çıkarma, value_inside, *options_list).pack()

	Miktar_entry = Entry(Çıkarma, textvariable=miktar, width="40", font="1")
	Miktar_entry.pack()

	Button(Çıkarma, text='Submit', command=lambda: [Çıkarma_karşılaştırma]).pack()

	Button(Çıkarma, text='Ana sayfaya dön',
	       command=lambda: [Para_çıkarma_kapama(Çıkarma), Currency(CurrencyRates)]).pack()

	Çıkarma.mainloop()


def Ana_sayfa(toplam_para):
	Main = Tk()
	Main.title = "Banka"

	w = 500
	h = 400
	ws = Main.winfo_screenwidth()
	hs = Main.winfo_screenheight()
	x = (ws / 2) - (w / 2)
	y = (hs / 2) - (h / 2)

	Main.geometry('%dx%d+%d+%d' % (w, h, x, y))

	Label(text="Güncel paranız", font=("Arial", 27)).pack()

	Label(text=toplam_para, font=("Arial", 27)).pack()

	Button(text="Para ekle", font=("Arial", 27), bg="blue", command=lambda: [Ana_sayfa_kapama(Main),
	                                                                         Para_ekleme_sayfası(w, h, x, y)]).pack()

	Button(text="Para çıkar", font=("Arial", 27), bg="blue", command=lambda: [Ana_sayfa_kapama(Main),
	                                                                          Para_çıkarma_sayfası(w, h, x, y)]).pack()

	Main.mainloop()


def Ekleme_popup():
	popup = Tk()
	popup.title = 'İşlem Başarılı'

	a = 350
	b = 200
	ad = popup.winfo_screenwidth()
	bd = popup.winfo_screenheight()
	k = (ad / 2) - (a / 2)
	m = (bd / 2) - (b / 2)

	popup.geometry('%dx%d+%d+%d' % (a, b, k, m))

	Label(popup, text='Başarıyla para eklendi', font=("Arial", 17)).place(x=60, y=50)

	Button(popup, text='Tamam', bg='blue', font=("Arial", 17), command=lambda: [Ekleme_popup_kapama(popup)]) \
		.place(x=120, y=80)

	popup.mainloop()


def Çıkarma_popup():
	popup = Tk()
	popup.title = 'İşlem Başarılı'

	a = 350
	b = 200
	ad = popup.winfo_screenwidth()
	bd = popup.winfo_screenheight()
	k = (ad / 2) - (a / 2)
	m = (bd / 2) - (b / 2)

	popup.geometry('%dx%d+%d+%d' % (a, b, k, m))

	Label(popup, text='Başarıyla para çıkarıldı', font=("Arial", 17)).place(x=60, y=50)

	Button(popup, text='Tamam', bg='blue', font=("Arial", 17), command=lambda: [Çıkarma_popup_kapama(popup)]) \
		.place(x=120, y=80)

	popup.mainloop()


def Ana_sayfa_kapama(Main):
	Main.destroy()


def Para_ekleme_kapama(Ekleme):
	Ekleme.destroy()


def Ekleme_popup_kapama(popup):
	popup.destroy()


def Para_çıkarma_kapama(Çıkarma):
	Çıkarma.destroy()


def Çıkarma_popup_kapama(popup):
	popup.destroy()


if __name__ == '__main__':
	Currency(CurrencyRates)
