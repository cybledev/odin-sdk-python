class GetCertificatesSummaryResponse:
    def __init__(self, data):
        self.success = None
        self.data = SearchData()

        self.success = data.get('success')
        self.message = data.get('message')
        self.data.populate_from_data(data.get('data', {}))


class SearchData:
    def __init__(self):
        self.doc_count_error_upper_bound = None
        self.sum_other_doc_count = None
        self.buckets = []

    def populate_from_data(self, data):
        self.doc_count_error_upper_bound = data.get('doc_count_error_upper_bound')
        self.sum_other_doc_count = data.get('sum_other_doc_count')
        self.buckets = [Bucket().populate_from_data(bucket) for bucket in data.get('buckets', [])]


class Bucket:
    def __init__(self):
        self.doc_count = None
        self.key = None

    def populate_from_data(self, data):
        self.doc_count = data.get('doc_count')
        self.key = data.get('key')
        return self
