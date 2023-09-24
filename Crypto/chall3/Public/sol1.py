from z3 import *
import binascii

s = '4b851cc4cdd1c7a3b7a3d83095a46a320e6b21e9e5afab7b8869d930c9cd981a0523a037faca8425f9a921c6ebca8f7087f8aab5bc53fe9cd5acfa9e'

encrypted = []
for i in range(0, len(s), 2):
    encrypted.append(binascii.unhexlify(s[i+1] + s[i])[0])

print('message len:', len(encrypted)-1)
print(encrypted)

encrypted = [IntVal(i) for i in encrypted]
message = [Int('flag%d' % i) for i in range(len(encrypted)-1)]

solver = Solver()

ml = len(encrypted) - 1


for i in range(ml):
    if i == ml - 33:
        solver.add(message[i] == ord('|'))
    else:

        solver.add(message[i] < 127)
        solver.add(message[i] >= 32)

for i in range(ml):
    solver.add(encrypted[i+1] == (message[i] + message[ml-32+i%32] + encrypted[i]) % 126)

if solver.check() == sat:
    m = solver.model()
    s = []
    for i in range(ml):
        s.append(m[message[i]].as_long())
    print(bytes(s))
else:
    print('unsat') 