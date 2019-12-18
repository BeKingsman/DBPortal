from django.shortcuts import render,redirect
from .forms import *
from django.http import HttpResponse
import xlrd
from .models import *


from .models import *
# Create your views here.
def upload_excel(request):

   if request.method == 'POST':
       userform = user_form(request.POST)
       excelform = excel_form(request.POST,request.FILES)
       if(userform.is_valid()):
           userform.save()
           return redirect(upload_excel)
       elif(excelform.is_valid()):
           excelform.instance.uploaded_by = request.user
           x = excelform.save()
           path = str(excelform.instance.sheet.path)
           user_profile_from_excel(path)
           return redirect(upload_excel)       

   excelform = excel_form()
   userform = user_form()
   return render(request,'staff/excel.html',{'form':excelform,'user_form':userform})

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
