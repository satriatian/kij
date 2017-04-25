import utils
from operator import xor

try:
    input = raw_input
except NameError:
    pass

def encrypt(plaintext,key):
    ascii_key = [None] * len(key)
    for i in range(0,len(key)):
        ascii_key[i] = ord(key[i])

    key0 = [None] * 4
    key1 = [None] * 4
    j = 0
    for i in range(0,len(ascii_key)):
        if i <= 3:
            key0[i] = ascii_key[i]
        else:
            key1[j] = ascii_key[i]
            j = j + 1

    recur = len(plaintext)/4
    kosong = 4 - (len(plaintext)%4)
    if kosong > 0:
        recur = recur + 1

    asciitext = [None] * (recur*4)
    for i in range(0,len(asciitext)):
        if i < len(plaintext):
            asciitext[i] = ord(plaintext[i])
        else:
            asciitext[i] = ord(' ');
    x = 0
    for i in range(0,recur):
        for j in range(0,4):
            asciitext[x] = xor(asciitext[x], key0[j])
            x = x + 1

    x = 0
    hasilEncryp = [None] * len(asciitext)
    for i in range(0,recur):
        for j in range(0,4):
            hasilEncryp[x] = asciitext[x] + key1[j]
            x = x + 1

    hasilEncrypted = [None] * (len(hasilEncryp) - kosong)
    for i in range(0,len(hasilEncrypted)):
        hasilEncrypted[i] = chr(hasilEncryp[i])

    return hasilEncrypted

def decrypt(hasilEnkripsi, key):
    ascii_key = [None] * len(key)
    for i in range(0, len(key)):
        ascii_key[i] = ord(key[i])

    key0 = [None] * 4
    key1 = [None] * 4

    j = 0
    for i in range(0, len(ascii_key)):
        if i <= 3:
            key0[i] = ascii_key[i]
        else:
            key1[j] = ascii_key[i]
            j = j + 1

    recur = len(hasilEnkripsi) / 4
    sisa = len(hasilEnkripsi) % 4
    ukuranEncryp = ((4*recur) + sisa)
    asciiEncryp = [None] * ukuranEncryp
    for i in range(0, len(asciiEncryp)):
        asciiEncryp[i] = ord(hasilEnkripsi[i])

    for i in range(0,ukuranEncryp):
        asciiEncryp[i] = asciiEncryp[i] - key1[i%4]

    hasilDecryp = [None] * len(asciiEncryp)
    for i in range(0,ukuranEncryp):
        hasilDecryp[i] = xor(asciiEncryp[i],key0[i%4])

    hasilDecrypted = [None] * len(hasilDecryp)
    for i in range(0,len(hasilDecrypted)):
        hasilDecrypted[i] = chr(hasilDecryp[i])

    return hasilDecrypted

def main():
    print('Pilih : ')
    print('1. ENCRYPT')
    print('2. DECRYPT')
    choice = int(input())

    key_text = str(input('key : \n'))

    if(choice == 1):
        print ('string : ')
        plain = str(input())
        cipher = encrypt(plain, key_text)
        print('\nCipher : ')
        print(cipher)

    else:
        plain = str(input('string awal :\n'))
        cip = encrypt(plain, key_text)
        dechip = decrypt(cip, key_text)
        print('\nString :')
        print "Hasil dekripsi dari" + str(cip) + ":" + str(dechip)

    print('\nKeluar...')
    return

if __name__ == '__main__':
    main()