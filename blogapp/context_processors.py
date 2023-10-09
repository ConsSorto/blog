from blogapp.models import Category, Article


def get_categories(request):
    cartegories_use = Article.objects.values_list(
        'categories').distinct()

    categories = Category.objects.values_list(
        'id', 'name').filter(id__in=cartegories_use).order_by('name')
    return {'categories': categories}
