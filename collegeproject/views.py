from collegeproject.decorators import unauthenticated_user
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project
import re
import csv
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
import pandas as pd
import os
from pandas.errors import EmptyDataError

# Create your views here.

@unauthenticated_user
def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email_regex='[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$'
        if password1 == password2:
            if bool(re.search(email_regex,email))==False:
                messages.error(request,'Invalid  '+email)
                return redirect('register')
            elif len(username)<8:
                messages.error(request,username+' must contain atleast 8 characters')
                return redirect('register')
            elif len(password1)<7:
                messages.error(request,password1+' must contain atleast 8 characters')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.error(request,username+' Exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request,email+' Exist')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password1,first_name=first_name,last_name=last_name)
                user.save()
        else:
            messages.error(request,'Passwords are Incorrect')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, "register.html")



@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')


@login_required(login_url='login')
def home(request):
    project=Project.objects.filter()
    context={'project':project}
    return render(request, 'home.html',context)





@login_required(login_url='login')
def createProject(request):
    if request.method == 'POST' :
        Academic=request.POST.get('academic')
        ProjectType=request.POST.get("project-type")
        Department=request.POST.get("department")
        size1=request.POST.get("size")
        GroupSize=int(size1)
        Title=request.POST.get("title")
        StudentRollno1=request.POST.get("st-rno1")
        StudentName1=request.POST.get("st-name1")
        StudentEmail1=request.POST.get("st-email1")
        StudentMobileNumber1=request.POST.get("st-mobilenumber1")

        StudentRollno2=request.POST.get("st-rno2")
        StudentName2=request.POST.get("st-name2")
        StudentEmail2=request.POST.get("st-email2")
        StudentMobileNumber2=request.POST.get("st-mobilenumber2")

        StudentRollno3=request.POST.get("st-rno3")
        StudentName3=request.POST.get("st-name3")
        StudentEmail3=request.POST.get("st-email3")
        StudentMobileNumber3=request.POST.get("st-mobilenumber3")

        StudentRollno4=request.POST.get("st-rno4")
        StudentName4=request.POST.get("st-name4")
        StudentEmail4=request.POST.get("st-email4")
        st_mobnum4=request.POST.get("st-mobilenumber4")

        StudentRollno5=request.POST.get("st-rno5")
        StudentName5=request.POST.get("st-name5")
        StudentEmail5=request.POST.get("st-email5")
        st_mobnum5=request.POST.get("st-mobilenumber5")

        Research=request.POST.get("research")
        Software=request.POST.get("software")
        GuideName=request.POST.get("guide-name")
        GuideNumber=request.POST.get("guide-number")
        GuideEmail=request.POST.get("guide-email")
        File=request.FILES["file"]
        
        id_regex="(\\d{2}).*(\\d{3})"
        name_regex="^[a-zA-Z ]*$"
        email_regex=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        st_rollno=[StudentRollno1,StudentRollno2,StudentRollno3,StudentRollno4,StudentRollno5]
        st_names=[StudentName1,StudentName2,StudentName3,StudentName4,StudentName5]
        st_mobilenums = [StudentMobileNumber1,StudentMobileNumber2,StudentMobileNumber3,st_mobnum4,st_mobnum5]
        st_emails = [StudentEmail1,StudentEmail2,StudentEmail3,StudentEmail4,StudentEmail5]
        if GroupSize==4:
            if StudentRollno4=='' or StudentName4=='' or StudentEmail4=='' or st_mobnum4=='':
                messages.info(request,'Student4 Fields are Missing')
                return redirect('createproject')
        if GroupSize==5:
            if StudentName5=='' or StudentRollno5=='' or StudentEmail5=='' or st_mobnum5=='' or StudentName4=='' or StudentRollno4=='' or StudentEmail4=='' or st_mobnum4=='':
                messages.info(request,'Student5 Fields are Missing')
                return redirect('createproject')
        if(len(StudentName1)==0 or len(StudentName1)>8 and len(StudentRollno1)==0 or len(StudentRollno1)==10 or len(StudentMobileNumber1)==0 or len(StudentMobileNumber1)==10):
            if(len(StudentName2)==0 or len(StudentName2)>8 and len(StudentRollno2)==0 or len(StudentRollno2)==10 or len(StudentMobileNumber2)==0 or len(StudentMobileNumber2)==10):
                if(len(StudentName3)==0 or len(StudentName3)>8 and len(StudentRollno3)==0 or len(StudentRollno3)==10 or len(StudentMobileNumber3)==0 or len(StudentMobileNumber3)==10):
                    if(len(StudentName4)==0 or len(StudentName4)>8 and len(StudentRollno4)==0 or len(StudentRollno4)==10 or len(st_mobnum4)==0 or len(st_mobnum4)==10):
                        if(len(StudentName5)==0 or len(StudentName5)>8 and len(StudentRollno5)==0 or len(StudentRollno5)==10 or len(st_mobnum5)==0 or len(st_mobnum5)==10):
                            for i in st_names:
                                if i!='':
                                    if(Project.objects.filter(StudentName1=i.title()).exists() or 
                                        Project.objects.filter(StudentName2=i.title()).exists() or 
                                        Project.objects.filter(StudentName3=i.title()).exists()):
                                        messages.info(request,i+' Exist')
                                        return redirect('createproject')
                            for j in st_rollno:
                                if j!='':
                                    if(Project.objects.filter(StudentRollno1=j.upper()).exists() or
                                        Project.objects.filter(StudentRollno2=j.upper()).exists() or
                                        Project.objects.filter(StudentRollno3=j.upper()).exists()):
                                        messages.info(request,j+' Exist')
                                        return redirect('createproject')
                            for i in st_rollno:
                                if len(i)!=0:
                                    if bool(re.search(id_regex,i))==False:
                                        messages.info(request,'Invalid '+i)
                                        return redirect('createproject')
                            for j in st_names:
                                if len(j)!=0:
                                    if bool(re.search(name_regex,j))==False:
                                        messages.info(request,'Invalid '+j)
                                        return redirect('createproject')
                            
                            
                            if bool(re.search(name_regex,GuideName))==False:
                                messages.info(request,'Invalid '+GuideName)
                                return redirect('createproject')
                            try:
                                StudentMobileNumber4= int(st_mobnum4)
                                StudentMobileNumber5= int(st_mobnum5)
                            except ValueError:
                                StudentMobileNumber4=None
                                StudentMobileNumber5=None

                            Project.objects.create(
                            Academic=Academic,
                            ProjectType=ProjectType,
                            Department=Department,
                            GroupSize=GroupSize,
                            Title=Title.title(),
                            StudentName1=StudentName1.title(),
                            StudentRollno1=StudentRollno1.upper(),
                            StudentMobileNumber1=StudentMobileNumber1,
                            StudentEmail1=StudentEmail1,
                            StudentName2=StudentName2.title(),
                            StudentRollno2=StudentRollno2.upper(),
                            StudentMobileNumber2=StudentMobileNumber2,
                            StudentEmail2=StudentEmail2,
                            StudentName3=StudentName3.title(),
                            StudentRollno3=StudentRollno3.upper(),
                            StudentMobileNumber3=StudentMobileNumber3,
                            StudentEmail3=StudentEmail3,
                            StudentName4=StudentName4.title(),
                            StudentRollno4=StudentRollno4.upper(),
                            StudentMobileNumber4=StudentMobileNumber4,
                            StudentEmail4=StudentEmail4,
                            StudentName5=StudentName5.title(),
                            StudentRollno5=StudentRollno5.upper(),
                            StudentMobileNumber5=StudentMobileNumber5,
                            StudentEmail5=StudentEmail5,
                            Research=Research,
                            Software=Software,
                            GuideName=GuideName.title(),
                            GuideNumber=GuideNumber,
                            GuideEmail=GuideEmail,
                            File=File)
                            messages.success(request,'Successfully added '+Title)
                            return redirect('home')
        messages.info(request,'Student name must contain atleast 8 characters and Student Id must contain 10 characters')
        return redirect('createproject')
    return render(request, 'form.html')


