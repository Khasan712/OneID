from django.shortcuts import render, redirect
import requests, json
from rest_framework.response import Response

from accounts.models import Users
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.


def index(request):
    code = request.GET.get('code', None)
    if code:
        url = 'https://sso.egov.uz/sso/oauth/Authorization.do'
        params = {
            'code': code,
            'grant_type': 'one_authorization_code',
            'client_id': 'unicon_yagona_billing',
            'client_secret': 'N3nk50XmyQFqijewiohDFZdB',
            'redirect_uri': 'redirect_uri',
        }
        res = requests.post(url=url, params=params)
        if res.json().get('access_token'):
            params_data = {
                'code': code,
                'grant_type': 'one_access_token_identify',
                'client_id': 'unicon_yagona_billing',
                'client_secret': 'N3nk50XmyQFqijewiohDFZdB',
                'access_token': res.json().get('access_token'),
            }
            user_data = requests.post(url=url, params=params_data)
            # data = user_data.json()
            if user_data.status_code == 200:
                mob_phone_no = user_data.json().get("mob_phone_no")
                first_name = user_data.json().get("first_name")
                last_name = user_data.json().get("sur_name")
                password = user_data.json().get("sess_id")
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
                    user.set_password(password)
                    user.save()
                return redirect("account", user.id)
    return render(request, 'index.html')



def account(request, pk):
    try:
        user = Users.objects.get(pk=pk)
        print(user)
    except Users.DoesNotExist:
        user = None
    print(user)
    context = {
        'user':user
    }
    return render(request, 'dashboard.html', context)

def logout_user(request):
    logout(request)
    return redirect('index')
    
