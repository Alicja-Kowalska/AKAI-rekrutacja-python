import operator

def word_rank(string):
    words = []
    rank = {}
    for line in string:
        sentence = line.split()
        for word in sentence:
            if word.isalpha():
                words.append(word.lower())

    for word in words:
        if word in rank:
            rank[word] += 1
        else:
            rank[word] = 1

    return sorted(rank.items(), reverse=True, key=operator.itemgetter(1))

sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]

list = word_rank(sentences)
for i in range(3):
    for j in range(len(list)):
        if list[j][1] == list[i][1]:
            print("Top", i + 1, ":", list[j][0], "\nLiczba wystąpień:", list[j][1])
    del list[j]
