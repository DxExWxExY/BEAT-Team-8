import r2pipe

class DynamicAnalysis:
    pass

    def setPath(self, path):
        try:
            #Open the binary file
            self.analyzer = r2pipe.open(path)
            # Analyze the binary
            self.analyzer.cmd("aaa")
            # Enter debugger mode
            self.analyzer.cmd("doo")
            #Ready for Binary Analysis
            if self.analyzer.info().stripped:
                print("The Binary is ready for dynamic analysis")
        except:
            self.analyzer = None
            print("Error could not perform dynamic analysis on the binary file.")

    def __dynamicAnalysis(self, command):
        if self.analyzer is not None:
            #Execute Dynamic Analysis
            self.analyzer.cmdj(command)

    def __Breakpoints(self)
        # Print Binary Information into the BEAT Prompt
        binaryInfo = self.__dynamicAnalysis("i1j")
        #Find references on binary
        findReferences = self.__dynamicAnalysis("axtj")

         for i in range(len(findReferences)):
            # Add breakpoint
            breakPoint = self.__dynamicAnalysis("db")  + hex(findReferences[i]["from"])
            #Add breakpoint at desired location
            run = self.__dynamicAnalysis(breakpoint)

        while True:
            #Run until breakpoint is checked
            run = self.__dynamicAnalysis("dc")
            #Execute on breakpoint reference call
            execute = self.__dynamicAnalysis("dso")
        if self.analyzer is not None:
            # Continue Program Execution Until Breakpoint
            self.__dynamicAnalysis("dc")

    def __exitAnalysis (self):
        # Exit Binary Dynamic Analysis
        #self.analyzer.cmd("exit")
        self.analyzer.quit()
        print("Exited Dynamic Analysis.")

    #TODO Modify Dynamic Analysis & Breakpoints
