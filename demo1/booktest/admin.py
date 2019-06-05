from django.contrib import admin
from  .models import BookInfo,HeroInfo
# Register your models here.

class HeroInfoInlines(admin.StackedInline):
    model = HeroInfo
    extra = 1

class BookInfoAdmin(admin.ModelAdmin):
    list_dispaly = ('title','pub_date')
    list_per_page = 2
    list_filter = ('title','pub_date')
    search_fields = ('title',)
    inlines = [HeroInfoInlines]


class HeroInfoAdmin(admin.ModelAdmin):
    list_dispaly = ("name","content")
    list_per_page = 2
    list_filter = ("name","content")
    search_fields = ('name','content')


admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)
