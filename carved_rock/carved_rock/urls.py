from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
<<<<<<< HEAD
=======
from django.conf import settings
from django.conf.urls.static import static
>>>>>>> fa9bec0 (fifth commit)

import debug_toolbar

urlpatterns = [
    path('', TemplateView.as_view(template_name="store/index.html"), name="index"),
    path('store/', include('store.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)), # Debug toolbar
<<<<<<< HEAD
]
=======
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# The part after the + allows serving uploaded images
# Don't do this in production! See https://docs.djangoproject.com/en/3.1/howto/static-files/#serving-files-uploaded-by-a-user-during-development
>>>>>>> fa9bec0 (fifth commit)
