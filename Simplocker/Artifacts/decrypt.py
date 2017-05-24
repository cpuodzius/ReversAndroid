"""
*
*	Revers@ndroid - Simplocker
*
*	Atividade: Cassius Puodzius (@cpuodzius)
*	Script: Cassius Puodzius (@cpuodzius)
*
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*- 
 
import hashlib
import os
import sys
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

password = "jndlasf074hr"
 
def decrypt(password, enc):
	sha256 = SHA256.new()
	sha256.update(password)
	key = sha256.digest()
	iv = 16 * '\x00'
	return AES.new(key, AES.MODE_CBC, iv).decrypt(enc)
 
 
"""
	Recebe a chave em formato hexadecimal.
"""
def decrypt_file(file_path, key):
	print 'Decriptando o arquivo %s' % file_path
	with open(file_path, 'rb') as fo:
	    ciphertext = fo.read()
	dec = decrypt(key, ciphertext)
	with open('%s%s%s' % (file_path[:-4], '_dec', file_path[-4:]), 'wb') as fo:
	    fo.write(dec)
 
"""
	Recebe por parámetro o caminho da pasta que contém os arquivos cifrado ou um arquivo cifrado em particular.
"""
if __name__ == '__main__':
	if len(sys.argv) > 2:
		    sys.exit('ERROR: Não especificou o caminho absoluto do arquivo ou diretório dos arquivos a serem decriptados.')
 
	param_path = sys.argv[1]
 
	if not os.path.exists(param_path):
	    sys.exit('ERROR: O arquivo ou diretório especificado nãõ existe.')
 
	if not os.path.isdir(param_path):
	    decrypt_file(param_path, password)
	else:
	    for root,subdirs, files in os.walk(param_path):
	        for filename in files:
	            decrypt_file(os.path.join(root, filename), key)
