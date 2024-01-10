"""""""
from django.shortcuts import redirect, render
from teacher_service.models import Teacher
from teacher_service.forms import TeacherForm

# Create your views here.

def teach(request):
    if request.method == "POST" :
        form = TeacherForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = TeacherForm()
    return render(request, 'index.html', {'form' :form})

def show(request):
    teachers = Teacher.objects.all()
    return render(request, 'show.html', {'teachers' : teachers})

def edit(request, id):
    teacher = Teacher.objects.get(id=id)
    return render(request, 'edit.html',{'teacher' :teacher})

def update(request, id):
    teacher = Teacher.objects.get(id-id)
    form = TeacherForm(request.POST, instance=teacher)
    if form.is_valid():
        form.save()
        return("/show")
    return render(request, 'edit.html', {'teacher' :teacher})


def destroy(request, id):
    teacher = Teacher.objects.get(id=id)
    teacher.delete()
    return redirect("/show")
    
            
