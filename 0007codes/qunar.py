# coding: utf-8

import urllib
import urllib2

req = urllib2.Request("http://flight.qunar.com")

postdata = urllib.urlencode([
	("searchDepartureAirport", "%E8%BF%90%E5%9F%8E"),
	("searchArrivalAirport", "%E6%9D%AD%E5%B7%9E"),
	("searchDepartureTime", "2016-08-26"),
	("searchArrivalTime", "2016-08-29"),
	("nextNDays", "0"),
	("startSearch", "true"),
	("fromCode", "YCU"),
	("toCode", "HGH"),
	("from", "qunarindex"),
])

req.add_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36")

req.add_header("Referer", "http://www.qunar.com/")

req.add_header("Host", "flight.qunar.com")

response = urllib2.urlopen(req, data=postdata.encode('utf-8'))

print response.read()