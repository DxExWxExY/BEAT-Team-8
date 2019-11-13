class PoiItem:
    def __init__(self, type, data=None):
        if data is None:
            self.data = {}
            self.data['type'] = type
        else:
            self.data = data