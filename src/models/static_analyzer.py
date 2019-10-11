import base64

import r2pipe

class StaticAnalyzer:
    pass

    def setPath(self, path):
        try:
            self.analyzer = r2pipe.open(path)
            self.analyzer.cmd("aaa")
            # self.analyzer.cmd("doo")
            print("si jalo")
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

    # finds functions,strings,variables, statically
    def R2findPOI(self, filterType):

        POISlist =[]
        if filterType == "function":
            list = self.__executej("isj")
            for i in range(len(list)):
                if(list[i]['type']) == "FUNC":
                    POISlist.append((str(list[i]['name'])))
            # print(POISlist)
            return POISlist

        if(filterType == "dll"):
            strs = self.__executej("iij")  # Grab all imports used by binary ping in json format.
            for i in range(len(strs)):
                obj = strs[i]
                POISlist.append(str(obj['name']))
            return POISlist

        if (filterType == "strings"):
            strs = self.__executej("izj")  # Grab all imports used by binary ping in json format.
            # print(strs)
            for i in range(len(strs)):
                POISlist.append(base64.b64decode(str(strs[i]['string'])).decode())
                # POISlist.append(str(obj['string']))
            print(POISlist)
            return POISlist
