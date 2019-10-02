#had to import request again >> setting >> project interpreter
import requests

    #requesting post code detail using request API
request_my_postcode = requests.get('https://api.postcodes.io/postcodes/SE50XN')

    #Print post code to ensure information are returned as  object
print(request_my_postcode)

    #Print retured response at poscode
print(request_my_postcode.json())

    # collecting poscode info
print(request_my_postcode.json()['result']['postcode'])
print(request_my_postcode.json()['result']['nhs_ha'])
print(request_my_postcode.json()['result']['country'])

info_1 = request_my_postcode.json()['result']['postcode']
info_2 = request_my_postcode.json()['result']['nhs_ha']
info_3 = request_my_postcode.json()['result']['country']




# Objective:
#
# make API GET call
# Write some details of the post code to TXT
# Postcode.io to txt
#
# Objective: make API GET call Write some details
# of the post code to TXT
# http://postcodes.io/ Specifications:
# git - At least 6 commits github README.me
# .gitignore function that take
# in a post code function that write
# Handle one error What happend
# if you put an invalid URL? Good conventions
# - Naming and file organization/structure
#
# http://postcodes.io/