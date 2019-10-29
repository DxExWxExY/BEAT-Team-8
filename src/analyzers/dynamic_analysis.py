import os

import r2pipe


class DynamicAnalysis:
    pass

    def setPath(self, path):
        try:
            self.analyzer = r2pipe.open(path)
            self.analyzer.cmd("aaa")
            self.analyzer.cmd("doo")
            if self.analyzer.info().stripped:
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

    def __breakpoints(self):
        # Print Binary Information into the BEAT Prompt
        binaryInfo = self.__executej("i1j")
        # Find references on binary
        findReferences = self.__executej("axtj")

        for i in range(len(findReferences)):
            # Add breakpoint
            breakPoint = self.__executej("db") + hex(findReferences[i]["from"])
            # Add breakpoint at desired location
            run = self.__executej(breakpoint)

        while True:
            # Run until breakpoint is checked
            run = self.__executej("dc")
            # Execute on breakpoint reference call
            execute = self.__executej("dso")

        if self.analyzer is not None:
            # Continue Program Execution Until Breakpoint
            self.__executej("dc")


    def __exitAnalysis(self):
        # Exit Binary Dynamic Analysis
        # self.analyzer.cmd("exit")
        self.analyzer.quit()
        print("Exited Dynamic Analysis.")

if __name__ == "__main__":
    a = DynamicAnalysis()
    a.setPath('res%sex.o' % os.sep)
