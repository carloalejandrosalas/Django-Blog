from django.contrib import admin
from .models import Question, Choice, Likes

# Register your models here.

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text', 'votes')
    # list_filter = ('choice_text',)


admin.site.register(Question)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Likes)