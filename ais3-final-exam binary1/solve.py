#!/usr/bin/python

key = '\xca\x70\x93\xc8\x06\x54\xd2\xd5\xda\x6a\xd1\x59\xde\x45\xf9\xb5\xa6\x87\x19\xa5\x56\x6e\x63'

def uint8(a1):
    return a1 & 255

anwser = ''
for i in range(len(key)):
    isfind = False
    for al in range(256):
        ''' Code in IDA 
        if ( *(_BYTE *)(i + 0x804A014) != (
        (unsigned __int8)((unsigned __int8)(*(_BYTE *)(i + a1) ^ i) << (((unsigned __int8)i ^ 9) & 3)) |
        (unsigned __int8)((signed int)(unsigned __int8)(*(_BYTE *)(i + a1) ^ i) >> (8 - (((unsigned __int8)i ^ 9) & 3)))) + 8 )
        '''
        v1 = uint8((uint8(al ^ i)) << ((uint8(i)^9) & 3))
        v2 = uint8((uint8(al ^ i)) >> (8 - ((uint8(i)^9) & 3)))
        if ord(key[i]) ==  uint8((v1 | v2)+8) :
            anwser += chr(al)
            isfind = True
            break
    if not isfind:
        anwser += ' '
print anwser