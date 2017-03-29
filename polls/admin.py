from django.contrib import admin
from .models import Question
from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        (None,               {'fields': ['question_desc']}),
        ('Date information', {'fields': ['pub_date']}),
        ('Is Accept?', {'fields': ['isAccept']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')

admin.site.register(Question, QuestionAdmin)

# Register your models here.
