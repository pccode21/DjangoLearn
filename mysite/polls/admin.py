from django.contrib import admin
from .models import FigureModel

# Register your models here.
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):  # TabularInline使相关对象将以更紧凑的基于表格的格式显示
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
                (None, {'fields': ['question_text']}),
                ('Date information', {'fields': ['pub_date']})
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
admin.site.register(FigureModel)
