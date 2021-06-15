import requests

# Send and mange cookies for API request calls
# website to call: https://www.google.com
# track cookies use cookie called 'visit-month'

# send cookies syntax as dict
cookie = {'visit-month': 'May'}
response = requests.get('https://www.google.com', cookies=cookie)
print(response.status_code)

# create request to call common cookie visit-month
se = requests.session()
se.cookies.update(cookie)

# Get cookie as text
res = se.get('https://httpbin.org/cookies', cookies={'visit-year': '2022'})
print(res.text)  # print out two cookies
# res = requests.get('https://httpbin.org/cookies', cookies={'visit-year': '2022'})
# print(res.text)  # print out only cookie visit-year


# Redirection and Timeouts attributes in making reuqest calls
# print history of Redirection, use allow_redirection=False
# to stop request if redirection,  add timeout to wait 1 second to get response
response2 = requests.get('https://systemate.net/index.php/knowledgebase',
                         allow_redirects=False, cookies=cookie, timeout=1)
print(response2.history)
print(response2.status_code)

# Send Attachments through Post request
# website to post request: petstore.swagger, with a petId provided by developers
url = 'https://petstore.swagger.io/v2/pet/9843217/uploadImage'
file = {'file': open('astronomy.jpeg', 'rb')}
r = requests.get(url, files=file)
print(r.status_code)
print(r.text)
