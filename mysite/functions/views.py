from django.shortcuts import render,redirect,get_object_or_404
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

@login_required
def edit_content(request, content_id):
    content = get_object_or_404(Content, id=content_id)
    
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES, instance=content)
        if form.is_valid():
            form.save()
            # บันทึกการแก้ไขข้อมูล content
            return redirect('index')  # หลังจากบันทึก ให้กลับไปที่หน้า index
    else:
        form = ContentForm(instance=content)
    
    return render(request, 'edit.html', {'form': form, 'content': content})

@login_required
def delete_content(request, content_id):
    content = get_object_or_404(Content, id=content_id)
    content.delete()
    return redirect('content1')  # หลังลบเสร็จแล้วให้กลับไปที่หน้า index

from django.shortcuts import render, get_object_or_404
from .models import Content

def get_month_in_thai(month_number):
    thai_months = [
        "มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", 
        "พฤษภาคม", "มิถุนายน", "กรกฎาคม", "สิงหาคม", 
        "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"
    ]
    return thai_months[month_number - 1] if 1 <= month_number <= 12 else ""

def content1(request):
    all_contents = Content.objects.filter(type='SOC')  # กรองเฉพาะเนื้อหาประเภท 'SOC'
    
    # แปลงวันที่เป็นภาษาไทย
    for content in all_contents:
        if content.date:  # ตรวจสอบว่ามีวันที่หรือไม่
            content.date_thai = f"{content.date.day} {get_month_in_thai(content.date.month)} {content.date.year}"
    
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