sset = ["-", "G", "Y"]

result = ["-", "-", "-", "-", "-"]

while ("".join(result) != "YYYYY"):
    print("".join(result))
    for i in range(5):
        nex = sset.index(result[i])+1
        if nex == 3:
            nex = 0
        result[i] = sset[nex]
        if nex != 0:
            break
print("YYYYY")

# Generates all possible results, including impossible oens containing 4G and 1Y