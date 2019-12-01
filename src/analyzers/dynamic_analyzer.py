import os
import time
from threading import Thread

import r2pipe


class DynamicAnalyzer:
    pass

    def setPath(self, path):
        try:
            self.analyzer = r2pipe.open(path)
            self.analyzer.cmd("aaa")
            # self.analyzer.cmd("e dbg.profile=r2.rr2")
            self.analyzer.cmd("doo")
            self.base = int(self.__executej("ej")['bin.baddr'])
            self.message = "Test"
            self.stopFlag = False
        except:
            self.analyzer = None

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
        self.__execute("ood")
        while True:
            self.__execute("dc")
            # file = open("pipe.txt", "r+")
            # print(file.read())
            # # file.truncate(0)
            var = self.__executej("sj")
            print(hex(var[0]['offset']), end="\n")
            print(self.__executej(f"axtj {hex(var[0]['offset'])}"))
            time.sleep(1)
        pass
        # self.__execute("doo")
        # while True:
        #     self.__execute("dc")
        #     print("running dynamic...")
        #
        #     # self.__execute("q")
        #     # self.__execute("ood")
        #
        #     self.__execute("s")
        #     var = self.__executej("sj")
        #     print(hex(var[0]['offset']), end="\n")
        #     print(self.__executej(f"axtj {hex(var[0]['offset'])}"))
        #     time.sleep(1)
        #
        # pass

        # # Print Binary Information into the BEAT Prompt
        # binaryInfo = self.__executej("i1j")
        # # Find references on binary
        # findReferences = self.__executej("axtj")
        #
        # for i in range(len(findReferences)):
        #     # Add breakpoint
        #     breakPoint = self.__executej("db") + hex(findReferences[i]["from"])
        #     # Add breakpoint at desired location
        #     run = self.__executej(breakpoint)
        #
        # while True:
        #     # Run until breakpoint is checked
        #     run = self.__executej("dc")
        #     # Execute on breakpoint reference call
        #     execute = self.__executej("dso")
        #
        # if self.analyzer is not None:
        #     self.__executej("dc")

    def __exitAnalysis(self):
        self.analyzer.quit()
        print("Exited Dynamic Analysis.")

    def setBreakpoint(self, address):
        actualAddr = hex(address + self.base)
        print(actualAddr)
        self.__execute(f"db {actualAddr}")

    def start(self, pois):
        Thread(target=self.__start, args=[pois]).start()

    def __start(self, pois):
        bpCount = 0
        while bpCount < len(pois):
            self.__execute("dc")
            temp = self.__executej("drj")
            currentAddr = hex(int(temp['rip']))
            for poi in pois:
                actualAddr = hex(poi['addr'] + self.base)
                if  actualAddr == currentAddr:
                    regs = self.__getRegisters()
                    poi['pval'] = []
                    for arg in poi['args']:
                        r = arg[2]
                        poi['pval'].append(regs[r])
                    self.__execute("dcr")
                    regs = self.__getRegisters()
                    poi['rval'] = regs['rax']
                    bpCount += 1

    def __getRegisters(self):
        registers = {}
        temp = self.__executej("drrj")
        for i in range(len(temp)):
            # print(temp[i]['reg'])
            # print(temp[i]['value'])
            reg = str(temp[i]['reg'])
            registers[reg] = temp[i]['value']
        return registers


if __name__ == "__main__":
    a = DynamicAnalyzer()
    a.setPath('..\\..\\res%sex2' % os.sep)
    a.breakpoints()
    # a.runDynamic()
