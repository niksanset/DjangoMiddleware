def user_groups(request):
    if request.user.is_authenticated:
        return {'user_groups': request.user_groups}
    else:
        return {'user_groups': 'Авторизуйтесь'}