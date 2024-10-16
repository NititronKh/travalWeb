from django.shortcuts import render, redirect
from .forms import ContentForm
from .models import Content


def submit_content(request):
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # เปลี่ยนเป็น URL ที่ต้องการหลังบันทึก
    else:
        form = ContentForm()
    return render(request, 'create01.html', {'form': form})


def show_content(request):
    all_contents = Content.objects.all()  # ดึงข้อมูลทั้งหมดจากฐานข้อมูล
    return render(request, 'content2.html', {'contents': all_contents})
