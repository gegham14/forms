from django.shortcuts import render, redirect
from .forms import StudentForm


def students(request):
    error = ''

    Max_File_Size = 5 * 1024 * 1024

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():
            uploaded_file = request.FILES.get('video')

            if uploaded_file and uploaded_file.size > Max_File_Size:
                error = 'File size exceeds the 5 MB limit'

            else:
                new_user = form.save(
                    commit=False)

                f_name = form.cleaned_data['first_name']

                if ' ' in f_name:
                    f_name = f_name.replace(' ', '')
                new_user.first_name = f_name
                form.save()
                return redirect('/')
        else:
            print(form.errors)
            error = 'Your number is already used'

    context = {'student': StudentForm(), 'error': error}
    return render(request, 'student.html', context)
