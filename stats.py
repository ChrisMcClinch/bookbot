def get_num_words(file_contents):
    w = list(file_contents.split())
    return f"Found {len(w)} total words"

def char_count(file_contents):
    o = {}
    for char in file_contents:
        if char.lower() not in o:
            o[char.lower()] = 1
        else:
            o[char.lower()] += 1
    return o

def sorted_chars(cc):
    s = []
    counter = 0
    for i in cc:
        if i.isalpha():
            s.append([cc[i], counter, {i:cc[i]}])
            counter += 1
    s.sort(reverse=True)
    return [i[2] for i in s]