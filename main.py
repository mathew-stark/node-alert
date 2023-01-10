import urllib.request
for i in range(6):
    headers = {'User-Agent': 'my-app/0.0.1'}
    req = urllib.request.Request("https://in.bookmyshow.com/buytickets/luxe-cinemas-chennai/cinema-chen-JACM-MT/20230112", headers=headers)
    response=urllib.request.urlopen(req)
    code = str(response.read())
    text = "Varisu"
    print(text in code)