from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from .forms import ContentForm
from .models import Content

@login_required
def submit_content(request):
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # บันทึกข้อมูล content ใหม่
            return redirect('index')  # หลังจากบันทึก ให้กลับไปที่หน้า index
    else:
        form = ContentForm()
    
    return render(request, 'create01.html', {'form': form})
def content1(request):
    all_contents = Content.objects.filter(type='SOC')  # กรองเฉพาะเนื้อหาประเภท 'SOC'
    return render(request, 'content1.html', {'contents': all_contents})

def content2(request):
    all_contents = Content.objects.filter(type='ECO')  # กรองเฉพาะเนื้อหาประเภท 'ECO'
    return render(request, 'content2.html', {'contents': all_contents})

def content3(request):
    all_contents = Content.objects.filter(type='POL')  # กรองเฉพาะเนื้อหาประเภท 'POL'
    return render(request, 'content3.html', {'contents': all_contents})

def content4(request):
    all_contents = Content.objects.filter(type='CUL')  # กรองเฉพาะเนื้อหาประเภท 'CUL'
    return render(request, 'content4.html', {'contents': all_contents})

def content5(request):
    all_contents = Content.objects.filter(type='REV')  # กรองเฉพาะเนื้อหาประเภท 'REV'
    return render(request, 'content5.html', {'contents': all_contents})