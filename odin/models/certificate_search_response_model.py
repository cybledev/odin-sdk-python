class CertificateSearchResponse:
    def __init__(self, data = None):
        self.success = None
        self.message = None
        self.pagination = Pagination()
        self.data = []
        if data is not None:
            self.fill_data( data)
            
    def fill_data(self,data):
        self.success = data.get('success')
        self.message = data.get('message')
        self.pagination.populate_from_data(data.get('pagination', {}))
        self.data = [Certificate().populate_from_data(cert) for cert in data.get('data', [])]


class Pagination:
    def __init__(self):
        self.start = None
        self.last = None
        self.limit = None
        self.total = None

    def populate_from_data(self, data):
        self.start = data.get('start')
        self.last = data.get('last')
        self.limit = data.get('limit')
        self.total = data.get('total')

        return self


class Certificate:
    def __init__(self):
        self.fingerprint_md5 = None
        self.fingerprint_sha1 = None
        self.fingerprint_sha256 = None
        self.issuer = Issuer()
        self.subject = Subject()
        self.subject_alt_name = SubjectAltName()
        self.tags = []
        self.validity = Validity()

    def populate_from_data(self, data):
        self.fingerprint_md5 = data.get('fingerprint_md5')
        self.fingerprint_sha1 = data.get('fingerprint_sha1')
        self.fingerprint_sha256 = data.get('fingerprint_sha256')
        self.issuer.populate_from_data(data.get('issuer', {}))
        self.subject.populate_from_data(data.get('subject', {}))
        self.subject_alt_name.populate_from_data(data.get('subject_alt_name', {}))
        self.tags = data.get('tags', [])
        self.validity.populate_from_data(data.get('validity', {}))

        return self


class Issuer:
    def __init__(self):
        self.common_name = []
        self.country = []
        self.organization = []

    def populate_from_data(self, data):
        self.common_name = data.get('common_name', [])
        self.country = data.get('country', [])
        self.organization = data.get('organization', [])

        return self


class Subject:
    def __init__(self):
        self.common_name = []

    def populate_from_data(self, data):
        self.common_name = data.get('common_name', [])

        return self


class SubjectAltName:
    def __init__(self):
        self.dns_names = []

    def populate_from_data(self, data):
        self.dns_names = data.get('dns_names', [])

        return self


class Validity:
    def __init__(self):
        self.end = None
        self.length = None
        self.start = None

    def populate_from_data(self, data):
        self.end = data.get('end')
        self.length = data.get('length')
        self.start = data.get('start')

        return self
