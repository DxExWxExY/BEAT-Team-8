import base64
import os, sys
import time

import r2pipe


class DynamicAnalysis:
    pass

    def setPath(self, path):
        try:
            self.analyzer = r2pipe.open(path)
            # self.analyzer.cmd("aaa")
            self.analyzer.cmd("e dbg.profile=r2.rr2")
            self.analyzer.cmd("doo")


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
        self.__execute("e dbg.bpinmaps=0")
        results = self.__executej("isj")
        for i in range(len(results)):
            address = hex(results[i]['vaddr'])
            if address != hex(0) and address not in bpSet:
                bpSet.append(address)
                print(f"db {address}")
                self.__execute(f"db {address}")
        # print(self.__executej("dbj"))
        self.runDynamic()
        # print(self.__executej("afvrj"))


    def runDynamic(self):
        self.__execute("ood > pipe.txt")
        while True:
            self.__execute("dc > pipe.txt")
            file = open("pipe.txt", "r+")
            print(file.read())
            # file.truncate(0)
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
        # Exit Binary Dynamic Analysis
        # self.analyzer.cmd("exit")
        self.analyzer.quit()
        print("Exited Dynamic Analysis.")

if __name__ == "__main__":
    a = DynamicAnalysis()
    a.setPath('..//..//res%sex.o' % os.sep)
    a.runDynamic()
    # a.breakpoints()

