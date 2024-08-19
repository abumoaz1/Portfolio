from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request,"about.html")

def projects(request):
    projects_show= [
        {
            'title':'Extractify',
            'path': 'images/extractify.png',
            'url': 'https://github.com/abumoaz1/Extractify'
        },
        {
            'title':'DevRooms',
            'path': 'images/Devrooms.png',
            'url': 'https://github.com/abumoaz1'
        },
    ]
    return render(request,"projects.html", {"projects_show": projects_show})


def certifications(request):
    cert_show=[
        {
            'title': 'Build and Secure Networks in Google Cloud',
            'path': 'images/1.png',
            'url': 'https://www.cloudskillsboost.google/public_profiles/0fa59aff-c0d8-441e-a5be-b176c511de8e/badges/5083965?utm_medium=social&utm_source=linkedin&utm_campaign=ql-social-share',
        },
        {
            'title': 'Create and Manage Cloud Resources',
            'path': 'images/2.png',
            'url': 'https://www.cloudskillsboost.google/public_profiles/0fa59aff-c0d8-441e-a5be-b176c511de8e/badges/5059357?utm_medium=social&utm_source=linkedin&utm_campaign=ql-social-share',
        },
        {
            'title': 'Data, AI and ML in Google Cloud',
            'path': 'images/3.png',
            'url': 'https://www.cloudskillsboost.google/public_profiles/0fa59aff-c0d8-441e-a5be-b176c511de8e/badges/5076569?utm_medium=social&utm_source=linkedin&utm_campaign=ql-social-share',
        },
        {
            'title': 'Infrastructure in Google Cloud',
            'path': 'images/4.png',
            'url': 'https://www.cloudskillsboost.google/public_profiles/0fa59aff-c0d8-441e-a5be-b176c511de8e/badges/5055277?utm_medium=social&utm_source=linkedin&utm_campaign=ql-social-share',
        },
        {
            'title': 'Google Cloud Computing Foundation: Networking',
            'path': 'images/5.png',
            'url': 'https://www.cloudskillsboost.google/public_profiles/0fa59aff-c0d8-441e-a5be-b176c511de8e/badges/5072845?utm_medium=social&utm_source=linkedin&utm_campaign=ql-social-share',
        },
        {
            'title': 'GenAI',
            'path': 'images/6.png',
            'url': 'https://www.cloudskillsboost.google/public_profiles/0fa59aff-c0d8-441e-a5be-b176c511de8e/badges/5143155?utm_medium=social&utm_source=linkedin&utm_campaign=ql-social-share',
        },
        {
            'title': 'Perform Foundation Data, AI and ML Tasks in Google Cloud',
            'path': 'images/7.png',
            'url': 'https://www.cloudskillsboost.google/public_profiles/0fa59aff-c0d8-441e-a5be-b176c511de8e/badges/5084734?utm_medium=social&utm_source=linkedin&utm_campaign=ql-social-share',
        },
        {
            'title': 'Introduction to Front-End Development',
            'path': 'images/8.png',
            'url' : 'https://coursera.org/share/8970647a0a4f2e467e96282ae4a1d04d'
        },
    ]
    return render(request,"certifications.html", {"cert_show": cert_show})

def contact(request):
    return render(request,"contact.html")



def resume(request):
    resume_path = "myresume/myresume.pdf"
    resume_path = staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path, "rb") as resume_files:
            response = HttpResponse(resume_files.read(), content_type="application/pdf")
            response['content-Disposition'] = 'attachment';filename="myresume.pdf"
            return response
    else:
        return HttpResponse("Resume not found", status=404)