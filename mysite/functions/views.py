from django.shortcuts import render, redirect
from .forms import ContentForm
from .models import Content

def submit_content(request):
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # บันทึกข้อมูลที่กรอกในฟอร์มลงฐานข้อมูล
            return redirect('show_content')  # เปลี่ยนไปหน้าโชว์เนื้อหา
    else:
        form = ContentForm()
    return render(request, 'create01.html', {'form': form})

def show_content(request):
    all_contents = Content.objects.all()  # ดึงข้อมูลทั้งหมดจากฐานข้อมูล
    return render(request, 'content2.html', {'contents': all_contents})
