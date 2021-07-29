from tkinter import *

global w, h, x, y


def password_check(password):
	SpecialSym = ['$', '@', '#', '%']
	val = True

	if len(password) < 6:
		print('length should be at least 6')
		val = False

	if len(password) > 20:
		print('length should be not be greater than 8')
		val = False

	if not any(char.isdigit() for char in password):
		print('Password should have at least one numeral')
		val = False

	if not any(char.isupper() for char in password):
		print('Password should have at least one uppercase letter')
		val = False

	if not any(char.islower() for char in password):
		print('Password should have at least one lowercase letter')
		val = False

	if not any(char in SpecialSym for char in password):
		print('Password should have at least one of the symbols $@#')
		val = False

	return val


def Kayıt_olma():
	file = open('Kullanıcı.txt', "a")
	file.write("")
	file.close()


def Login_bilgi_alma(name_entry, surname_entry, password_entry):
	Name = name_entry.get()
	Surname = surname_entry.get()
	Password = password_entry.get()


def Login_sayfası_açma():
	Login_sayfası = Tk()
	Login_sayfası.title("Login")

	Login_sayfası.geometry('%dx%d+%d+%d' % (w, h, x, y))

	name = StringVar()
	surname = StringVar()
	password = StringVar()

	Label(Login_sayfası, text="Lütfen bilgilerinizi girin", font="1").pack()
	Label(Login_sayfası, text="").pack()

	Label(Login_sayfası, text="Adınız", font="17").pack()

	name_entry = Entry(Login_sayfası, textvariable=name, width="40", font="1").pack()
	Label(Login_sayfası, text="").pack()

	Label(Login_sayfası, text="Soyadınız", font="17").pack()

	surname_entry = Entry(Login_sayfası, textvariable=surname, width="40", font="1").pack()
	Label(Login_sayfası, text="").pack()

	Label(Login_sayfası, text="Şifreniz", font="17").pack()

	password_entry = Entry(Login_sayfası, textvariable=password, show='*', width="40", font="1").pack()
	Label(Login_sayfası, text="").pack()

	Button(text="Login", bg="blue", height="5", width="40", command=lambda: [Login_sayfası_kapama(Login_sayfası),
	                                                                         Login_bilgi_alma(name_entry, surname_entry,
	                                                                                          password_entry)]).pack()

	Login_sayfası.mainloop()


def Ana_sayfa():
	Main_Page = Tk()
	Main_Page.title("21 Oyunu")

	w = 500
	h = 400
	ws = Main_Page.winfo_screenwidth()
	hs = Main_Page.winfo_screenheight()
	x = (ws / 2) - (w / 2)
	y = (hs / 2) - (h / 2)

	Main_Page.geometry('%dx%d+%d+%d' % (w, h, x, y))

	Label(text="Giriş yapın veya Kayıt olsun", width="300", height="1", font=27).pack()
	Label().pack()

	Button(text="Giriş yapın", bg="blue", height="8", width="50", command=lambda: [Ana_sayfa_kapama(Main_Page),
	                                                                               Login_sayfası_açma()]).pack()
	Label().pack()

	Button(text="Kayıt olun", bg="blue", height="8", width="50",
	       command=lambda: [Ana_sayfa_kapama(Main_Page)]).pack()

	Main_Page.mainloop()


def Ana_sayfa_kapama(Main_Page):
	Main_Page.destroy()


def Login_sayfası_kapama(Login_sayfası):
	Login_sayfası.destroy()


if __name__ == '__main__':
	Ana_sayfa()
