from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import Teacher


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('psw')
        print("aaaaaaaaaaaaaaaaaaaaaa")
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is None:
            print('user does not exist')
        else:
            print('user exist')
            login(request, user)
            if user.is_staff:
                return redirect('admin')
            else:
                return redirect('login')
    return render(request, 'login.html', {})

def admin_view(request):
    return render(request, 'admin.html', {})


def admission_view(request):
    if request.method == "POST":
        education = request.POST.get("education")
        experience = request.POST.get("experience")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        designation = request.POST.get("designation")
        assignedclass = request.POST.get("assignedclass")
        bloodgroup = request.POST.get("bloodgroup")
        gender = request.POST.get("gender")
        emailaddress = request.POST.get("emailaddress")
        phonenumber = request.POST.get("phonenumber")
        # teacher = Teacher.objects.create(Education=education,Experience=experience,Firstname=firstname,Lastname=lastname,Designation=designation,Assignedclass=assignedclass,Bloodgroup=bloodgroup,Gender=gender,Emailaddress=emailaddress,Phonenumber=phonenumber)
        tea = Teacher()
        tea.Education = education
        tea.Experience = experience
        tea.Firstname = firstname
        tea.Lastname = lastname
        tea.Designation = designation
        tea.Assignedclass = assignedclass
        tea.Bloodgroup = bloodgroup
        tea.Gender = gender
        tea.Emailaddress = emailaddress
        tea.Phonenumber = phonenumber
        tea.save()
        return redirect('admin')

    return render(request, 'admission.html', {})

def registration(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        email = request.POST.get('eaddress')
        password = request.POST.get('psw')
        confirm = request.POST.get('cpsw')
        print(username, email, password, confirm)
        if password == confirm:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('admin')

    return render(request, 'registration.html', {})

#
# def Teacher_view(request):
#     return render(request, 'teacher.html', {})



def Teacherlist(request):
    obj = Teacher.objects.all()
    if request.method == 'POST'and 'delete' in request.POST:
        idd = request.POST.get('delete')
        ob = Teacher.objects.get(id=idd)
        ob.delete()
    return render(request, 'teacherlist.html', {'key': obj})


def editteacher(request,id):
        obj = Teacher.objects.get(id=id)
        if request.method == 'POST':
            education = request.POST.get("education")
            obj.Education = education
            experience = request.POST.get("experience")
            obj.Experience = experience
            firstname = request.POST.get("firstname")
            obj.Firstname = firstname
            lastname = request.POST.get("lastname")
            obj.Lastname = lastname
            designation = request.POST.get("designation")
            obj.Designation = designation
            assignedclass = request.POST.get("assignedclass")
            obj.Assignedclass = assignedclass
            bloodgroup = request.POST.get("bloodgroup")
            obj.Bloodgroup = bloodgroup
            gender = request.POST.get("gender")
            obj.Gender = gender
            emailaddress = request.POST.get("emailaddress")
            obj.Emailaddress = emailaddress
            phonenumber = request.POST.get("phonenumber")
            obj.Phonenumber = phonenumber
            obj.save()

            return redirect('teacherlist')
        return render(request, 'editteacher.html', {})

