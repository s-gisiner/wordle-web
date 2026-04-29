import requests
from django.conf import settings

def view_all_coins(access_token):
   # Use the access token to make an authenticated request
   headers = {
       'Authorization': f'Bearer {access_token}'
   }


   # Make a GET request with the authorization header
   api_response = requests.get(f"{settings.KRATOS_API_BASE}", headers=headers)


   if api_response.status_code == 200:
       # Process the data from the API
       return api_response.json()
   else:
       print("Failed to access the API endpoint to view all coins:", api_response.status_code)

def view_balance_for_user(access_token, email):
   # Use the access token to make an authenticated request
   headers = {
       'Authorization': f'Bearer {access_token}'
   }


   # Make a GET request with the authorization header
   api_response = requests.get(f"{settings.KRATOS_API_BASE}/player/{email}/", headers=headers)


   if api_response.status_code == 200:
       # Process the data from the API
       return api_response.json()
   else:
       print("Failed to access the API endpoint to view balance for user:", api_response.status_code)

def user_pay(access_token, email, amount):
   headers = {
       'Authorization': f'Bearer {access_token}'
   }

   data = {"amount": amount}

   api_response = requests.post(
       f"{settings.KRATOS_API_BASE}/player/{email}/pay",
       headers=headers,
       data=data
   )

#    print("PAY URL:", f"{settings.KRATOS_API_BASE}/player/{email}/pay")
#    print("PAY STATUS:", api_response.status_code)
#    print("PAY RESPONSE:", api_response.text)

   if api_response.status_code == 200:
       return api_response.json()
   else:
       return None