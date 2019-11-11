from jinja2 import Template
import re
class OutputGenerator:
    global file

    def __init__(self):
        pass

    # function for user to enter their own lines of code.
    def createForm(self):
        pass

    def createFile(self, name, fileType):
        fileName = name + fileType
        self.file = open(fileName, "w")

    # write to output file
    def __writeToFile(self, data):
        self.file.write(data)

    #Werer assiming that the point of innterest will have its python quivalent as a string tied to it
    def fillInTemplate(self, type, data):
        pass

    # enter function name ONLY, dictionary of data(?)
    # key = flag, value = string
    # scenarios of function body:
    #   1. data initialization
    #   2. return 'value' (?)
    #   3. other function calls
    # parameter 'data':
    #   data[0] = function name
    #   data[1] = function return value
    #   data[2] = function parameters
    def generateFunction(self, data):
        func_name = data[0]
        func_ret = data[1]
        try:
            func_para = data[2]
        except IndexError:
            func_para = ""
        tm = Template("def {{func_name}}({{func_para}}): \n   {{func_ret}}\n")
        line = tm.render(func_name=func_name,func_body=func_ret, func_para=func_para)
        self.__writeToFile(line)

    # generate strings, structs, variables.
    # must provide type, name, and value of variable to create.
    def generateVars(self, type, name, value):
        tm = Template("{{type}} {{name}} = {{value}}\n")
        line = tm.render(type=type, name=name, value=value)
        self.__writeToFile(line)

outputGen = OutputGenerator()
list = ["printMethod","printf(\"hello world\")"]
outputGen.generateFunction(list)