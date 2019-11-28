import r2pipe

# variable = input('Executable name?')
r2 = r2pipe.open("ex.o")
r2.cmd("aaa")
r2.cmd("doo")
strs = r2.cmdj("iij") # Grab all imports used by binary ping in json format.
BinInfo = r2.cmdj("ij")
a=r2.cmdj("isj")

importList =[]
info=[]

for i in range(len(strs)):
    obj = strs[i]
    importList.append (str(obj['name']))

print("\n")

info.append(BinInfo["core"]["file"])
info.append(BinInfo["bin"]["os"])
info.append(BinInfo["bin"]["arch"])
info.append(BinInfo["bin"]["machine"])
info.append(BinInfo["bin"]["bits"])
info.append(BinInfo["bin"]["canary"])
info.append(BinInfo["bin"]["crypto"])
info.append(BinInfo["bin"]["nx"])
info.append(BinInfo["bin"]["pic"])
info.append(BinInfo["bin"]["relocs"])
info.append(BinInfo["bin"]["stripped"])
info.append(BinInfo["bin"]["endian"])
info.append(BinInfo["core"]["format"])

# print(info)

print("Executable info:")
print("address= ",info[0])
print("OS= ",info[1])
print("arch= ",info[2])
print("machine= ",info[3])
print("bits= ",info[4])
print("canary= ",info[5])
print("crypto= ",info[6])
print("nx= ",info[7])
print("pic= ",info[8])
print("relocs= ",info[9])
print("stripped= ",info[10])
print("endian= ",info[11])
print("format= ",info[12],"\n")

print("Executable import functions:")
print('\n'.join(map(str, importList)))
print("\n")


list=[]
add=[]
# all_recvs = r2.cmdj("axtj sym.imp.recv")

for i in range(len(a)):
    if (a[i]['type']) == "FUNC":
        list.append((str(a[i]['name'])))
        add.append((str(a[i]['vaddr'])))

print("functions")
for i in range(len(list)):
    print(list[i]," ",add[i])

print("\n")
print("variables")
for i in range(len(a)):
    if (a[i]['name']) == "multiply(int, int)" :
        address = "s "+ hex(a[i]['vaddr'])
        print(address)

        r2.cmd("ds")
        r2.cmd(address)
        variables=r2.cmd("afv")
        # print(variables)
        strings=r2.cmd("iz")
        print(strings)


r2.cmd("exit")
print('exit r2.')
