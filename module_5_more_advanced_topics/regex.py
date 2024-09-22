#!/usr/bin/env python3


import re


# Find the age of every human in the paragraph.
text = """
Rebecca is 26 years old.
Steph is 99.
My friend Leslie is 44.
Coral is 104.
My dog is 3 years old.
Little boy Billy is 0.
Griss (my cat) is 17!
"""
ages = re.findall('TODO', text)
print(ages)
assert ages == ['26', '99', '44', '104', '0']


# Find all words (everything that isn't punctuation or spaces) in the following text.
text = """
'Twas brillig, and the slithy toves
      Did gyre and gimble in the wabe:
All mimsy were the borogoves,
      And the mome raths outgrabe.

"Beware the Jabberwock, my son!
      The jaws that bite, the claws that catch!
Beware the Jubjub bird, and shun
      The frumious Bandersnatch!"
"""
words = re.findall('TODO', text)
print(words)
assert words == ['Twas', 'brillig', 'and', 'the', 'slithy', 'toves', 'Did', 'gyre', 'and',
                 'gimble', 'in', 'the', 'wabe', 'All', 'mimsy', 'were', 'the', 'borogoves', 'And',
                 'the', 'mome', 'raths', 'outgrabe', 'Beware', 'the', 'Jabberwock', 'my', 'son',
                 'The', 'jaws', 'that', 'bite', 'the', 'claws', 'that', 'catch', 'Beware', 'the',
                 'Jubjub', 'bird', 'and', 'shun', 'The', 'frumious', 'Bandersnatch']


# Find all IPv4 addresses of the machine from the 'ip a' output.
text = """
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp0s31f6: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
    link/ether 38:f3:ab:cf:bd:28 brd ff:ff:ff:ff:ff:ff
3: wlp0s20f3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 64:6e:e0:ed:03:2d brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.153/24 brd 192.168.1.255 scope global dynamic noprefixroute wlp0s20f3
       valid_lft 81563sec preferred_lft 81563sec
    inet6 fe80::3c28:bf54:ea9a:3036/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
4: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default
    link/ether 02:42:47:c5:b3:88 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
"""
ips = re.findall('TODO', text)
print(ips)
assert ips == ['127.0.0.1', '192.168.1.153', '192.168.1.255', '172.17.0.1', '172.17.255.255']


# Find all words such that the following assertion passes.
text = [
 'timezone',
 'zodiac',
 'trapezoid',
 'zombi',
 "trapezoid's",
 'trapezoidal',
 'trapezoids',
 'vizor',
 "vizor's",
 'vizors',
 "zodiac's",
 'zodiacal',
 'zodiacs',
 "zombi's",
]
words = []
for item in text:
    hits = re.search('TODO', item)
    if hits:
        words.append(hits.group(0))
print(words)
assert words == ['zodiac', 'zombi', "zodiac's", 'zodiacal', 'zodiacs', "zombi's"]
