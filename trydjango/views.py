from django.http import HttpResponse
from django.template.loader import render_to_string

from articles.models import Article


def home_view(request):
    # from the database
    article_obj = Article.objects.get(id=2)
    article_list = Article.objects.all()
    object_list = article_list #[102, 13, 342, 1331, 213]


    context = {
        "object_list": object_list,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content,
    }

    # Django templates
    # tmpl = get_template("home-view.html")
    # tmpl_string = tmpl.render(context=context)


    HTML_STR = render_to_string("home-view.html", context=context)
    #"""
    #<h1>{title} (id : {id})</h1>
    #<p>{content}</p>""".format(**context)


    return HttpResponse(HTML_STR)
