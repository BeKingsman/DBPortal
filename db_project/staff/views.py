from django.shortcuts import render,redirect
from .forms import *
from django.http import HttpResponse
import xlrd
from .models import *
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from staff.serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import *
from rest_framework import generics,reverse
from .permissions import *
from django.core.mail import send_mail
from django.contrib.auth import logout,authenticate,login


from .models import *
# Create your views here.

def HomePage(request):
   return render(request,'staff/home.html')





def upload_excel(request):
 if request.user.is_staff==True:
   if request.method == 'POST':
       userform = user_form(request.POST)
       excelform = excel_form(request.POST,request.FILES)
       if(userform.is_valid()):
           userform.save()

           return redirect('home-page')
       elif(excelform.is_valid()):
           excelform.instance.uploaded_by = request.user
           x = excelform.save()
           path = str(excelform.instance.sheet.path)
           user_profile_from_excel(path)
           return redirect('home-page')

   excelform = excel_form()
   userform = user_form()
   return render(request,'staff/excel.html',{'form':excelform,'user_form':userform})
 return HttpResponse("You Are Not Authenticated")

def get_model(name,model):
    obj = model.objects.get(name = name)
    return obj



def user_profile_from_excel(path):

     book = xlrd.open_workbook(path)
     sheet = book.sheet_by_index(0)
     row = sheet.nrows
     cols = sheet.ncols

     for i in range(1,row):

              adhaar_no= int(sheet.cell_value(i,1))
              name = sheet.cell_value(i,2)
              DOB = sheet.cell_value(i,3)
              gender = sheet.cell_value(i,4)
              city = sheet.cell_value(i,5)
              state = sheet.cell_value(i,6)

              city_model = get_model(city,City)
              state_model = get_model(state,State)
              print(DOB)
              new = str((xlrd.xldate_as_datetime(DOB,book.datemode)))[0:10]

              print(new)
              print("")
              birth = str(DOB)

              new = user_profile.objects.create(adhaar_no=adhaar_no,name=name,DOB=new,gender= gender,city=city_model, state=state_model)
              new.save()


def load_cities(request):
    print("")
    print("")
    State_id = request.GET.get('state')
    # st_obj = State.objects.get(id=State_id)
    cities = City.objects.filter(state_id=State_id).order_by('name')
    # cities = City.objects.filter(state=st_obj).order_by('name')

    for city in cities:
        print(city)

    return render(request, 'staff/city_dropdown_list_options.html', {'cities': cities})


class Dber_list(generics.ListCreateAPIView):
    queryset = user_profile.objects.all()
    serializer_class = user_profile_serializer

class Dber_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = user_profile.objects.all()
    serializer_class = user_profile_serializer
    # permission_classes = ['IsStaffOrAdmin']


def mail(request):
    send_mail(
    'testing',
    'Here is the message.',
    'harsh.rollno15@gmail.com',
    ['harshagarwal8055@gmail.com'],
    fail_silently=False,
)
    return HttpResponse(done)


def register(request):

    if request.method == 'POST':
            reg_form = register_form(request.POST)
            if reg_form.is_valid:
                adh = request.POST['Adhaar']
                ad_list =[]
                for user in user_profile.objects.all():
                    if int(user.adhaar_no) == int(adh):
                        u_name = request.POST['username']
                        passw = request.POST['password']
                        user.adhaar_linked = True
                        user.username = u_name
                        user.Password = passw
                        user.save()
                        u_name = request.POST['username']
                        passw = request.POST['password']
                        try:
                            new = User.objects.create(username =u_name,password=passw)
                            new.save()
                            return render(request,'staff/login.html')
                        except exceptions:
                           pass
                return HttpResponse("adhhar number not matched , please contact administrator")
            return HttpResponse("<h3>User Not Found</h3>")

    reg_form = register_form()
    return render(request,'staff/register.html',{'r_form':reg_form})


def login_view(request):
    if request.method == 'POST':
        l_form = login_form(request.POST)
        if l_form.is_valid():
            u_name = request.POST['username']
            passw = request.POST['password']
            user = authenticate(username=u_name,password=passw)
            if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('home-page')
        return HttpResponse("<h3>INVALID CREDENTIALS...!!!!")
    l_form = login_form()
    return render(request,'staff/register.html',{'l_form':l_form})



def HomePage(request):
    return render(request,'staff/home.html')
