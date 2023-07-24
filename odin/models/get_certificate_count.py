class GetCertificatesCountResponse:
    def __init__(self, data):
        # self.success = None
        self.data = Data()

        self.success = data.get('success')
        self.message = data.get('message')
        self.data.populate_from_data(data.get('data', {}))


class Data:
    def __init__(self):
        self.count = None

    def populate_from_data(self, data):
        self.count = data.get('count')

        return self
