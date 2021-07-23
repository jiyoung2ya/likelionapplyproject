from apply.models import Apply
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.contrib import messages

# Create your views here.

def home(request):
    return render (request, 'home.html')

def new(request):
    if request.method == 'POST':
        if Apply.objects.filter(student_id = request.POST['htmlstudent_id']).exists(): #중복지원인 경우
            exist_apply = get_object_or_404(Apply, student_id = request.POST['htmlstudent_id'])
            messages.info(request, '한 계정당 하나의 지원서만 작성 가능합니다!')
            return redirect('urlnamedetail', exist_apply.id)
        new_apply = Apply()
        new_apply.name = request.POST['htmlname']
        new_apply.student_id = request.POST['htmlstudent_id']
        new_apply.major = request.POST['htmlmajor']
        new_apply.q1 = request.POST['htmlq1']
        new_apply.q2 = request.POST['htmlq2']
        new_apply.q3 = request.POST['htmlq3']
        new_apply.q4 = request.POST['htmlq4']
        new_apply.date = timezone.now()
        new_apply.save()
        return redirect('urlnamehome')
    else:
        return render (request, 'new.html')


def readall(request):
    apply_all = Apply.objects.order_by('-date')
    count_apply = apply_all.count()
    return render(request, 'readall.html', {'views_apply_all':apply_all, 'views_apply':count_apply})

def detail(request, each_id):
    apply = get_object_or_404(Apply, pk = each_id)
    return render (request, 'detail.html', {'views_apply':apply})

def update(request,each_id):
    if request.method == 'POST':
        apply = get_object_or_404(Apply, pk = each_id)
        apply.name = request.POST['htmlname']
        apply.student_id = request.POST['htmlstudent_id']
        apply.major = request.POST['htmlmajor']
        apply.q1 = request.POST['htmlq1']
        apply.q2 = request.POST['htmlq2']
        apply.q3 = request.POST['htmlq3']
        apply.q4 = request.POST['htmlq4']
        apply.date = timezone.now()
        apply.save()
        return redirect('urlnamedetail', apply.id)
    else:
        apply = get_object_or_404(Apply, pk = each_id)
        return render (request, 'update.html', {'update_apply':apply})

def delete(request, each_id):
    apply = get_object_or_404(Apply, pk = each_id)
    apply.delete()
    return redirect('urlnamereadall')

