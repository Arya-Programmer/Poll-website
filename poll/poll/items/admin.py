from django.contrib import admin
from .models.answer_model import Answer
from .models.form_model import Form
from .models.question_model import Question

# Register your models here.


admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Form)
