import sys
import math
import binascii
import re

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# message = raw_input()
message = "CC"
output = ""

for x in [m.group(0) for m in re.finditer(r"(\d)\1*", "".join([str(bin(int(binascii.hexlify(y), 16)))[2:] for y in list(message)]), 16)]:
	sys.stdout.write( "{0} {1} ".format("0" if '1' in x else '00', "0" * len(x)))
# Write an action using p