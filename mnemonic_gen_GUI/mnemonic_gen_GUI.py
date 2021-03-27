#!/usr/bin/python3

import secrets
from tkinter import Tk, IntVar, StringVar, Label, Entry, Button
from mnemonic_gen import resize_bin, checksum, get_mnemonic, mnemonic_to_seed, get_dic

class app:
	def  __init__(self):
		self.master = Tk()

		self.dict_path = "../BIP39_Wordlists/BIP39_EN"
		self.nbits = IntVar(self.master, 128)
		self.entropy_intvar = IntVar(self.master, 150) 
		self.entropy_binvar = StringVar(self.master)
		self.checksumtoken = StringVar(self.master)
		self.mnemonic = StringVar(self.master)
		self.seed = StringVar(self.master)


		self.L_seed = Label(self.master, textvariable=self.seed)
		self.L_mnemonic = Label(self.master, textvariable=self.mnemonic)
		self.L_checksumtoken = Label(self.master, textvariable=self.checksumtoken)
		self.E_entropy_int = Entry(self.master, textvariable=self.entropy_intvar)
		self.E_entropy_bin = Entry(self.master, textvariable=self.entropy_binvar)
		self.E_nbits = Entry(self.master, textvariable=self.nbits)
		self.B_entropy_gen = Button(self.master, text="Generate", command=self.generate)
		self.B_update = Button(self.master, text="Update", command=self.update)


	def generate(self):
		self.entropy_intvar.set(secrets.randbits(self.nbits.get()))
	
	def update(self):
		entropy = self.entropy_intvar.get()
		entropy_bin =  resize_bin(bin(entropy)[2:], self.nbits.get())
		self.entropy_binvar.set(entropy_bin)
		checksumv = checksum(entropy, self.nbits.get())
		self.checksumtoken.set(checksumv.replace(resize_bin(bin(entropy)[2:], self.nbits.get()), ''))
		self.mnemonic.set(get_mnemonic(checksumv, get_dic(self.dict_path)))
		self.seed.set(mnemonic_to_seed(get_mnemonic(checksumv, get_dic(self.dict_path)), ""))


	def MainApp(self):
		self.E_entropy_int.pack()
		self.E_entropy_bin.pack()
		self.L_checksumtoken.pack()
		self.L_mnemonic.pack()
		self.L_seed.pack()
		self.B_entropy_gen.pack()
		self.E_nbits.pack()
		self.B_update.pack()

		self.master.mainloop()

master = app()
master.MainApp()