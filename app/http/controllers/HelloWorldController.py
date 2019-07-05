"""A HelloWorldController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller


class HelloWorldController(Controller):
    """HelloWorldController Controller Class."""

    def __init__(self, request: Request):
        """HelloWorldController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View):
        """ Show Hello World Template """
        return view.render('helloworld')
