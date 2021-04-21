class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print(f'entrou no __init__')
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print('passou no __call__')
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
"""
    def process_template_response(self, request, response):
        print('passou no process_template_response')
        return Response({})"""