@login_required(login_url='login')
def uploadfile(request):
    res=''
    count=0
    user_exist =[]
    id_regex="(\\d{2}).*(\\d{3})"
    name_regex="^[a-zA-Z ]*$"
    email_regex=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if request.method=='POST':
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename =fs.save(myfile.name, myfile)
        file_url = fs.url(filename)
        excel_file = file_url
        try:
            excel_data = pd.read_csv("."+excel_file)
            df = pd.DataFrame(excel_data)
        except EmptyDataError:
                df = pd.DataFrame()
        if df.empty:
            messages.info(request,'No cells exists')
            return redirect('uploadexcelfile')
        df.fillna(0,inplace=True)
        data_cells = len(df.index)
        dbframe = df
        count1=0
        for db in dbframe.itertuples():
            stu_names = [db.StudentName1,db.StudentName2,db.StudentName3,db.StudentName4,db.StudentName5]
            stu_id = [db.StudentRollno1,db.StudentRollno2,db.StudentRollno3,db.StudentRollno4,db.StudentRollno5]
            stu_mobile = [db.StudentMobileNumber1,db.StudentMobileNumber2,db.StudentMobileNumber3,db.StudentMobileNumber4,db.StudentMobileNumber5]
            stu_email = [db.StudentEmail1,db.StudentEmail2,db.StudentEmail3,db.StudentEmail4,db.StudentEmail5]
            student_details = [stu_names,stu_id,stu_mobile,stu_email]            
            for sub_student_details in student_details:
                for value in sub_student_details:
                            if sub_student_details==stu_names:
                                if(len(str(value))>8):
                                    if(Project.objects.filter(StudentName1=value.title()).exists() or
                                    Project.objects.filter(StudentName2=value.title()).exists() or
                                    Project.objects.filter(StudentName3=value.title()).exists() or
                                    Project.objects.filter(StudentName4=value.title()).exists() or
                                    Project.objects.filter(StudentName5=value.title()).exists()):
                                        index=db.Index
                                        if not df.Title[index] in user_exist:
                                            user_exist.append(df.Title[index])

                                        
                                    elif bool(re.search(name_regex,value))==False:
                                        messages.info(request,'Invalid  '+value.title())
                                        return redirect('uploadexcelfile')

                                    elif value==0.0:
                                        pass
                                    else:
                                        messages.info(request,value.title()+'  Required Minimum 8 Characters')
                                        return redirect('uploadexcelfile')
                            elif sub_student_details==stu_id:
                                if(len(str(value))==10):
                                    if(Project.objects.filter(StudentRollno1=value.upper()).exists() or
                                    Project.objects.filter(StudentRollno2=value.upper()).exists() or
                                    Project.objects.filter(StudentRollno3=value.upper()).exists() or
                                    Project.objects.filter(StudentRollno4=value.upper()).exists() or
                                    Project.objects.filter(StudentRollno5=value.upper()).exists()):
                                        
                                        messages.info(request,value.upper()+'  Already Exists')
                                        return redirect('uploadexcelfile')
                                    elif bool(re.search(id_regex,value))==False:
                                        messages.info(request,'Invalid  '+value.upper())
                                        return redirect('uploadexcelfile')

                                elif value==0.0:
                                    pass
                                else:
                                    messages.info(request,value.upper()+'  Required 10 Characters')
                                    return redirect('uploadexcelfile')
                            elif sub_student_details==stu_mobile:
                                print(type(value))
                                
                                if(len(str(value))==10):
                                        if(Project.objects.filter(StudentMobileNumber1=value).exists() or
                                        Project.objects.filter(StudentMobileNumber2=value).exists() or
                                        Project.objects.filter(StudentMobileNumber3=value).exists() or
                                        Project.objects.filter(StudentMobileNumber4=value).exists() or
                                        Project.objects.filter(StudentMobileNumber5=value).exists()):
                                            user_exist.append(value)
                                            messages.info(request,str(value)+' Already Exists')
                                            return redirect('uploadexcelfile')
                                        elif type(value)!=int:
                                            messages.info(request,str(value)+' Must Contain Only Numbers')
                                            return redirect('uploadexcelfile')
                                elif value==0:
                                        pass
                                
                                else:
                                        messages.info(request,str(value)+'  Required 10 Characters')
                                        return redirect('uploadexcelfile')
                                    
                            elif sub_student_details==stu_email:
                                if(len(str(value))>8):
                                    if(Project.objects.filter(StudentEmail1=value).exists() or
                                    Project.objects.filter(StudentEmail2=value).exists() or
                                    Project.objects.filter(StudentEmail3=value).exists() or
                                    Project.objects.filter(StudentEmail4=value).exists() or
                                    Project.objects.filter(StudentEmail5=value).exists()):
                                        messages.info(request,value+'  Already Exists')
                                        return redirect('uploadexcelfile')
                                    elif bool(re.search(email_regex,value))==False:
                                        messages.info(request,'Invalid  '+value)
                                        return redirect('uploadexcelfile')

                                elif value==0.0:
                                    pass
                                else:
                                    messages.info(request,value+'  Required 8 Characters')
                                    return redirect('uploadexcelfile')
                            else:
                                pass
        for i in user_exist:
            res+=i.title()
            res+=','
        if user_exist is not None:
            messages.info(request,res+' Already Exist')
            return redirect('uploadexcelfile')
            count+=1
        if data_cells==count:
            print(count)
            for data in dbframe.itertuples():
                Project.objects.create(
                    Academic=data.Academic,
                    ProjectType=data.ProjectType,
                    Department=data.Department,
                    GroupSize=data.GroupSize,
                    Title=data.Title.title(),
                    StudentName1=data.StudentName1.title(),
                    StudentRollno1=data.StudentRollno1.upper(),
                    StudentMobileNumber1=data.StudentMobileNumber1,
                    StudentEmail1=data.StudentEmail1,
                    StudentName2=data.StudentName2.title(),
                    StudentRollno2=data.StudentRollno2.upper(),
                    StudentMobileNumber2=data.StudentMobileNumber2,
                    StudentEmail2=data.StudentEmail2,
                    StudentName3=data.StudentName3.title(),
                    StudentRollno3=data.StudentRollno3.upper(),
                    StudentMobileNumber3=data.StudentMobileNumber3,
                    StudentEmail3=data.StudentEmail3,
                    StudentName4=str(data.StudentName4).title(),
                    StudentRollno4=str(data.StudentRollno4).upper(),
                    StudentMobileNumber4=int(data.StudentMobileNumber4),
                    StudentEmail4=data.StudentEmail4,
                    StudentName5=str(data.StudentName5).title(),
                    StudentRollno5=str(data.StudentRollno5).upper(),
                    StudentMobileNumber5=int(data.StudentMobileNumber5),
                    StudentEmail5=data.StudentEmail5,
                    Research=data.Research,
                    Software=data.Software,
                    GuideName=str(data.GuideName).title(),
                    GuideNumber=data.GuideNumber,
                    GuideEmail=data.GuideEmail,
                    File=data.File)
            messages.success(request,'Successfully added')
            return redirect('home')
    return render(request, 'uploadfile.html')




