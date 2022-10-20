# file name: name_function.py
def get_formatted_name(first, middle ,last, ):  # Gera um nome completo formatado de modo elegante.
    full_name = first + ' ' + last
    return full_name.title()


#function v2
def get_formatted_name1(first, last, middle=''):  # Gera um nome completo formatado de modo elegante.
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()