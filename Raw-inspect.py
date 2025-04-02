import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Connection": "keep-alive",
}






while True :
  try :
    
   url = input("Enter Url ")
   session = requests.Session()
   response = session.get(url, headers=headers)

   print(response.status_code)
   print(response.text[:50000])  # Print the first 500 characters of the page
  except:
    print("Erorr")
  
