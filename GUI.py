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

		self.checksum_token = tk.StringVar(self.window, "")
		self.entropy = tk.StringVar(self.window, "0")
		self.mnemonic = tk.StringVar(self.window, "")


		self.dic = get_dic(dic_path)


		self.window.bind('<Key>', self.update)
		self.window.bind('<Motion>', self.update)
	
	def check_type(self):
		if (self.type_select.get() == 'bin'):
			return (int(self.entropy.get(), 2))
		elif (self.type_select.get() == 'hex'):
			return (int(self.entropy.get(), 16)) 
		elif (self.type_select.get() == 'dec'):
			return(self.entropy.get())
		else:
			return (0)


	def generate(self):
		self.nbits = int(self.nbits_select.get())
		entropy = secrets.randbits(self.nbits)
		if (self.type_select.get() == 'bin'):
			self.entropy.set(bin(entropy)[2:])
		elif (self.type_select.get() == 'hex'):
			self.entropy.set(hex(entropy)[2:]) 
		elif (self.type_select.get() == 'dec'):
			self.entropy.set(entropy)

		self.update("")

	
	def update(self, event):
		entropy = int(self.check_type())
		try:
			self.checksum_token.set(checksum(entropy, self.nbits))
			self.mnemonic.set( get_mnemonic(bin(entropy)[2:] + self.checksum_token.get(), self.dic))
		except:
			self.mnemonic.set("please use a valid entropy")
			self.checksum_token.set("")
		


	def MainApp(self):

		type_list = ["bin", "hex", "dec"]
		nbits_list = ["128", "160", "192", "224", "256"]

		self.entry_entropy = tk.Entry(self.window, textvariable=self.entropy)
		self.label_checksum = tk.Label(self.window, textvariable=self.checksum_token)
		self.label_mnemonic = tk.Label(self.window, textvariable=self.mnemonic)
		self.button_generate = tk.Button(self.window, text="Generate", command=self.generate)
		self.type_select = ttk.Combobox(self.window, values=type_list)
		self.nbits_select = ttk.Combobox(self.window, values=nbits_list)

		self.type_select.set("bin")
		self.nbits_select.set("128")

		self.entry_entropy.pack()
		self.label_checksum.pack()
		self.button_generate.pack()
		self.label_mnemonic.pack()
		self.type_select.pack()
		self.nbits_select.pack()
		self.window.mainloop()




test = MnemonicGenerator()
test.MainApp()