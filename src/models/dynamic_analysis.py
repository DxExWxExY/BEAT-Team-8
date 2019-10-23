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
            #Continue Program Execution
            self.analyzer.cmd("dc")
            # Print Binary Information into the BEAT Prompt
           return self.analyzer.cmd("i1j")

    def exitAnalysis (self, command):
        # Exit Binary Dynamic Analysis
        #self.analyzer.cmd("exit")
        self.analyzer.quit()
        print("Exited Dynamic Analysis.")


