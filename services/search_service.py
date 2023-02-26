from models.users import User


def perform_search(query):

    search_results_set = set()
    first_names = User.query.filter(User.first_name.ilike("%{}%".format(query))).all()
    last_names = User.query.filter(User.last_name.ilike("%{}%".format(query))).all()

    print(first_names)
    print(last_names)
    for fn in first_names:
        search_results_set.add(vars(fn))

    for ln in last_names:
        search_results_set.add(vars(ln))

    return list(search_results_set)
