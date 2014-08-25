buddycloud-tests-framework
===========================

[![Build Status](http://travis-ci.org/buddycloud/buddycloud-tests-framework.svg?branch=master)](http://travis-ci.org/buddycloud/buddycloud-tests-framework)

*A framework for issuing tests to a given Buddycloud*


This project is all about testing Buddycloud technology,
as well as helping one check if a given Buddycloud installation
is correctly setup and able to federate with the world.

A test version is currently being deployed at http://protocol.buddycloud.com!

Want to help? It's pretty easy!

Adding a new test to a test suite
----------------------------------

First things, first. There are two test suites, each having different roles.

The ```installation``` test suite is composed of a series of tests to make sure a given Buddycloud installation
is correctly setup. Otherwise, it won't be able to federate and socialize with others. DNS lookups, XMPP communication checks and other
things like that are done to ensure the installation process was successful.

The ```integration``` test suite is composed, as the name suggests, of integration tests for the Buddycloud technology.
These tests are necessary because they will exercise your Buddycloud installation enough
 so we can be safe that your Buddycloud will be able to federate and socialize with others.


Here's how you can add a new test to one of these suites. First, determine to which suite the new test is going to be added.

<dl><dt>Determine which test suite you want to contribute to</dl></dt>

> You can pick either the ```installation``` or the ```integration``` suite.
> Please bear in mind the purposes of each test suite before adding a new test.

<dl><dt>Create a new test file</dl></dt>

> Write a python test file (e.g named ```example.py```) containing a function called ```testFunction```.  
> 
> As of now, this ```testFuncion``` must have the first parameter corresponding to the domain to be tested
and an optional session parameter which some tests populate so that, say, channels created by one test can
be referenced in another test. This is a not-so-good design.
Later we plan to make every test actually execute its dependency tests all over again in a setUp/tearDown fashion -- no relying
on collateral effects of previous tests.

> Also, future versions may allow a more flexible approach for the parameter passing to ```testFunction```.
>
> Make sure your ```testFunction``` always returns a tuple with four elements in the following format:
>
> ```(exit_status, briefing, message, output)``` where:
>
> * ```exit_status type:int```
>	should be equal to ```0``` if test was successful or any other integer otherwise,
>
> * ```briefing type:str```
>	should be a brief explanation of what happened during the test,
>
> * ```message type:str```
>	should be a longer message with more information and
>
> * ```output type:anything```
>	should be anything your test could output if you want this test's results to be reused by other tests,
>	otherwise just return ```None```
>
> *Important:*
>
> *1.* Your test runs within an execution_context folder with read/write permissions. Anything your test writes will be placed there (e.g. logs).
>
> *2.* Your test can import any library that is installed in the server. If you need some other library to be installed, let us know.
>
> *3.* Your test can import other ```testFuncion```s defined in other existing tests belonging to **BOTH** test suites as well!
> That means that even while tests are split into different test suites, they can be imported just as if they all belonged to the same suite.
>
> Here's an example of a test that reuses the test defined at ```api_lookup.py```:
>
    from api_server_lookup import testFunction as apiLookup 
    def testFunction(domain_url):
	    (exit_status, briefing, message, output) = apiLookup(domain_url)
>
> *4.* There is a ```suite_utils``` folder including utilitary files both test suites can reuse.

<dl><dt>Declare that your test should be run as part of the test suite</dl></dt>

> Append a new line to the ```installation/installation_tests.cfg``` configuration file containing only the name
> of your new test file.
>
> *Important:*
>
> *1.* You can always prepend a hashtag to a line of the configuration file to make sure the test suite won't include that particular test.


So, that's all, folks!
--------------

Please send pull requests with new tests.
