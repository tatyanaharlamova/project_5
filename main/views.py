from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main.models import Students


class StudentListView(ListView):
    model = Students


# def index(request):
#     students_list = Students.objects.all()
#     context = {
#         'object_list': students_list,
#         'title': 'Главная'
#         }
#     return render(request, 'main/index.html', context)


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


class StudentDetailView(DetailView):
    model = Students


class StudentCreateView(CreateView):
    model = Students
    fields = ('first_name', 'last_name', 'avatar')
    success_url = reverse_lazy('main:index')

# def view_student(request, pk):
#     student_item = get_object_or_404(Students, pk=pk)
#     context = {'object': student_item}
#     return render(request, 'main/student_detail.html', context)


class StudentUpdateView(UpdateView):
    model = Students
    fields = ('first_name', 'last_name', 'avatar')
    success_url = reverse_lazy('main:index')


class StudentDeleteView(DeleteView):
    model = Students
    success_url = reverse_lazy('main:index')


def toggle_activity(request, pk):
    student_item = get_object_or_404(Students, pk=pk)
    if student_item.is_active:
        student_item.is_active = False
    else:
        student_item.is_active = True

    student_item.save()
    return redirect(reverse('main:index'))
