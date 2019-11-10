from jinja2 import Template

class OutputGenerator:
    def __init__(self) :
        fileWriter = open()
    # Werer assiming that the point of innterest will have its python quivalent as a string tied to it
    def fillInTemplate(self, type, data):
        pass

    def __generateFunction(self, data):
        scapeString = data.functionAsString # sys.fork({{ key1 }}) 1
        template = Template(scapeString)
        for k in data.parameters.keys():
            template.render(k=data.parameters[k])
        script = template.generate()
        return script