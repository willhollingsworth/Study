from codewars_test import test_framework as Test
import re
# having issues, putting on pause
# |http:\/\/|https:\/\/www\.|http:\/\/www\.)

def domain_name(url):
    return re.sub(r'(http|https)?(:\/\/)?(www\.)?(\w)*(\.).*', r'\4', url)
# (?:http:\/\/|https:\/\/)*(?!www\.)*(?!\.)*(?:\..*)$
Test.assert_equals(domain_name("http://google.com"), "google")
Test.assert_equals(domain_name("http://google.co.jp"), "google")
Test.assert_equals(domain_name("www.xakep.ru"), "xakep")
Test.assert_equals(domain_name("https://youtube.com"), "youtube")