import requests

def write_postcode_to_file(file, postcode):
    try:
        with open(file, 'a') as opened_file:
            var = requests.get("https://api.postcodes.io/postcodes/" + postcode)
            postcode_dic = var.json()
            don = postcode_dic['result']['postcode']
            opened_file.write(don + '\n')
    except FileNotFoundError:
        print('File not found')