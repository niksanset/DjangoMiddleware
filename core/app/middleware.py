class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            print('user')
            request.user_groups = list(request.user.groups.values_list('name', flat=True))
            print(request.user_groups)
        return response