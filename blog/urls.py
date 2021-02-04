from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('',include("blog.url")),
	path('admin/',admin.site.urls),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)