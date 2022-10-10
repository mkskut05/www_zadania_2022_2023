from django.contrib import admin
from .models import Question, Choice, Answer

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "pub_date")
    list_filter = ("question_text", "pub_date")
    search_fields = ("question_text", "pub_date")


admin.site.register(Question, QuestionAdmin)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("question", "choice_text", "votes")
    search_fields = ("question", "choice_text")


admin.site.register(Choice, ChoiceAdmin)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ("question", "is_open")
    seatch_fields = "question"
    ordering = ("question",)


admin.site.register(Answer, AnswerAdmin)