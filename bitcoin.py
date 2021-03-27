#!/usr/bin/python3
import hmac
import binascii
import ecdsa
import base58
from hashlib import sha512, sha256, new, pbkdf2_hmac


def get_bip32masterkey(seed):
	master_key = hmac.new(("Bitcoin seed").encode(), binascii.a2b_hex(seed) , sha512).hexdigest()
	return (master_key)


def get_xpub(xpriv, compressed=False):
	xpriv = bytes.fromhex(xpriv)
	signing_key = ecdsa.SigningKey.from_string(xpriv, curve = ecdsa.SECP256k1)
	verifying_key = signing_key.get_verifying_key()
	uncompressed_k = (bytes.fromhex("04") + verifying_key.to_string()).hex()
	compressed_k =  i2o_ECPublicKey(verifying_key.pubkey, True)
	if (compressed == True):
		return (compressed_k)
	else:
		return (uncompressed_k)


def get_addr(xpub, prefix):
	xpub_hash = get_xpub_hash(xpub)
	print("xpub_hash: ", xpub_hash,"\n\n")
	checksum_token = addr_checksum((prefix + xpub_hash))
	addr = prefix + xpub_hash + checksum_token
	print("checksumtoken: ", checksum_token,"\n\n")
	addr = base58.b58encode(bytes.fromhex(addr))
	print("addr: ", str(addr),"\n\n")
	return (str(addr))


def get_xpub_hash(xpub):
	xpub_hash = sha256(binascii.a2b_hex(xpub)).hexdigest()
	xpub_hash = new('ripemd160', binascii.a2b_hex(xpub_hash)).hexdigest()
	return (xpub_hash)


def get_child_key(master_key, index):
	print(hmac.new(master_key.encode(), index).hexdigest())

# pywallet openssl private key implementation
def i2o_ECPublicKey(pubkey, compressed=False):
    # public keys are 65 bytes long (520 bits)
    # 0x04 + 32-byte X-coordinate + 32-byte Y-coordinate
    # 0x00 = point at infinity, 0x02 and 0x03 = compressed, 0x04 = uncompressed
    # compressed keys: <sign> <x> where <sign> is 0x02 if y is even and 0x03 if y is odd
    if compressed:
        if pubkey.point.y() & 1:
            key = '03' + '%064x' % pubkey.point.x()
        else:
            key = '02' + '%064x' % pubkey.point.x()
    else:
        key = '04' + \
              '%064x' % pubkey.point.x() + \
              '%064x' % pubkey.point.y()

    return key


def addr_checksum(hash):
	checksum_token = sha256(binascii.a2b_hex(hash)).hexdigest()
	checksum_token = sha256(binascii.a2b_hex(checksum_token)).hexdigest()
	return (checksum_token[:8])