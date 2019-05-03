import algorithm.myapplication as myapp


def analysis(text):
    temp = myapp.client.lexer(text)

    lists = [{}]
    counter = 0

    for word in temp.get('items'):
        if word.get('item') == '，' or word.get('item') == '。':
            continue
        if word.get('ne') == '':
            if 'ISSUE' in lists[counter]:
                lists[counter]['ISSUE'] += word.get('item')
            else:
                lists[counter]['ISSUE'] = word.get('item')
            continue
        if word.get('ne') == 'TIME':
            part = {}
            lists.append(part)
            counter += 1
            lists[counter]['TIME'] = word.get('item')
        else:
            if word.get('ne') in lists[counter]:
                lists[counter][word.get('ne')] += ','
                lists[counter][word.get('ne')] += word.get('item')
            else:
                lists[counter][word.get('ne')] = word.get('item')
    i = 0
    while i < lists.__len__():
        if lists[i].__len__() == 0:
            lists.__delitem__(i)
        i += 1

    return lists
