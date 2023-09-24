import string
from hashlib import md5
flag = "KMA{"
hash_str = "16ab78b0c0654e663d7e2e22ac0a9b7a"
flag_hash = md5(flag.encode()).hexdigest()
bin_enc = "10010111001101100000111110111010001011000111000101010110110001101101001011100101110000111010110101111000101111001111110100000010001111000111011011011110101011111110011000111110111101001001000100011010001101111101"
mid = "101000101100011100010101011011000110110100101110010111000011101011010111100010111100111111010000001000111100011101101101111010101111111001100011111011110100100100010001101000110"
def encode(m):
    return ''.join(bin(ord(c))[2:] for c in m)

print(len(mid))
def binary_to_letter(binary_str):
    decimal_value = int(binary_str, 2)

    character = chr(decimal_value)

    return character


res = "(X8" 
end = "HFF"
mid_part = mid[len(encode(res)):]
def indc(c):
    if c in string.printable[:-6]:
        return True
    return False


all_flag = []
def findres(end):
    mid_part = mid[len(encode(end)):]
    if len(end) == 27:
        all_flag.append(end)
        return
    last6 = binary_to_letter(mid_part[:6])
    last7 = binary_to_letter(mid_part[:7])

    if indc(last6) and not indc(last7) :
        end = end + last6 
        findres(end)
    elif not indc(last6) and  indc(last7) :
        end = end + last7 
        findres(end)
    elif indc(last6) and indc(last7):
        end1 = end +last6 
        findres(end1)
        end2 = end + last7 
        findres(end2)
    else :
        return
findres(res)
print(all_flag)
print("--------------------------------------")
for x in all_flag:
    flag = "KMA{" + x + "}"
    flag_hash = md5(flag.encode()).hexdigest()
    if flag_hash == hash_str:
        print(flag)

print(len(all_flag))



