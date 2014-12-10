from requests import Request, Session, ConnectionError

#util_dependencies
from ssl_adapter import SSLAdapter

#installation_suite_dependencies
from api_server_lookup import testFunction as apiLookup


def testFunction(domain_url):

	status, briefing, message, api_TXT_record = apiLookup(domain_url)
	if ( status != 0 ):
		status = 2
		briefing = "This test was skipped because previous test "
		briefing += "<strong>api_server_lookup</strong> has failed.<br/>"
		new_message = briefing
		new_message += "Reason:<br/>"
		new_message += "<br/>" + message
		return (status, briefing, new_message, None)

	try:
		req = Request('HEAD', "%(protocol)s://%(domain)s:%(port)s%(path)s/scripts/buddycloud.js" %api_TXT_record)
		r = req.prepare()

		s = Session()
		s.mount('https://', SSLAdapter('TLSv1'))

		if ( (s.send(r, verify=False, timeout=1)).ok ):
		
			status = 0
			briefing = "Websocket interface for realtime connections available at: <a href=\"%(protocol)s://%(domain)s:%(port)s%(path)s/scripts/buddycloud.js\" target=\"_blank\"><strong>%(protocol)s://%(domain)s:%(port)s%(path)s/scripts/buddycloud.js</strong></a>"%api_TXT_record
			message = briefing
			return (status, briefing, message, None)

		else:

			raise ConnectionError()

	except ConnectionError as e:
	
		status = 1

		error = "Could not retrieve the websocket interface for realtime connections, which should be located at <strong>%(domain)s:%(port)s%(path)s/scripts/buddycloud.js</strong>!" % api_TXT_record
		briefing = error
		message = briefing

		if str(e) != "":
			message += "<br/>Reason: %s" % str(e)

		return (status, briefing, message, None)


	except Exception as e:

		status = 2
		briefing = "Something odd happened while trying to retrieve the websocket interface for realtime connections, which should be located at "
		briefing += "<strong>%(domain)s:%(port)s%(path)s/scripts/buddycloud.js</strong>!" % api_TXT_record
		message = briefing
		message += "<br/>This is the exception we got: {%s}" % str(e)
		message += "<br/>It is probably a temporary issue with domain " + domain_url + "."
		message += "<br/>But it could also be a bug in our Inspector."
		message += " Let us know at <a href='https://github.com/buddycloud/buddycloud-tests-framework/issues'>our issue tracker</a> if you think so." 
		return (status, briefing, message, None)
