from articles.models import Category, Tag

class getCategoriesAndTagsAction:
    @staticmethod
    def execute():
        cats = Category.objects.all()
        tags = Tag.objects.all()
        return (cats,tags,)