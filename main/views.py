from django.shortcuts import render, get_object_or_404

from main.models import Students


def index(request):
    students_list = Students.objects.all()
    context = {
        'object_list': students_list,
        'title': 'Главная'
        }
    return render(request, 'main/index.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        emal = request.POST.get("email")
        massage = request.POST.get("message")
        print(f"{name}, {emal}, {massage}")
    context = {
        'title': 'Контакты'
    }

    return render(request, 'main/contact.html', context)


def view_student(request, pk):
    student_item = get_object_or_404(Students, pk=pk)
    context = {'object': student_item}
    return render(request, 'main/student_detail.html', context)
