import string
from api_utils import topic_channel_exists, create_topic_channel, delete_topic_channel
from find_api_location import findAPILocation


def testFunction(domain_url):

	(status, briefing, message, api_location) = findAPILocation(domain_url)
	if status != 0:
		return (status, briefing, message, None)

	test_topic_channel_name = "test_topic_channel_open"
	test_topic_channel_owner_username = "test_user_channel_open"

	if delete_topic_channel(domain_url, api_location, test_topic_channel_owner_username, test_topic_channel_name):
	
		status = 0
		briefing = "Could successfully remove test topic channel: <strong>%s@topics.%s</strong>" % (test_topic_channel_name, domain_url)
		message = "We could successfully assert deletion of test topic channel <strong>%s@topics.%s</strong>." % (test_topic_channel_name, domain_url)
		message += "<br/>That test topic channel was being used for testing purposes."

		return (status, briefing, message, None)

	else:

		if not topic_channel_exists(domain_url, api_location, test_topic_channel_name):

			status = 2
			briefing = "The test topic channel <strong>%s@topics.%s</strong> was " % (test_topic_channel_name, domain_url)
			briefing += "expected to exist but it didn't, so it could not be deleted."
			message = briefing

			if ( create_user_channel(domain_url, api_location, test_topic_channel_owner_username, test_topic_channel_name)
			and delete_user_channel(domain_url, api_location, test_topic_channel_owner_username, test_topic_channel_name) ):

				status = 0
				additional_info = "<br/>But we could assert that topic channel deletion is being properly implemented by your API server."
				briefing += additional_info
				message += additional_info
				message += "<br/>We created another test topic channel and then were successful in deleting it."
			else:
				message += "<br/>The problem is we cannot assert that topic channel deletion is working."

			return (status, briefing, message, None)

		else:

			status = 1
			briefing = "The test topic channel <strong>%s@topics.%s</strong> could not be deleted." % (test_topic_channel_name, domain_url)
			message = briefing
			message += "<br/>It seems like your HTTP API server is problematic. It had trouble deleting a topic channel - that operation must work."
			
			return (status, briefing, message, None)