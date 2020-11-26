

def validate(request, model):
    try:
        from urllib.parse import unquote

        body = request.body.decode('utf-8')
        body = unquote(body)
        body = str(body).replace('&', '\', \'').replace('=', '\':\'').replace("+", " ")
        body = eval("{'" + body + "'}")

        text = dict()
        num = 1
        for question in model.questions.all():
            if question.type == "MultiChoice":
                found = False
                for _ in range(len(question.answers.all())):
                    try:
                        text[question.title + str(num)] = body[question.title + str(num)]
                        num += 1
                    except KeyError:
                        continue
                    found = True
                if found != True:
                    return "Please Fill All The Fields"

            else:
                text[question.title] = body[question.title]


    except KeyError:
        return "Please Fill All The Fields"
    return text




def getIp(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    import socket

    try:
        socket.inet_aton(ip)
        ip_valid = True
    except socket.error:
        ip_valid = False
    return ip, ip_valid