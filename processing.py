def pr(data):
    data = data.replace('.', '')
    data = data.replace(',', '')
    data = data.replace("'", "")
    data = data.replace('.', '')
    data = data.replace(' ', '')
    data = data.replace('!', '')
    data = data.replace('?', '')
    data = data.lower()
    return data