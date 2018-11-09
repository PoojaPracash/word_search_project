import os
from django.http import HttpResponse
from django.template import loader
from django.conf import settings
from django.shortcuts import render
import csv
from mybrowser.mysearch import Trie


def submit(request):
    template = loader.get_template("searchengine/search.html")
    return HttpResponse(template.render())


def read_my_file(request):
    file_ = open(os.path.join(settings.PROJECT_ROOT, 'word_search.tsv'))
    path_list = []
    rev_list = []
    trie = Trie()
    with open(file_) as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter="\t")
        for line in tsvreader:
            path_list.append(line[0])
    for w_search in path_list:
        trie.add(w_search)
    # word = input("Enter word to be searched: ")
    start_list = trie.start_with_prefix(word)

    if (len(start_list) < 25):
        trie1 = Trie()
        for w in path_list:
            rev_word = trie1.reverseWord(w)
            trie1.add(rev_word)
        # reversed_word = [trie1.reverseWord(word) for word in path_list]
        rev_word = trie1.reverseWord(word)
        rev_list = trie1.start_with_prefix(rev_word)
        end_list = [trie1.reverseWord(w) for w in rev_list]
        for i in end_list:
            if i not in end_list:
                end_list.append(i)

        return render(request, 'startsearch.html', {'list': end_list})
