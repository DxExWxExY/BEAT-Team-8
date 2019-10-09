import r2pipe

class StaticAnalyzer:
    pass

    def setPath(self, path):
        try:
            self.analyzer = r2pipe.open(path)
            self.analyzer.cmd("aaa")
            self.analyzer.cmd("doo")
        except:
            self.analyzer = None

    def getBinaryProperties(self):
        if self.analyzer is not None:
            properties = dict()
            BinInfo = self.__executej("ij")
            properties['file'] = BinInfo["core"]["file"]
            properties['os'] = BinInfo["bin"]["os"]
            properties['arch'] = BinInfo["bin"]["arch"]
            properties['machine'] = BinInfo["bin"]["machine"]
            properties['bits'] = BinInfo["bin"]["bits"]
            properties['canary'] = BinInfo["bin"]["canary"]
            properties['crypto'] = BinInfo["bin"]["crypto"]
            properties['nx'] = BinInfo["bin"]["nx"]
            properties['pic'] = BinInfo["bin"]["pic"]
            properties['relocs'] = BinInfo["bin"]["relocs"]
            properties['stripped'] = BinInfo["bin"]["stripped"]
            properties['endian'] = BinInfo["bin"]["endian"]
            properties['format'] = BinInfo["core"]["format"]
            return properties

    def __execute(self, command):
        if self.analyzer is not None:
            self.analyzer.cmd(command)

    def __executej(self, command):
        if self.analyzer is not None:
            return self.analyzer.cmdj(command)

    def getPois(self, plugin, type):
        if self.analyzer is not None:
            json = self.__executej("ij")
            results = []
            filter = plugin.listFilter(type)
            for e in json:
                if e in filter:
                    results.append(e)
            return results