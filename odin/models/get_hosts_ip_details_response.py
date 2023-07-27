class GetHostsIpDetailsResponse:
    def __init__(self, data):
        self.success = None
        self.data = Data()

        self.message = data.get('message')
        self.success = data.get('success')
        self.data.populate_from_data(data.get('data', {}))


class Data:
    def __init__(self):
        self.asn = ASN()
        self.asn_updated_at = None
        self.domains = None
        self.hostnames = []
        self.ip = None
        self.is_ipv4 = None
        self.is_ipv6 = None
        self.last_updated_at = None
        self.location = Location()
        self.location_updated_at = None
        self.scan_id = None
        self.services = []
        self.services_hash = None
        self.tags = []
        self.whois = Whois()
        self.whois_updated_at = None

    def populate_from_data(self, data):
        self.asn.populate_from_data(data.get('asn', {}))
        self.asn_updated_at = data.get('asn_updated_at')
        self.domains = data.get('domains')
        self.hostnames = [Hostname().populate_from_data(hostname) for hostname in data.get('hostnames', [])]
        self.ip = data.get('ip')
        self.is_ipv4 = data.get('is_ipv4')
        self.is_ipv6 = data.get('is_ipv6')
        self.last_updated_at = data.get('last_updated_at')
        self.location.populate_from_data(data.get('location', {}))
        self.location_updated_at = data.get('location_updated_at')
        self.scan_id = data.get('scan_id')
        self.services = [Service().populate_from_data(service) for service in data.get('services', [])]
        self.services_hash = data.get('services_hash')
        self.tags = [Tag().populate_from_data(tag) for tag in data.get('tags', [])]
        self.whois.populate_from_data(data.get('whois', {}))
        self.whois_updated_at = data.get('whois_updated_at')

        return self


class ASN:
    def __init__(self):
        self.country_code = None
        self.number = None
        self.organization = None

    def populate_from_data(self, data):
        self.country_code = data.get('country_code')
        self.number = data.get('number')
        self.organization = data.get('organization')

        return self


class Hostname:
    def __init__(self):
        self.last_updated_at = None
        self.name = None

    def populate_from_data(self, data):
        self.last_updated_at = data.get('last_updated_at')
        self.name = data.get('name')

        return self


class Location:
    def __init__(self):
        self.city = None
        self.continent = None
        self.coordinates = Coordinates()
        self.country_code = None
        self.country_name = None
        self.geo_point = None
        self.locale_code = None
        self.network = None
        self.postal_code = None

    def populate_from_data(self, data):
        self.city = data.get('city')
        self.continent = data.get('continent')
        self.coordinates.populate_from_data(data.get('coordinates', {}))
        self.country_code = data.get('country_code')
        self.country_name = data.get('country_name')
        self.geo_point = data.get('geo_point')
        self.locale_code = data.get('locale_code')
        self.network = data.get('network')
        self.postal_code = data.get('postal_code')

        return self


class Coordinates:
    def __init__(self):
        self.latitude = None
        self.longitude = None

    def populate_from_data(self, data):
        self.latitude = data.get('latitude')
        self.longitude = data.get('longitude')

        return self


class Service:
    def __init__(self):
        self._meta = Meta()
        self.extra_info = None
        self.last_updated_at = None
        self.modules = Modules()
        self.name = None
        self.port = None
        self.product = None
        self.protocol = None
        self.softwares = []
        self.tunnel = None
        self.version = None
        self.cve = []

    def populate_from_data(self, data):
        self._meta.populate_from_data(data.get('_meta', {}))
        self.extra_info = data.get('extra_info')
        self.last_updated_at = data.get('last_updated_at')
        self.modules.populate_from_data(data.get('modules', {}))
        self.name = data.get('name')
        self.port = data.get('port')
        self.product = data.get('product')
        self.protocol = data.get('protocol')
        self.softwares = data.get('softwares', [])
        self.tunnel = data.get('tunnel')
        self.version = data.get('version')
        self.cve = [CVE(cve_item['id'], cve_item['severity']) for cve_item in data.get('cve', [])]

        return self

class CVE:
    def __init__(self, cve_id, severity):
        self.id = cve_id
        self.severity = severity

class Meta:
    def __init__(self):
        self.category = None
        self.desc = None
        self.name = None
        self.tags = None

    def populate_from_data(self, data):
        self.category = data.get('category')
        self.desc = data.get('desc')
        self.name = data.get('name')
        self.tags = data.get('tags')

        return self


class Modules:
    def __init__(self):
        self.oracle = Oracle()

    def populate_from_data(self, data):
        self.oracle.populate_from_data(data.get('oracle', {}))

        return self


class Oracle:
    def __init__(self):
        self.accept_version = None
        self.connect_flags0 = {}
        self.connect_flags1 = {}
        self.did_resend = None
        self.global_service_options = {}
        self.nsn_service_versions = {}

    def populate_from_data(self, data):
        self.accept_version = data.get('accept_version')
        self.connect_flags0 = data.get('connect_flags0', {})
        self.connect_flags1 = data.get('connect_flags1', {})
        self.did_resend = data.get('did_resend')
        self.global_service_options = data.get('global_service_options', {})
        self.nsn_service_versions = data.get('nsn_service_versions', {})

        return self


class Tag:
    def __init__(self):
        self.last_updated_at = None
        self.name = None
        self.pretty_name = None
        self.value = None

    def populate_from_data(self, data):
        self.last_updated_at = data.get('last_updated_at')
        self.name = data.get('name')
        self.pretty_name = data.get('pretty_name')
        self.value = data.get('value')

        return self


class Whois:
    def __init__(self):
        self._encoding = Encoding()
        self.descr = None
        self.network = None
        self.organization = None
        self.raw = None

    def populate_from_data(self, data):
        self._encoding.populate_from_data(data.get('_encoding', {}))
        self.descr = data.get('descr')
        self.network = data.get('network')
        self.organization = data.get('organization')
        self.raw = data.get('raw')

        return self


class Encoding:
    def __init__(self):
        self.raw = None

    def populate_from_data(self, data):
        self.raw = data.get('raw')

        return self
