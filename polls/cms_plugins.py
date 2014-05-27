from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from .models import PollPluginModel
from .models import Hello


class PollPlugin(CMSPluginBase):
	model = PollPluginModel                 # Model where data about this plugin is saved
	name = _("Poll Plugin")                 # Name of the plugin
	render_template = "polls/plugin.html"   # template to render the plugin with

	def render(self, context, instance, placeholder):
		context.update({'instance':instance})
		return context

plugin_pool.register_plugin(PollPlugin) # register the plugin


class HelloPlugin(CMSPluginBase):
	model = Hello
	render_template = "polls/hello_plugin.html"
plugin_pool.register_plugin(HelloPlugin)