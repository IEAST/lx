from django.shortcuts import render
from blog.models import Article


# Create your views here.
def get_index_page(request):
    all_article = Article.objects.all()
    return render(request, 'blog/index.html', {
        'article_list': all_article
    })


def get_detail_page(request):
    curr_article = Article.objects.all()[0]
    section_list = curr_article.content.split('/n')
    return render(request, 'blog/detail.html', {
        'curr_article': curr_article,
        'section_list': section_list
    })


