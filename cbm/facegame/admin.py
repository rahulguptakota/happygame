from django.contrib import admin

# Register your models here.
from .models import scores
from .models import level1_happy
from .models import level2_happy
from .models import level3_happy
from .models import level1_else
from .models import level2_else
from .models import level3_else

admin.site.register(scores)
admin.site.register(level1_happy)
admin.site.register(level2_happy)
admin.site.register(level3_happy)
admin.site.register(level1_else)
admin.site.register(level2_else)
admin.site.register(level3_else)
