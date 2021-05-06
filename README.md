# BIP_39-Mnemonic_Generator

"The aim of this repo is to show all the steps to get from a random (or not) number to a BIP_39 mnemonic passphrase/seed"

##  Use :

```
 ./mnemonic_gen [nbits] [dict_path] [entropy]
```
 nbits & dict_path are both optional default nbits is 256 , default dict is BIP39_EN            /!\ (nbits modulo 32 = 0 & 128 < nbits < 256)
 entropy is also optional and should only be used when nbits and dict_path are manually set , default entropy is an cryptographically secure pseudorandom number.
 ##### Examples :
 `````
 ./mnemonic_gen 
 ./mnemonic_gen 128
 ./mnemonic_gen 160 ./BIP_39_Wordlists/BIP39_FR
 ./mnemonic_gen 256 ./BIP_39_Wordlists/BIP39_FR 14235
 `````


### Requierements :

- base58  : pip install base58
- ecdsa   : pip install ecdsa
- secrets : pip install secrets


### Status :
[IN PROGRESS] - working on GUI

### Updates :

````
[ ] : GUI 
````

### Usefull links :

- [Checksum](https://learnmeabitcoin.com/technical/checksum)
- [Mnemonic](https://learnmeabitcoin.com/technical/mnemonic)
- [ECDSA](https://learnmeabitcoin.com/technical/ecdsa)
- [Private_Keys](https://learnmeabitcoin.com/technical/private-key)
- [Public_Keys](https://learnmeabitcoin.com/technical/public-key)
- [Adress](https://learnmeabitcoin.com/technical/address)
- [Extended_Keys](https://learnmeabitcoin.com/technical/extended-keys)

Thanks to https://learnmeabitcoin.com/ for all the informations needed to understand the Bitcoin Protocol.
