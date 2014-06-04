"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

# from xblock.fields import Integer, Scope, String, Any, Boolean, Dict
from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment
import paellaservers


class paellaXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.
    server = String(display_name="server",
                  default="http://matterhorn.cc.upv.es:8080/paella3.0/ui/embed.html?server=&id=",
                  scope=Scope.content,
                  help="Server with the Paella Player")

    video_id = String(display_name="id",
                  default="e2af6698-59cf-479c-90b8-f8900d403ef9",
                  scope=Scope.content,
                  help="Id of the Paella Video")

    display_name = String(display_name="Display Name",
                          default="Paella Video",
                          scope=Scope.settings,
                          help="Name of the component in the edxplatform")

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    @XBlock.json_handler
    def save_paella(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        #assert data['hello'] == 'world'
        self.server = data['server']
        self.video_id = data['video_id']
        self.display_name = data['display_name']

        return {
            'result': 'success',
        }

    def student_view(self, context=None):
        """
        The primary view of the paellaXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/paellavideo.html")
        frag = Fragment(html.format(self=self))
        return frag



    # TO-DO: change this view to display your data your own way.
    def studio_view(self, context=None):
        html = self.resource_string("static/html/paellavideo_edit.html")

        options = "<option value=''  >----</option>"
        for key in paellaservers.PAELLASERVERS:
            if self.server ==key['url']:
                options = options + "<option value='" + key['url'] + "' selected='selected' >" + key['name'] + "</option>"
            else:
                options = options + "<option value='" + key['url'] + "' >" + key['name'] + "</option>"

        selector=u"""
            <script type="text/template" id="xblock-equality-template">
            </script>
            <select name='Server' id='edit_server'>
            {}
            </select>""".format(options)

        frag = Fragment(html.format(self=self,selector=selector))
        frag.add_javascript(self.resource_string("static/js/src/paellavideo.js"))
        frag.initialize_js('paellaXBlock')
        return frag

    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("paellaXBlock",
             """<vertical_demo>
                <paellavideo/>
                </vertical_demo>
             """),
        ]