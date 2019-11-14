import base64

import r2pipe


class StaticAnalyzer:
    pass

    def setPath(self, path):
        try:
            self.analyzer = r2pipe.open(path)
            self.analyzer.cmd("aaaa")
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

    def __funcAddr(self, addr):
        self.__execute(f"s {addr}")
        calls = self.__executej("afij")
        if not calls:
            return []
        if 'callrefs' not in calls[0].keys():
            return []
        calls = calls[0]['callrefs']
        addresses = [hex(e['addr']) for e in calls]
        for address in addresses:
            addresses += self.__funcAddr(address)
        return addresses

    def findPois(self, filterType):
        poiList = []
        if filterType == "function":
            mainAddr = hex(self.__executej("iMj")['vaddr'])
            addresses = [mainAddr] + self.__funcAddr(mainAddr)
            for address in addresses:
                poi = {}
                self.__execute(f"s {address}")
                info = self.__executej("afij")[0]
                poi['type'] = 'Function'
                poi['name'] = info['name']
                if info['nargs'] != 0:
                    args = self.__executej("afvj")['reg']
                    poi['args'] = [(a['name'], a['type']) for a in args]
                else:
                    poi['args'] = []
                poiList.append(poi)
            return poiList
            # list = self.__executej("isj")
            # for i in range(len(list)):
            #     if (list[i]['type']) == "FUNC" and list[i]['demname']:
            #         item = {}
            #         item['type'] = 'Function'
            #         item['name'] = str(list[i]['demname'])
            #         item['addr'] = hex(list[i]['vaddr'])
            #         self.__execute(f"s {hex(list[i]['vaddr'])}")
            #         results = self.__executej("afvj")
            #         temp = []
            #         for j in range(len(results['reg'])):
            #             temp.append(results['reg'][j]['name'])
            #             temp.append(results['reg'][j]['type'])
            #         item['args'] = temp
            #         poiList.append(item)
            # return poiList

        strs = self.__executej("iij")
        if (filterType == "dll"):
            for i in range(len(strs)):
                item = {}
                item['type'] = 'DLL'
                item['name'] = (strs[i]['name'])
                poiList.append(item)
            return poiList

        if (filterType == "strings"):
            strs = self.__executej("izj")
            for i in range(len(strs)):
                item = {}
                item['type'] = 'String'
                item['value'] = base64.b64decode(str(strs[i]['string'])).decode()
                item['addr'] = hex(strs[i]['vaddr'])
                poiList.append(item)
            return poiList

        if filterType == "variable":
            mainAddr = hex(self.__executej("iMj")['vaddr'])
            addresses = [mainAddr] + self.__funcAddr(mainAddr)
            for address in addresses:
                poi = {}
                self.__execute(f"s {address}")
                info = self.__executej("afvj")['bp']
                poi['type'] = 'Variable'
                poi['dtype'] = info['type']
                poiList.append(poi)
            return poiList
        # TODO add variables, structs, packet protocol

    def close(self):
        self.__execute("exit")
        self.analyzer = None
