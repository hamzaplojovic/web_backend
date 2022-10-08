def validate_user_data(request):
    requirements = ["username", "password", "full_name", "email", "github", "job"]
    checked = []
    for x in requirements:
        if len(str(request[x]))>1:
            checked.append(x)
    return 200 if len(checked)==6 else 404