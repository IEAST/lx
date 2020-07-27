from django.shortcuts import render
from blog.models import Article
from django.core.paginator import Paginator


# Create your views here.
def get_index_page(request):
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1

    print(page)
    all_article = Article.objects.all()
    all_article_list=Article.objects.order_by('-publish_date')
    paginator = Paginator(all_article, 4)
    page_num = paginator.num_pages
    page_article_list = paginator.page(page)
    if page_article_list.has_next():
        next_page = page + 1
    else:
        next_page = page
    if page_article_list.has_previous():
        previous_page = page - 1
    else:
        previous_page = page
    return render(request, 'blog/index.html', {
        'article_list': page_article_list,
        'page_num': range(1, page_num + 1),
        'curr_page': page,
        'next_page': next_page,
        'previous_page': previous_page,
        'all_article_list': all_article_list
    })


def get_detail_page(request, article_id):
    all_article = Article.objects.all()
    curr_article = None
    previous_index = 0
    next_index = 0
    previous_article = None
    next_article = None
    for index, article in enumerate(all_article):
        if index == 0:
            previous_index = 0
            next_index = index + 1
        elif index == len(all_article) - 1:
            previous_index = index - 1
            next_index = index
        else:
            previous_index = index - 1
            next_index = index + 1
        if article.article_id == article_id:
            curr_article = article
            previous_article = all_article[previous_index]
            next_article = all_article[next_index]
            break
    # curr_article = Article.objects.all()[curr_article - 1]
    section_list = curr_article.content.split('\n')
    return render(request, 'blog/detail.html', {
        'curr_article': curr_article,
        'section_list': section_list,
        'previous_article': previous_article,
        'next_article': next_article,
    })