@login_required(login_url='login')
def update(request,id1):
    project = Project.objects.get(id=id1)
    if request.method == 'POST':
        project.Academic=request.POST.get('academic')
        project.ProjectType=request.POST.get("project-type")
        project.Department=request.POST.get("department")
        project.size1=request.POST.get("size")
        GroupSize=int(project.size1)
        project.Title=request.POST.get("title").title()
        project.StudentRollno1=request.POST.get("st-rno1").upper()
        project.StudentName1=request.POST.get("st-name1").title()
        project.StudentMobileNumber1=request.POST.get("")
        project.StudentEmail1=request.POST.get("")
        project.StudentRollno2=request.POST.get("st-rno2").upper()
        project.StudentName2=request.POST.get("st-name2").title()
        project.StudentMobileNumber2=request.POST.get("")
        project.StudentEmail2=request.POST.get("")
        project.StudentRollno3=request.POST.get("st-rno3").upper()
        project.StudentName3=request.POST.get("st-name3").title()
        project.StudentMobileNumber3=request.POST.get("")
        project.StudentEmail3=request.POST.get("")
        project.StudentRollno4=request.POST.get("st-rno4").upper()
        project.StudentName4=request.POST.get("st-name4").title()
        project.StudentMobileNumber4=request.POST.get("")
        project.StudentEmail4=request.POST.get("")
        project.StudentRollno5=request.POST.get("st-rno5").upper()
        project.StudentName5=request.POST.get("st-name5").title()
        project.StudentMobileNumber5=request.POST.get("")
        project.StudentEmail5=request.POST.get("")
        project.Research=request.POST.get("research")
        project.Software=request.POST.get("software")
        project.GuideName=request.POST.get("guide").title()
        project.GuideEmail=request.POST.get("")
        project.GuideNumber=request.POST.get("")
        project.file=request.FILES["file"]
        print(project.file.url)
        id_regex="(\\d{2}).*(\\d{3})"
        name_regex="^[a-zA-Z ]*$"
        st_rollno=[project.StudentRollno1,project.StudentRollno2,project.StudentRollno3,project.StudentRollno4,project.StudentRollno5]
        st_names=[project.StudentName1,project.StudentName2,project.StudentName3,project.StudentName4,project.stu_name5]
        if GroupSize==4:
            if project.StudentRollno4=='' or project.StudentName4=='':
                messages.info(request,'Student4 Name and Id required')
                return redirect('createproject')
        if GroupSize==5:
            if project.StudentRollno5=='' or project.StudentName5=='':
                messages.info(request,'Student5 Name and Id required')
                return redirect('createproject')
        if len(project.StudentRollno1)==0 or len(project.StudentRollno1)==10 and len(project.StudentName1)==0 or len(project.StudentName1)>8:
            if len(project.StudentRollno2)==0 or len(project.StudentRollno2)==10 and len(project.StudentName2)==0 or len(project.StudentName2)>8:
                if len(project.StudentRollno3)==0 or len(project.StudentRollno3)==10 and len(project.StudentName3)==0 or len(project.StudentName3)>8:
                    if len(project.StudentRollno4)==0 or len(project.StudentRollno4)==10 and len(project.StudentName4)==0 or len(project.StudentName4)>8:
                        if len(project.StudentRollno5)==0 or len(project.StudentRollno5)==10 and len(project.StudentName5)==0 or len(project.StudentName5)>8:
                            for i in st_rollno:
                                if len(i)!=0:
                                    if bool(re.search(id_regex,i))==False:
                                        messages.info(request,'Invalid '+i)
                                        return redirect('createproject')
                            for j in st_names:
                                if len(j)!=0:
                                    if bool(re.search(name_regex,j))==False:
                                        messages.info(request,'Invalid '+j)
                                        return redirect('createproject')
                            if bool(re.search(name_regex,project.GuideName))==False:
                                messages.info(request,'Invalid '+project.GuideName)
                                return redirect('createproject')
                            project.save()
                            messages.success(request,'Successfully updated '+project.Title)
                            return redirect('home')
        messages.info(request,'Student Id must contain 10 characters and Name must contain atleast 8 characters')
        return redirect('createproject')
    return render(request,'form.html',{'project':project})





