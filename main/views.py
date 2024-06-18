from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main.forms import StudentsForm, SubjectForm
from main.models import Students, Subject


class StudentListView(LoginRequiredMixin, ListView):
    model = Students


# def index(request):
#     students_list = Students.objects.all()
#     context = {
#         'object_list': students_list,
#         'title': 'Главная'
#         }
#     return render(request, 'main/index.html', context)

@login_required
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


class StudentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Students
    permission_required = 'main.view_students'


class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin,  CreateView):
    model = Students
    form_class = StudentsForm
    permission_required = 'main.add_students'
    # fields = ('first_name', 'last_name', 'avatar')
    success_url = reverse_lazy('main:index')

# def view_student(request, pk):
#     student_item = get_object_or_404(Students, pk=pk)
#     context = {'object': student_item}
#     return render(request, 'main/student_detail.html', context)


class StudentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Students
    form_class = StudentsForm
    # fields = ('first_name', 'last_name', 'avatar')
    permission_required = 'main.change_students'
    success_url = reverse_lazy('main:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Students, Subject, form=SubjectForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class StudentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Students
    success_url = reverse_lazy('main:index')

    def test_func(self):
        return self.request.user.is_superuser


@login_required
@permission_required('main.view_students')
def toggle_activity(request, pk):
    student_item = get_object_or_404(Students, pk=pk)
    if student_item.is_active:
        student_item.is_active = False
    else:
        student_item.is_active = True

    student_item.save()
    return redirect(reverse('main:index'))
