class CVEDetailsResponse:
    def __init__(self, data):
        self.success = None
        self.data = {} 

        self.success = data.get('success')
        self.message = data.get('message')
        if 'data' in data:
            self.populate_cve_details(data.get('data'))

    def populate_cve_details(self, cve_data):
        for cve_id, cve_info in cve_data.items():
            cve = Cve()
            cve.populate_from_data(cve_info)
            self.data[cve_id] = cve


class Cve:
    def __init__(self):
        self.id = None
        self.references = []
        self.score = None
        self.services = []
        self.severity = None
        self.summary = None
        self.vector_string = None
        self.weakness = None

    def populate_from_data(self, data):
        self.id = data.get('id')
        self.references = data.get('references', [])
        self.score = data.get('score')
        self.services = data.get('services', [])
        self.severity = data.get('severity')
        self.summary = data.get('summary')
        self.vector_string = data.get('vector_string')
        self.weakness = data.get('weakness')

        return self
