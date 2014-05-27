from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from .menu import PollsMenu
from django.db import models

from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool

from django.contrib import admin
from cms.extensions import PageExtensionAdmin

from .models import IconExtension


class IconExtensionAdmin(PageExtensionAdmin):
    pass

admin.site.register(IconExtension, IconExtensionAdmin)



class IconExtension(PageExtension):
    image = models.ImageField(upload_to='icons')

extension_pool.register(IconExtension)


class PollsApp(CMSApp):
	name = _("Poll App")        # give your app a name, this is required
	urls = ["polls.urls"]       # link your app to url configuration(s)
	app_name = "polls-1"
	menus = [PollsMenu]          # this is the application namespace

apphook_pool.register(PollsApp) # register your app