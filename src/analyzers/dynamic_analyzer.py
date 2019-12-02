import os
import struct
import time
from threading import Thread

import r2pipe


class DynamicAnalyzer:
    pass

    def setPath(self, path, args=None):
        try:
            self.analyzer = r2pipe.open(path)
            self.analyzer.cmd("aaa")
            if args is not None:
                self.__execute('doo ' + args)
            else:
                self.analyzer.cmd("doo")
            self.pid = self.__executej("dpaj")
            self.base = int(self.__executej("ej")['bin.baddr'])
        except:
            self.analyzer = None

    def __executej(self, command):
        if self.analyzer is not None:
            return self.analyzer.cmdj(command)

    def __execute(self, command):
        if self.analyzer is not None:
            self.analyzer.cmd(command)

    def close(self, force=False):
        if force:
            os.kill(self.pid)
        self.__execute("exit")
        self.analyzer = None

    def setBreakpoint(self, address):
        actualAddr = hex(address + self.base)
        self.__execute(f"db {actualAddr}")

    def start(self, pois, stopFlag):
        Thread(target=self.__start, args=[pois, stopFlag]).start()

    def __start(self, pois, stopFlag):
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
                        if '*' not in arg[1]:
                            r = arg[2]
                            poi['pval'].append(self.__typeCaster(arg[1], regs[r]))
                    self.__execute("dso")
                    regs = self.__getRegisters()
                    for arg in poi['args']:
                        if '*' in arg[1]:
                            r = arg[2]
                            poi['pval'].append(self.__typeCaster(arg[1], regs[r]))
                    poi['rval'] = regs['rax']
                    bpCount += 1
        stopFlag += [1]


    def __typeCaster(self, type, value):
        if 'char *' in type:
            data = self.__executej(f"pxj @ {value}")
            string = ""
            for i in data:
                string += chr(i)
                if i == 0:
                    break
            return string
        if type in 'int':
            return int(value, 0)
        if type == 'char':
            return chr(int(value, 0))
        if type == 'boolean':
            return struct.unpack('d', value.decode("hex"))

    def __getRegisters(self):
        registers = {}
        temp = self.__executej("drrj")
        for i in range(len(temp)):
            reg = str(temp[i]['reg'])
            registers[reg] = temp[i]['value']
        return registers
