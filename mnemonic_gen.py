import secrets
import binascii
from hashlib import sha256 , pbkdf2_hmac

def main():
	dict_path = "./BIP39_Wordlists/BIP39_EN"
	nbits = 256
	entropy = secrets.randbits(nbits)
	checksum_bin = checksum(entropy, nbits)
	mnemonic = get_mnemonic(checksum_bin, get_dic(dict_path))
	seed = mnemonic_to_seed(mnemonic, "")
	print("Entropy : " , entropy , "\nEntropy Bin : ", resize_bin(bin(entropy)[2:], nbits), "\nnbits : ", nbits , "\n\n")
	print("Checksum : ", checksum_bin, "\nChecksum Token : " , checksum_bin.replace(resize_bin(bin(entropy)[2:], nbits), ''), "\n\n")
	print("Mnemonic :" , mnemonic,"\n")
	print("Seed : ", seed)


def resize_bin(bin, nbits):
	if nbits - len(bin) > 0:
		for i in range(0, nbits - len(bin)):
			bin = "0" + bin
	return (bin)


def checksum(entropy, nbits):
	entropy_hex = hex(entropy)[2:]
	entropy_bin = bin(entropy)[2:]
	entropy_bin = resize_bin(entropy_bin, nbits)
	fingerprint_hash = sha256(bytearray.fromhex(entropy_hex)).hexdigest()
	fingerprint = bin(int(fingerprint_hash, 16))[2:]
	fingerprint = resize_bin(fingerprint, 256)
	checksum = str(entropy_bin) + fingerprint[:int(nbits/32)]
	return (checksum)

def get_dic(dict_path):
	wordlist = {}
	with open(dict_path) as dict:
		key = 0
		for line in dict:
			(key, val) = key , line
			wordlist[int(key)] = val
			key += 1
		return (wordlist)

def get_mnemonic(checksum, dict):
	mnemonic = {}
	index = 1
	i = 0
	while i < len(checksum):
		word = int(checksum[i:i+11], 2)
		word = dict.get(word)
		(index, word) = index , word[:-1]
		mnemonic[int(index)] = word
		index += 1
		i += 11
	return (mnemonic)

def mnemonic_to_seed(mnemonic, passphrase):
	mnemonic_phrase = ""
	for key in mnemonic:
		mnemonic_phrase = mnemonic_phrase + mnemonic[key] + " "
	mnemonic_phrase = mnemonic_phrase[:-1] + passphrase
	seed = pbkdf2_hmac("SHA512", bytes(mnemonic_phrase.encode()), bytes(("mnemonic" + passphrase).encode()), 2048).hex()
	return (seed)


main()
