import base64
import os, sys
import time

import r2pipe


class DynamicAnalysis:
    pass

    def setPath(self, path):
        self.registers = {}
        try:
            self.analyzer = r2pipe.open(path)
            self.analyzer.cmd("aaaa")
            self.analyzer.cmd("doo")
            self.analyzer.cmd("e dbg.profile=r2.rr2")
            print("The Binary is ready for dynamic analysis")



        except:
            self.analyzer = None
            print("Error could not perform dynamic analysis on the binary file.")

    def __executej(self, command):
        if self.analyzer is not None:
            return self.analyzer.cmdj(command)

    def __execute(self, command):
        if self.analyzer is not None:
            self.analyzer.cmd(command)

    def breakpoints(self):
        bpSet = []
        # self.__execute("e dbg.bpinmaps=0")
        mainLocation = self.__executej("iMj")
        self.__execute(f"s {hex(mainLocation['vaddr'])}")
        results = self.__executej("isj")
        for i in range(len(results)):
            address = hex(results[i]['vaddr'])
            if address != hex(0) and address not in bpSet:
                bpSet.append(address)
                print(f"db {address}")
                self.__execute(f"db {address}")
        # print(self.__executej("dbj"))
        # self.runDynamic()
        # print(self.__executej("afvrj"))

    def runDynamic(self):

        # self.getPID()
        # current_instruction = []
        while True:
            self.__execute("dc")
            # self.PrintTerminal()
            # self.getRegisters()
            # self.__execute("ds")
            current_instruction = self.__executej("pdj 1")
            print(current_instruction)
            # for i in range(len(current_instruction)):
            #     temp = current_instruction[i]['opcode']
            #     print(temp)
            # if current_instruction['type'] == 'ret':
            #     print("ddr~{}")
            #     break
            # break
            print("______________")





    def getRegisters(self):
        temp = self.__executej("drrj")
        for i in range(len(temp)):
            # print(temp[i]['reg'])
            # print(temp[i]['value'])
            reg = str(temp[i]['reg'])
            self.registers[reg] = temp[i]['value']
        print(self.registers)

    def getPID(self):
        # print("getting PID")
        self.__execute("doo > temp.txt")
        file = open("temp.txt", "r+")
        pid=file.read().replace('\n', '')
        file.truncate(0)
        print("Proccess with PID ",pid,"started...")

    def __exitAnalysis(self):
        # Exit Binary Dynamic Analysis
        # self.analyzer.cmd("exit")
        self.analyzer.quit()
        print("Exited Dynamic Analysis.")

    # def PrintTerminal(self):
        # print(self.getTerminalText())

    # def getTerminalText(self):
    #     file = open("temp.txt", "r+")
    #     text = file.read()
    #     file.truncate(0)
    #     return str(text)

if __name__ == "__main__":
    a = DynamicAnalysis()
    a.setPath('..//..//res%sex.o' % os.sep)
    a.breakpoints()
    a.runDynamic()

