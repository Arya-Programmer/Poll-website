def staticing(query, form):
    stats = dict()
    for question in form.first().questions.all():
        if question.type != "Text":
            stats[question.title] = {answer.title: 0 for answer in question.answers.all()}
        else:
            stats[question.title] = []

    for user in query:
        user_answers = eval(user.answers)

        for key, value in dict(user_answers).items():
            if key[-1].isdigit():
                stats[key[:-1]][value] += 1

            elif isinstance(stats[key], list):
                stats[key].append(value)

            elif not isinstance(stats[key], list):
                stats[key][value] += 1

    return stats
