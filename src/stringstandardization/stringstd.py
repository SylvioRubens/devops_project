from unidecode import unidecode


def standardize(text):
    return unidecode(text)


name = 'Sylvio Rúbens'

std_name = standardize(name)
print(std_name)
