import r2pipe, re

r2 = r2pipe.open("ex.o")

r2.cmd("aa")
# iz for strings in data section
# izz for all strings in whole binary
def R2findString():
    binary_strings = r2.cmd("iz")
    # 1Num 2Paddr 3Vaddr 4Len 5Size 6Section 7Type 8String
    binary_strings = re.split("\n", binary_strings)
    string_list = []
    for item in range(2, len(binary_strings)-1):
        temp = re.split(" ", binary_strings[item])
        global section
        section = {'Address': temp[1], 'Section': temp[7], 'Value': ""}
        for counter in range(9, len(temp)):
            section['Value'] += temp[counter]
            if counter != len(temp) - 1:
                section['Value'] += " "
        string_list.append(section)
    return section
    print(string_list)

