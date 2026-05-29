import requests

def extract_data(url):
   response = requests.get(url)
   if response.status_code == 200:
      print("Request successful, API Verified!")
      return response.json()
   else:
      print("Unsuccessful Request")
      return []





 