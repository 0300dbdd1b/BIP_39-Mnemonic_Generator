#!/usr/bin/python3

### This file contain all the function to generate a BIP39 Mnemonic Seed
import secrets
import binascii
import sys

from hashlib import sha256 , pbkdf2_hmac

def resize(str):
	l = len(str)
	while (l % 32 != 0):
		str = "0" + str
		l += 1
	return (str)


# Returns the checksum from the given entropy (entropy is an integer)
def checksum(entropy):
	entropy_len = len(resize(bin(entropy)[2:]))
	entropy_hex = hex(entropy)[2:]
	entropy_hex = entropy_hex if len(entropy_hex) % 2 == 0 else "0" + entropy_hex
	checksum = resize(bin(int(sha256(binascii.a2b_hex(entropy_hex)).hexdigest(), 16))[2:])[:int(entropy_len/32)]
	return (checksum)


# Get the BIP39 Wordlist dict from the specified filepath
def get_dic(dict_path="./BIP39_Wordlists/BIP39_EN"):
	wordlist = {}
	with open(dict_path) as dict:
		key = 0
		for line in dict:
			(key, val) = key , line
			wordlist[int(key)] = val
			key += 1
		return (wordlist)

# Get the mnemonic phrase from the given entropy & dict (entropy is an integer)
def get_mnemonic(entropy, dict_path="./BIP39_Wordlists/BIP39_EN"):
	mnemonic = {}
	index = 1
	i = 0
	checksumed_entropy = resize(bin(entropy)[2:]) + checksum(entropy)
	dict = get_dic(dict_path)
	while i < len(checksumed_entropy):
		word = int(checksumed_entropy[i:i+11], 2)
		word = dict.get(word)
		(index, word) = index , word[:-1]
		mnemonic[int(index)] = word
		index += 1
		i += 11
	return (mnemonic)


# Transform a mnemonic phrase & passphrase to a BIP39 seed
def mnemonic_to_seed(mnemonic, passphrase=""):
	mnemonic_phrase = ""
	for key in mnemonic:
		mnemonic_phrase = mnemonic_phrase + mnemonic[key] + " "
	mnemonic_phrase = mnemonic_phrase[:-1] + passphrase
	seed = pbkdf2_hmac("SHA512", bytes(mnemonic_phrase.encode()), bytes(("mnemonic" + passphrase).encode()), 2048).hex()
	return (seed)




# Generates a cryptographically secure pseudorandom number of size nbits and returns its mnemonic phrase representation
def get_bip39_mnemonic(nbits=128, dict_path="./BIP39_Wordlists/BIP39_EN"):
	if nbits % 32 != 0:
		return ("Error : the entropy size must be a multiple of 32")
	entropy = secrets.randbits(nbits)
	print(resize(bin(entropy)[2:]))
	mnemonic = get_mnemonic(entropy, dict_path)
	return mnemonic

	


# Main

if __name__ == "__main__":
	if len(sys.argv) > 3:
		mnemonic = get_mnemonic(int(sys.argv[3]), str(sys.argv[2]))
	elif len(sys.argv) > 2:
		mnemonic = get_bip39_mnemonic(int(sys.argv[1]), str(sys.argv[2]))
	elif len(sys.argv) > 1:
		mnemonic = get_bip39_mnemonic(int(sys.argv[1]))
	else:
		mnemonic = get_bip39_mnemonic()
	print(mnemonic)
	if type(mnemonic) == "string":
		seed = mnemonic_to_seed(mnemonic)
		print("seed: ", seed)