import sys
import traceback

import r2pipe


class StaticAnalyzer:
    pass

    def setPath(self, path):
        try:
            self.analyzer = r2pipe.open(path,flags=['-d'])
            self.analyzer.cmd("aaaa")
            self.analyzer.cmd("doo")
            self.base = int(self.__executej("ej")['bin.baddr'])
        except:
            self.analyzer = None

    def getBinaryProperties(self):
        if self.analyzer is not None:
            properties = dict()
            BinInfo = self.__executej("ij")
            properties['os'] = BinInfo["bin"]["os"]
            properties['arch'] = BinInfo["bin"]["arch"]
            properties['machine'] = BinInfo["bin"]["machine"]
            properties['class'] = BinInfo["core"]["format"]
            properties['bits'] = str(BinInfo["bin"]["bits"])
            properties['lang'] = BinInfo["bin"]["lang"]
            properties['canary'] = str(BinInfo["bin"]["canary"])
            properties['crypto'] = str(BinInfo["bin"]["crypto"])
            properties['nx'] = str(BinInfo["bin"]["nx"])
            properties['pic'] = str(BinInfo["bin"]["pic"])
            properties['relocs'] = str(BinInfo["bin"]["relocs"])
            properties['relro'] = str(BinInfo["bin"]["relro"])
            properties['stripped'] = str(BinInfo["bin"]["stripped"])
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

    def __getFunctions(self):
        poiList = {}
        data = self.__executej("aflj")
        for i in range(len(data)):
            poi = {}
            poi['type'] = 'Function'
            poi['name'] = (str(data[i]['name']))
            if 'sym.imp.' in poi['name']:
                self.__execute(f"s {int(data[i]['offset'])}")
                try:
                    calls = self.__executej("afij")[0]["codexrefs"]
                    for call in calls:
                        if call['type'] == 'CALL':
                            poi['addr'] = int(call['addr'] - self.base)
                except KeyError:
                    poi['addr'] = 0
            else:
                poi['addr'] = int(data[i]['offset'] - self.base)
            self.__execute(f"s {self.base + poi['addr']}")
            info = self.__executej("afij")
            if info:
                try:
                    if info[0]['nargs'] != 0:
                        args = self.__executej("afvj")['reg']
                        poi['args'] = [(a['name'], a['type'], a['ref']) for a in args]
                    else:
                        poi['args'] = []
                except:
                    traceback.print_exc(file=sys.stdout)
                    traceback.print_exc(limit=1, file=sys.stdout)
            else:
                poi['args'] = []
            poiList[poi['name']] = poi
        return poiList

    def findPois(self, filterType):
        poiList = {}
        if filterType == "function":
            return self.__getFunctions()

        if (filterType == "dll"):
            imports = self.__executej("iij")
            for i in range(len(imports)):
                item = {}
                item['type'] = 'DLL'
                item['name'] = (imports[i]['name'])
                poiList[item['name']] = item
            return poiList

        if (filterType == "strings"):
            strings = self.__executej("izj")
            for i in range(len(strings)):
                item = {}
                item['type'] = 'String'
                item['name'] = strings[i]['string']
                item['addr'] = hex(strings[i]['vaddr'])
                poiList[item['name']] = item
            return poiList

        if filterType == "variable":
        #     mainAddr = hex(self.__executej("iMj")['vaddr'])
        #     addresses = [mainAddr] + self.__funcAddr(mainAddr)
        #     for address in addresses:
        #         self.__execute(f"s {address}")
        #         name = self.__executej("afij")[0]['name']
        #         info = self.__executej("afvj")['bp']
        #         for i in info:
        #             poi = {}
        #             poi['type'] = 'Variable'
        #             poi['name'] = f"{name}.var{abs(int(i['ref']['offset']))}"
        #             poi['dtype'] = i['type']
        #             poiList[poi['name']] = name
            return poiList
        # TODO add variables, structs, packet protocol

    def close(self):
        self.analyzer.quit()
        self.analyzer = None
