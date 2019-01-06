from django.contrib import admin
from .models import User
from .models import Character
from .models import UserAndCharacterLink
from .models import BattleResult
from .models import Skill

# Register your models here.


admin.site.register(User)
admin.site.register(Character)
admin.site.register(UserAndCharacterLink)
admin.site.register(BattleResult)
admin.site.register(Skill)

