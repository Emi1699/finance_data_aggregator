import requests
import file_system

with open("C:\\example.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

class 

def get_financials_date
cookies = {
    'cookiesession1': '678B2878UVWXYZABCDEFGIJKLMNOA93E',
    '_ga': 'GA1.2.1355707676.1668264785',
    'BVBCulturePref': 'en-US',
    'ASP.NET_SessionId': '5ioyibt2wcpnvkn5xftctpl5',
    '_gid': 'GA1.2.184486518.1669474268',
    '_gat': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'X-Requested-With': 'XMLHttpRequest',
    'X-MicrosoftAjax': 'Delta=true',
    'Cache-Control': 'no-cache',
    'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    'Origin': 'https://www.bvb.ro',
    'Connection': 'keep-alive',
    'Referer': 'https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx?s=TRANSI',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'cookiesession1=678B2878UVWXYZABCDEFGIJKLMNOA93E; _ga=GA1.2.1355707676.1668264785; BVBCulturePref=en-US; ASP.NET_SessionId=5ioyibt2wcpnvkn5xftctpl5; _gid=GA1.2.184486518.1669474268; _gat=1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

params = {
    's': 'TRANSI',
}

data = {
    'ctl00$MasterScriptManager': 'ctl00$body$updIfttc|ctl00$body$IFTC$182ecbd5-53ed-45a8-abdc-c4c9b66cda85',
    '__EVENTTARGET': '',
    '__EVENTARGUMENT': '',
    '__LASTFOCUS': '',
    '__VIEWSTATE': '4oafHpTjFsp5gceJHQ7Qw+F36SpjMn4xxqzAAJ1K4dxb1EQyNyXcZ06CmxryMeu4waDzo6uJb9P2gsIN+pGuYsV5Ejdah5yxNeUZF3hJ4CBvSagme/DlC8bVkhmDlTWobR2jNJUV1ojmF/KdZ2ps4nyhzpQPgGi3mfWvLCkwQDMGP82r2O/sNm8hu9OJdSjA5DtxxFx9aENHf+tl9QvB+PYzbKt7tB4y4VNFJ+5mdJ0x7wQos/PBRuArEvCRORX/CvbQrl6CYZj4miNVNxMxYc0kdzlxYq+0CNM1bXajoD+ZuM5aI7W/jY2dFc8HjdpXc7LO5GcKF1zDluPIRsy6KAReT+Jopj3Q1wngc8MZtpkE1z7mfC/uga2VGLJH5ks/1Ly2Du0PP8vCM+n2wEUVcE33XvACzxTeDTOEJ87Tdwzqb3GTf8Dz4Q0QF6sqyvA3ANqD/pAx7HiZ9zwKrQPLY2WE8bvH5GRS81nd5Z/4g8G4CQFlXZQjnd2b4rqeRt5QPmYkl0aWw3HPQJUERBtft05N838I3fUPeFjwMu/I2y8o9K3beY0bUJOGmVdm1DG+Z8MzZF0Lh7w7AziuKBt4gcktSoDHmgwfubOArk0PHSJl6fPZIjTydCyRK21QCAZTh+sHDDxOSmh1ka0WF1mgOCZ2YxcOW4qaa9YqX/8SwHrQgm+76hljy8Je8LVXwZwYt1vZ4OZn0jmVFSCVCrCWtyXIwSfs+PG4/jl4r9D6/2o0pihC9aEgN8cMWIi8QuDPWc3aU0YwAChIERSJDirHZ4VIJweA0cZVokNbMYBnBQxajyx9YvBpTWyRKqWaIjCLdBjnzkBI1vpC/X63u8CSgjVyK1fduOzGt7FYAaEO3eUdeXpAwgHElBdcQeVjGR6oCOp5tposjijVtzHP8sFd3rr32/0Oww+NVaqg76PU/Xg4v/QGt1wLZrNUUkPkgipuHtH8tTzslUKkBtpWT/w5B39C4rRE7uKA64hkOsW0B3+4TlbE9Vn6i3esvBFyuHiJp8SPugZ4odOUJPokfdZyYJOYmSAJbtPIsfb5ijCSmPv2W85hXBe/W4BTu167pF+IPTTmwHQtGmARs5pDtlZtIYorzDxWqyPzIr7lkU/uNmkzV+eEF35FzhzdAKeO4hRGIsTPc3fpqi1ppHozVlQjS8M3XAgnfyvd+Kme0bYtojwd+WN11y0QmMtlxBZLZNndT7WFjX/cPVGbubHhGsSXGyC/BVYDzmkZUHUDgjDfx+IUi3h6pfFnFVELbjHBW+fGob1XxGyD70n4hlpNazSh+Q0zPBwZB6vvkt3cC2KlUpNvEAIA2LcJxaBHhEeX0J8FcLTeT7yoiBlZz5pAowfC271EdL4IjQQUSNRb/xBVEe1Wip3bx2UBUstAS8kIcqNfmPUdecdWcSPTLjhaak9tBDF9YCWh+ytqgOBRZ2XFh5qv0IASu3O5tI/KM0CPG5ANNGRdacRgE3zfprq/2lpMLL3xCgcbsK9t8jyYg75Scb2gr8g0NGpDjZ0LI2cSeiKheB6Gib18sX5h1Jf6FBvHuEYEmEIRVr7Y/FK0KNEJiMw2fdkMKV+ZRTA3fNgBvRwQnbmoUV/GDsndIeI0D2rFMi32t5+zDeEeXmwYfIo/1NmypsN9W9p9uqJHZbSOAZ9lkGh7HKn3REPPaZgE0bfi/v4xfK8ojPximdUjNxFldZ340xvDmYq79eavxFLVEqvZ5V/n0oOR8f6z15CzRvq+5ICYnK0jca6jw6Kq7qqSSrXJZ1gW27Lmf5WfcFS9AisxZJsvZjGJy+jS3UlHn2C/iNBln9N/n4TQu0urNFlBacj2MemtshloB7gOE5fKbbr3ZFbt8j+fXcP+8FHfflcVobzYrqYQ+3xwXfvB+fIJW5MAgk95+PiQ8DR/ZTcSuLRpFnJo/Dncq3XE9EbRajhM4MjHXdcMu+1sGBTIE8xPfDWnOaTw/AwMh+oaMZzUQ0oi+lYvi+2lIGsV9LwAgoO5c0cry2AgsQ7EoLXNBjZuuIXIEjk0hxcVntVtIyFGsP/cMssix8Qd2EouAI1vECPVdgzZIRAmGYAst3q61e7sKJk4KM50+lSjYZS+CXQ5x1AgUYFbbx8SlY7c3qYc9XiSWCdNIqV0NxwChXsSsHJGmen3PuxWBRznw+5mkJnh9YkIGmB6798C7wMGZ+x+upkhWziXHIq07+nL2fc2sAu+lSdFGCPds1hWZ6Nd3/vv1qxBX74up7jVFf4jFAjijx1WRMX9UjDgYmfGje8bkjSdkj2jil6ZWmqOdCszOj4thUTJyhLtnHH1BuOZTDPaE3SEu/t37s57ZcA975RDl9EWas3CNcKPhomqbAuAnyAvFNh2GsAdU9F4yQ/eubu16A6vsdLYiAcpKFxMLLFLdifpcufVVCyRg7JwUWEWQ7uwsuSFY/jng7aXmTPLFYJvfEaqLF5kOaW2RTceEiVZtqrwawRRgCy+zK+D0SIQnkeXtUVLUZI0YWTm2vPlieW3Yb2xTQniIax4glyKjI4n17PTv6wfvAEEH3DH3rUl3H0SznYl0RAz645yW7RIXcgkiLlQvlslPIGtRrP3p1HCHtvA3eUylrIJvT/JBTt9DsNtaWnwHLjCUqbxzb2lj4wGPQoyWs77wzkKS5dvbNNWaleRXNpRhbB9le79YxEh2ez9Htvt+r+LrZUwnS0NpMdsMF3vmEat/RbvTtPA5+PoY7HG6mWU2CHKMFp3qJ/2tBUeNkQhorS6oHt3hZV7eMlIEbUuauMfCYrjNlODgXV+V6VzXaBnMnhb5UDmY1J+S6SAKYuX7gJLzrggq9xjaVO9Yweu+fdreOq65+ygfY/txIYhHHxhwna9sZwmmsdL3jyDw+DVmsuHnNxM57FZ1rpdPC77lv44IuJXZm6WKhf0xA0WH21V8BN7EgS6rAFqwxOq7X6tTbJTXxxK3uQBRfzeFwVmhSuWh6o3ampyBv26Du77PTRAcwwzaQ3rfdUahoehM4x9hfAFzD8HtJalsuRRYBPu0Q6ZTaLKJjTCbgQz/ZyEKpaFemX7h7fGVTz1OJ/ttEKVDTU88KqFPpz2NgjcKJXY9Ftb3dzs3ef9vjMV8sDSRbA7QyP4lHfI44kStWjN89FbeYyAb8+pUWekvJ+DP1fvTZll/3l8Nso2SvrxMO5snR3YGKHN7iJpmBHBUalleECrbqBtxWke5i8ulievS+cD1RJk4DjTlKpCrdoFQ7IMHiCagas06XianZiM95z7brMnq6z/DGQtX/+ebx/ltqQHfOuSpkwnUES774x9uBvx+/AzBrWB6enwoELtfqdjzeVUHR+kfN4aE+jzWlWWSX4fc6LK8cbrXUMePB57h4YLj2QyCbwaLGDeUGjDzLMEnmO3KOaggDwaM4tJZmd0gI4YgcpjCrhCTQbMeZkDpAm7L5bD1LYlZWEbK+axjZ2zlPxqCOHDhVSXjGsw1iEwkOEt/pRwJtqloGT/6cjMO5V5EXHgbNtX40qK3tqLBKl8vC2/krQqH+wauSKpDaTpkmYzelMJIqed++JM/aNcsvY6AGG8bg98XSLVB9wO3kzD54SUaFHfVjfkKI0iqDxuw52RCQqUUyPNg/eCkfb4jd05nZmSE+j2GQ+CR3uEzfEMmJaIczMYUpcVxL+u6tIZxSQir4g4yjR4TprZxCXG6Lz7MjHcNN2AjNYmcxyi3VyLkk+LRuvqUwHiY/ZUN1cG6YjEht+Fg6DoG3xBY42D1JMMmMrcTVyvisOYJjqiHsPf8PnqTcxR5J+KiWrMm/xw5gE6xPV1zb1ktT2lx//qE3RKeyXWjRYAkhb49llQsE5qpzwiRL4wvsDOssfvpZl8VGyAVgBr7EDQdcS/iLmvTY9ke32P4TtdMGFzYt8zc/KLHtO0fpgz4Ur1HXS/F1y1L8ZSdOSrU/qi+q2o8RSQmWQ4qVvbzaDpDJrtr8cZO6yc8eqlwXqAmp89ZeJCDOgSvEb+nKt1WThjkPqXsEFsk6bNK8nGxxRvh0Uiu1z6N5K1a4xvAmG4U+rjaYyanA0p0u4D+KevuOJxcbBg1FPzZDNEDeLiQt1OqTJJeh1fAUFZGYAmsM6c49bDyjp7ZMJMW/i4c3J+EQxL/027/3P4x8z/v9+JgL0TLnUuz81EsAfiNXW0gXnoGg2UGG57SytYDUhP4miuYa0u7wed+IZ0lZwNYVsi4dH6wG+MT+tFtIpVI30gFUXjEBbGhfZkqiPppTVDZKPuTNyr2cKPGCSAy+muHi7uhPHnXrgD6Et6xOcK+H6Y/w2lNKw8fMcc2GWZoWMoEMyRQTl2C9Gc8YAQ8B8R0KX9ujTdlRJSB0kZM7+3YnV6ETdYGlKhxhX4uT/gnacUGBkjlJXkqpo1+WMWQWFpB6TXwigrfzVNkBb2MkTTGmNB4H4AkmsK/4V/QUjjSgvCfC8Sn7qClgfyY9db1RXnbPLbGAUKvOEzJNf53z+EzdASRkfWnFUYnfAJegxYS30qZlNh1xXh33JiTGn8XVpu7tCK5edqYkaOQaZbA8RzsowRDYfk68/lJ2LFM9iyqjBZBvZndaXF91liDuRm+WQyErqWjXdvRv5ZH8XoY5uuLxnIkbLWZnSl3QnRWKqlFdONJUX/D0J0Hfo6O4YpB1WRptNfepEPK11JOBlCNMr4OblnHBIAmIJhQflIp4G2MVSnhlcSMC3kDeTPJuZroLhRBLxm672CmgGUXE7LINJeKgkcgUuGKmoXwvwW/wpJK8Y95pP8SRn3AEfVEN0v7wKg8cXuKtBaOD6JVOucqYNy0fcVZsqR7k39eFfgGg+Ls6SW+w==',
    '__VIEWSTATEGENERATOR': 'A396FC17',
    '__VIEWSTATEENCRYPTED': '',
    '__EVENTVALIDATION': 'cpO4A6BefJkzlebzvu5Mcx+er6OulrVRAIt3vhrbrH5Xh7OkgSqKdUbd21vl5+7zT/F0celejAKhvZouKFa6vlvp5o89+Sczuej/MMtmshf+Wd4lnDSDhY8H6ytDfqhLeAvOZOLpi9WThS1siRD+uI29zkT4ykpIORRdnXCgLiewNSmHHspscbJ87cne1siI1L3fGASqP3UNV/it++k58+z3K+k0p5j82pYmNUkyF8eLtYAuwqB912x/2daZ08DGBq1wPUzbxwiFAt4MLpEfNA==',
    'ctl00$body$ctl02$NewsBySymbolControl$chOutVolatility': 'on',
    'ctl00$body$ctl02$NewsBySymbolControl$chOutInsiders': 'on',
    '__ASYNCPOST': 'true',
    'ctl00$body$IFTC$182ecbd5-53ed-45a8-abdc-c4c9b66cda85': 'Financials',
}

response = requests.post('https://www.bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx', params=params, headers=headers, data=data)

file_system.write_to_file("test_curl.html", response.text, "test")