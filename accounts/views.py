from django.shortcuts import render, redirect
import requests, json
from rest_framework.response import Response

from accounts.models import Users
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.


def get_access_token(request):
    code = request.GET.get('code', None)
    if code:
        params = {
                'code': code,
                'grant_type': 'one_authorization_code',
                'client_id': 'unicon_yagona_billing',
                'client_secret': 'N3nk50XmyQFqijewiohDFZdB',
                'redirect_uri': 'redirect_uri',
            }
        url = 'https://sso.egov.uz/sso/oauth/Authorization.do'
        res = requests.post(url=url, params=params)
        access_token = res.json().get('access_token')
        data = {
            "access_token":access_token,
            "code": code
        }
        return data

def get_user_data(request):
    get_data = get_access_token(request)
    code = get_data.get("code")
    access_token = get_data.get("access_token")
    if code and access_token:
        params_data = {
            'code': code,
            'grant_type': 'one_access_token_identify',
            'client_id': 'unicon_yagona_billing',
            'client_secret': 'N3nk50XmyQFqijewiohDFZdB',
            'access_token': access_token,
        }
        url = 'https://sso.egov.uz/sso/oauth/Authorization.do'
        user_data = requests.post(url=url, params=params_data)
        data = user_data.json()
    return data

def index(request):
    code = request.GET.get('code', None)
    if code:
        user_data = get_user_data(request)
        if user_data:
            mob_phone_no = user_data.get("mob_phone_no")
            first_name = user_data.get("first_name")
            last_name = user_data.get("sur_name")
            try:
                user = Users.objects.get(phone_number=mob_phone_no)
            except Users.DoesNotExist:
                user = None
            if user is None:
                user = Users.objects.create(
                    phone_number=mob_phone_no,
                    first_name=first_name,
                    last_name=last_name
                )
                return redirect("account", user.id)
            else:
                return redirect("account", user.id)

    
    return render(request, 'index.html')



def account(request, pk):
    try:
        user = Users.objects.get(pk=pk)
        print(user)
    except Users.DoesNotExist:
        user = None
    # if user is not authenticated:
    #     pass
    print(user)
    context = {
        'user':user
    }
    return render(request, 'dashboard.html', context)

def logout_user(request):
    logout(request)
    return redirect('index')
    



# get_data = get_access_token(request)
#     code = get_data.get("code")
    access_token = get_data.get("access_token")
    # if get_data:
    #     params_data = {
    #         'code': code,
    #         'grant_type': 'one_access_token_identify',
    #         'client_id': 'unicon_yagona_billing',
    #         'client_secret': 'N3nk50XmyQFqijewiohDFZdB',
    #         'access_token': access_token,
    #     }
    #     user_data = requests.post(url=url, params=params_data)
    #     # data = user_data.json()

    # code = request.GET.get('code', None)
    # if code:
    #     params = {
    #         'code': code,
    #         'grant_type': 'one_authorization_code',
    #         'client_id': 'unicon_yagona_billing',
    #         'client_secret': 'N3nk50XmyQFqijewiohDFZdB',
    #         'redirect_uri': 'redirect_uri',
    #     }
    #     url = 'https://sso.egov.uz/sso/oauth/Authorization.do'
    #     res = requests.post(url=url, params=params)