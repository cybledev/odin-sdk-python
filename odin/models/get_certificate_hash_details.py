class GetCertificateHashDetails:
    def __init__(self, data):
        self.success = None
        self.data = CertificateData()

        self.success = data.get('success')
        self.message = data.get('message')
        self.data.populate_from_data(data.get('data', {}))


class CertificateData:
    def __init__(self):
        self.certificate = Certificate()
        self.tags = []

    def populate_from_data(self, data):
        self.certificate.populate_from_data(data.get('certificate', {}))
        self.tags = data.get('tags', [])


class Certificate:
    def __init__(self):
        self.extensions = Extensions()
        self.fingerprint_md5 = None
        self.fingerprint_sha1 = None
        self.fingerprint_sha256 = None
        self.issuer = Issuer()
        self.redacted = None
        self.serial_number = None
        self.signature = Signature()
        self.subject = Subject()
        self.subject_alt_name = SubjectAltName()
        self.subject_key_info = SubjectKeyInfo()
        self.tbs_fingerprint = None
        self.validation_level = None
        self.validity = Validity()
        self.version = None

    def populate_from_data(self, data):
        self.extensions.populate_from_data(data.get('extensions', {}))
        self.fingerprint_md5 = data.get('fingerprint_md5')
        self.fingerprint_sha1 = data.get('fingerprint_sha1')
        self.fingerprint_sha256 = data.get('fingerprint_sha256')
        self.issuer.populate_from_data(data.get('issuer', {}))
        self.redacted = data.get('redacted')
        self.serial_number = data.get('serial_number')
        self.signature.populate_from_data(data.get('signature', {}))
        self.subject.populate_from_data(data.get('subject', {}))
        self.subject_alt_name.populate_from_data(data.get('subject_alt_name', {}))
        self.subject_key_info.populate_from_data(data.get('subject_key_info', {}))
        self.tbs_fingerprint = data.get('tbs_fingerprint')
        self.validation_level = data.get('validation_level')
        self.validity.populate_from_data(data.get('validity', {}))
        self.version = data.get('version')


class Extensions:
    def __init__(self):
        self.authority_info_access = AuthorityInfoAccess()
        self.authority_key_id = None
        self.basic_constraints = BasicConstraints()
        self.certificate_policies = []
        self.ct_poison = None
        self.extended_key_usage = ExtendedKeyUsage()
        self.key_usage = KeyUsage()
        self.subject_alt_name = SubjectAltName()
        self.subject_key_id = None

    def populate_from_data(self, data):
        self.authority_info_access.populate_from_data(data.get('authority_info_access', {}))
        self.authority_key_id = data.get('authority_key_id')
        self.basic_constraints.populate_from_data(data.get('basic_constraints', {}))
        self.certificate_policies = [CertificatePolicy().populate_from_data(policy) for policy in data.get('certificate_policies', [])]
        self.ct_poison = data.get('ct_poison')
        self.extended_key_usage.populate_from_data(data.get('extended_key_usage', {}))
        self.key_usage.populate_from_data(data.get('key_usage', {}))
        self.subject_alt_name.populate_from_data(data.get('subject_alt_name', {}))
        self.subject_key_id = data.get('subject_key_id')


class AuthorityInfoAccess:
    def __init__(self):
        self.issuer_urls = []
        self.ocsp_urls = []

    def populate_from_data(self, data):
        self.issuer_urls = data.get('issuer_urls', [])
        self.ocsp_urls = data.get('ocsp_urls', [])


class BasicConstraints:
    def __init__(self):
        self.is_ca = None

    def populate_from_data(self, data):
        self.is_ca = data.get('is_ca')


class CertificatePolicy:
    def __init__(self):
        self.id = None
        self.cps = []

    def populate_from_data(self, data):
        self.id = data.get('id')
        self.cps = data.get('cps', [])


class ExtendedKeyUsage:
    def __init__(self):
        self.client_auth = None
        self.server_auth = None

    def populate_from_data(self, data):
        self.client_auth = data.get('client_auth')
        self.server_auth = data.get('server_auth')


class KeyUsage:
    def __init__(self):
        self.digital_signature = None

    def populate_from_data(self, data):
        self.digital_signature = data.get('digital_signature')


class SubjectAltName:
    def __init__(self):
        self.dns_names = []
        self.extended_dns_names = []

    def populate_from_data(self, data):
        self.dns_names = data.get('dns_names', [])
        self.extended_dns_names = [ExtendedDNSName().populate_from_data(name) for name in data.get('extended_dns_names', [])]


class ExtendedDNSName:
    def __init__(self):
        self.domain = None
        self.fld = None
        self.subdomain = None
        self.tld = None

    def populate_from_data(self, data):
        self.domain = data.get('domain')
        self.fld = data.get('fld')
        self.subdomain = data.get('subdomain')
        self.tld = data.get('tld')


class Issuer:
    def __init__(self):
        self.common_name = []
        self.country = []
        self.organization = []

    def populate_from_data(self, data):
        self.common_name = data.get('common_name', [])
        self.country = data.get('country', [])
        self.organization = data.get('organization', [])


class Signature:
    def __init__(self):
        self.signature_algorithm = SignatureAlgorithm()

    def populate_from_data(self, data):
        self.signature_algorithm.populate_from_data(data.get('signature_algorithm', {}))


class SignatureAlgorithm:
    def __init__(self):
        self.name = None
        self.oid = None

    def populate_from_data(self, data):
        self.name = data.get('name')
        self.oid = data.get('oid')


class Subject:
    def __init__(self):
        self.common_name = []

    def populate_from_data(self, data):
        self.common_name = data.get('common_name', [])


class SubjectKeyInfo:
    def __init__(self):
        self.fingerprint_sha256 = None
        self.key_algorithm = None
        self.public_key = PublicKey()

    def populate_from_data(self, data):
        self.fingerprint_sha256 = data.get('fingerprint_sha256')
        self.key_algorithm = data.get('key_algorithm')
        self.public_key.populate_from_data(data.get('public_key', {}))


class PublicKey:
    def __init__(self):
        self.b = None
        self.curve = None
        self.gx = None
        self.gy = None
        self.length = None
        self.p = None
        self.x = None
        self.y = None

    def populate_from_data(self, data):
        self.b = data.get('b')
        self.curve = data.get('curve')
        self.gx = data.get('gx')
        self.gy = data.get('gy')
        self.length = data.get('length')
        self.p = data.get('p')
        self.x = data.get('x')
        self.y = data.get('y')


class Validity:
    def __init__(self):
        self.end = None
        self.length = None
        self.start = None

    def populate_from_data(self, data):
        self.end = data.get('end')
        self.length = data.get('length')
        self.start = data.get('start')


