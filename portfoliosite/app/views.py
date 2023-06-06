from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post, Question
from .forms import ContactForm
# Create your views here.

def home_page(request):
    return render(request, 'app/index.html')

class ListProjects(ListView):
    model = Post
    template_name = 'app/listprojects.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()


def show_post(request, post_id):
    print(request.GET)
    #return HttpResponse(f"Page {post_id}")
    post = get_object_or_404(Post, id=post_id)

    context = {'title': post.title,
               'post': post}

    return render(request, 'app/oneproject.html', context=context)


def questions(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Обработка данных формы
            email = form.cleaned_data
            question = Question.objects.create(author=form.cleaned_data['name'],
                                               contact=form.cleaned_data['email'],
                                               content=form.cleaned_data['content'])

            # Дальнейшая обработка или сохранение данных

    return render(request, 'app/questions.html', {'form': form})