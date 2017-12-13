# from googlefinance import getQuotes
# import json
#
# print(json.dumps(getQuotes("VLACX")))

# VLACX, VFINX, VMMSX, VWAHX, VWNFX


import json
import requests
from jsoncomment import JsonComment


FINANCE_URL='https://finance.google.com/finance?q={}&output=json'

# Works only for mutual funds
def get_mutual_fund_quote(symbol):
    rsp = requests.get(FINANCE_URL.format(symbol))
    content = rsp.content[6:-2].decode('utf-8')
    content = content.replace("\n", "")
    print(type(content))
    parser = JsonComment(json)
    fin_data = parser.loads(content)
    performance = fin_data['performance']
    print(performance)
    print("----------------------")

my_mutf = ["VLACX", "VFINX", "VMMSX", "VWAHX", "VWNFX"]

for item in my_mutf:
    get_mutual_fund_quote(item)