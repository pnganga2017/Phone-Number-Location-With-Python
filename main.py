import phonenumbers
from test import number

from phonenumbers import geocoder
ch_nmber = phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_nmber,"en"))

from phonenumbers import carrier
service_nmber = phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_nmber,"en"))

from phonenumbers import timezone
r_number = phonenumbers.parse(number,"RO")
print(timezone.time_zones_for_number(r_number))




