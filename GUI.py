from binascii import hexlify
import tkinter as tk
from tkinter import ttk
from mnemonic_gen import *


def clear_entry(entry):
	entry.delete(0, tk.END)

class MnemonicGenerator:


	def __init__(self, dic_path="./BIP39_Wordlists/BIP39_EN"):
		self.window = tk.Tk()
		self.window.title("MnemonicGenerator")
		self.window.geometry("1920x1080")

		self.checksum_token = tk.StringVar(self.window, "")
		self.entropy = tk.StringVar(self.window, "0")
		self.mnemonic = tk.StringVar(self.window, "")


		self.dic = get_dic(dic_path)


		self.window.bind('<Key>', self.update)
		self.window.bind('<Motion>', self.update)
	

	def generate(self):
		self.entropy.set(bin(secrets.randbits(int(self.nbits_select.get())))[2:])
		self.update("")

	
	def update(self, event):
		entropy = int(self.entropy.get(), 2)
		print(entropy)
		try:
			self.checksum_token.set(checksum(entropy, int(self.nbits_select.get())))
			self.mnemonic.set( get_mnemonic(bin(entropy)[2:] + self.checksum_token.get(), self.dic))
		except:
			self.mnemonic.set("please use a valid entropy")
			self.checksum_token.set("")
		


	def MainApp(self):

		nbits_list = ["128", "160", "192", "224", "256"]

		self.entry_entropy = tk.Entry(self.window, textvariable=self.entropy)
		self.label_checksum = tk.Label(self.window, textvariable=self.checksum_token)
		self.label_mnemonic = tk.Label(self.window, textvariable=self.mnemonic)
		self.button_generate = tk.Button(self.window, text="Generate", command=self.generate)
		self.nbits_select = ttk.Combobox(self.window, values=nbits_list)

		self.nbits_select.set("128")

		self.entry_entropy.pack(padx=10, pady=10, ipadx=500, ipady=10, side='left', expand=True)
		self.label_checksum.pack(padx=0, pady=0, ipadx=0, ipady=0, side='left', expand=True)
		self.button_generate.pack(side='bottom')
		self.nbits_select.pack(side='bottom')
		self.label_mnemonic.pack(padx=10, pady=10, ipadx=200, ipady=20, side='bottom')
		self.window.mainloop()




test = MnemonicGenerator()
test.MainApp()