@login_required(login_url='login')
def updatePage(request):
    if request.method=='POST':
        year=request.POST.get("year")
        protype=request.POST.get("protype")
        dept=request.POST.get("dept")
        updateval=Project.objects.filter(Q(Academic=year) & Q(ProjectType=protype) & Q(Department=dept))
        return render(request,'modify_search_data.html',{'value':updateval})
    return render(request,'modify_search_page.html')



@login_required(login_url='login')
def search(request):
    if request.method=='POST':
        search=request.POST.get('search')
        titles=Project.objects.filter(Q(Title__icontains=search) | Q(Department__icontains=search) | Q(GuideName__icontains=search))
        context={'titles':titles,'search':search}
        if search=='' or search is None:
            return redirect('search')
        return render(request,'searchdata.html',context)
    return render(request,'search.html')





@login_required(login_url='login')
def data(request,id):
    project = Project.objects.get(id=id)
    context = {'project': project }
    return render(request,'data.html',context)




@login_required(login_url='login')
def delete(request,id2):
    project = Project.objects.get(id=id2)
    project.delete()
    messages.success(request,'successfully deleted')
    return redirect('home')



def exportcsv(request):
    projects_data = Project.objects.all()
    response = HttpResponse('')
    response['Content-Disposition'] = 'attachment; filename=students.csv'
    writer = csv.writer(response)
    writer.writerow(['Title', 'Academic', 'ProjectType', 'Department', 'GroupSize',
    'StudentName1','StudentRollno1','StudentMobileNumber1','StudentEmail1',
    'StudentName1','StudentRollno1','StudentMobileNumber1','StudentEmail1',
    'StudentName1','StudentRollno1','StudentMobileNumber1','StudentEmail1',
    'StudentName1','StudentRollno1','StudentMobileNumber1','StudentEmail1',
    'StudentName1','StudentRollno1','StudentMobileNumber1','StudentEmail1',
    'Research','GuideName','GuideNumber','GuideEmail','Software','File'])
    each_data = projects_data.values_list('Title','Academic', 'ProjectType', 'Department', 'GroupSize',
    'StudentName1','StudentRollno1','StudentMobileNumber1','StudentEmail1',
    'StudentName1','StudentRollno1','StudentMobileNumber1','StudentEmail1',
    'StudentName1','StudentRollno1','StudentMobileNumber1','StudentEmail1',
    'StudentName1','StudentRollno1','StudentMobileNumber1','StudentEmail1',
    'StudentName1','StudentRollno1','StudentMobileNumber1','StudentEmail1',
    'Research','GuideName','GuideNumber','GuideEmail','Software','File')
    for data in each_data:
        writer.writerow(data)
    return response


def logoutPage(request):
    logout(request)
    return redirect('login')



def deleteItem(request,id3):
    project = Project.objects.get(id=id3)
    context = {'project': project }
    return render(request,'remainder.html',context)