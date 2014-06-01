from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from .models import NewsPluginModel
from .models import News
from .models import NewsContentPluginModel


class NewsPlugin(CMSPluginBase):
	model = NewsContentPluginModel                 # Model where data about this plugin is saved
	name = _("News Plugin")                 # Name of the plugin
	render_template = "news/news.html"   # template to render the plugin with

	def render(self, context, instance, placeholder):
		context.update({'instance':instance})
		return context

plugin_pool.register_plugin(NewsPlugin) # register the plugin