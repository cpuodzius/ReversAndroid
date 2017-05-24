"""
*
*       Revers@ndroid - Simplocker
*
*       Atividade: Cassius Puodzius (@cpuodzius)
*       Script: Cassius Puodzius (@cpuodzius)
*
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*- 
 
import hashlib
import os
import sys
from Crypto import Random
from Crypto.Cipher import AES
 
key = '9FF9D002556F252C2F324BB0137D54EF8C3E760ED395C44DDA471CD39D335ADB'
 
def decrypt(key, enc):
    return AES.new(key.decode('hex'), AES.MODE_ECB).decrypt(enc)
 
 
def decrypt_file(file_path, key):
    """
    Recibe una clave en formato hexadecimal.
    """
    print 'Descifrando archivo %s' % file_path
    with open(file_path, 'rb') as fo:
        ciphertext = fo.read()
    dec = decrypt(key, ciphertext)
    with open('%s%s%s' % (file_path[:-4], '_dec', file_path[-4:]), 'wb') as fo:
        fo.write(dec)
 
if __name__ == '__main__':
    """
    Recibe por parámetro la ruta absoluta de la carpeta que contiene los archivos cifrados o un archivo cifrado en particular.
    """
    if len(sys.argv) > 2:
        sys.exit('ERROR: No se especificó la ruta absoluta del archivo o directorio de archivos a descifrar.')
 
    param_path = sys.argv[1]
 
    if not os.path.exists(param_path):
        sys.exit('ERROR: El archivo o directorio especificado no existe.')
 
    if not os.path.isdir(param_path):
        decrypt_file(param_path, key)
    else:
        for root,subdirs, files in os.walk(param_path):
            for filename in files:
                decrypt_file(os.path.join(root, filename), key)
