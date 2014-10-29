import dns.resolver, string
from dns.resolver import NoAnswer, NXDOMAIN, Timeout
from sleekxmpp import ClientXMPP

from srv_lookup import performSRVLookup

#util_dependencies
from domain_name_lookup import testFunction as domainNameLookup


def testFunction(domain_url):

	return performSRVLookup(domain_url, "_xmpp-server._tcp.", "XMPP server SRV record", "5269")
