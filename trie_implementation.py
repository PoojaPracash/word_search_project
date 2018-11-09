import csv


class Node:
    def __init__(self, label=None, data=None):
        self.label = label
        self.data = data
        self.children = dict()

    def addChild(self, key, data=None):
        if not isinstance(key, Node):
            self.children[key] = Node(key, data)
        else:
            self.children[key.label] = key

    def __getitem__(self, key):
        return self.children[key]


class Trie:
    def __init__(self):
        self.head = Node()

    def __getitem__(self, key):
        return self.head.children[key]

    def add(self, word):
        current_node = self.head
        word_finished = True

        for i in range(len(word)):
            if word[i] in current_node.children:
                current_node = current_node.children[word[i]]
            else:
                word_finished = False
                break

        # For ever new letter, create a new child node
        if not word_finished:
            while i < len(word):
                current_node.addChild(word[i])
                current_node = current_node.children[word[i]]
                i += 1

        # Let's store the full word at the end node so we don't need to
        # travel back up the tree to reconstruct the word
        current_node.data = word

    def has_word(self, word):
        if word == '':
            return False
        if word is None:
            raise ValueError('Trie.has_word requires a not-Null string')

        # Start at the top
        current_node = self.head
        exists = True
        for letter in word:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                exists = False
                break

        # Still need to check if we just reached a word like 't'
        # that isn't actually a full word in our dictionary
        if exists:
            if current_node.data is None:
                exists = False

        return exists

    def start_with_prefix(self, prefix):
        """ Returns a list of all words in tree that start with prefix """
        words = list()
        if prefix is None:
            raise ValueError('Requires not-Null prefix')

        # Determine end-of-prefix node
        top_node = self.head
        for letter in prefix:
            if letter in top_node.children:
                top_node = top_node.children[letter]
            else:
                # Prefix not in tree, go no further
                return words

        # Get words under prefix
        if top_node == self.head:
            queue = [node for key, node in top_node.children.items()]
        else:
            queue = [top_node]

        # Perform a breadth first search under the prefix
        # A cool effect of using BFS as opposed to DFS is that BFS will return
        # a list of words ordered by increasing length
        while queue:
            current_node = queue.pop()
            if current_node.data is not None:
                # Isn't it nice to not have to go back up the tree?
                words.append(current_node.data)

            queue = [node for key, node in current_node.children.items()] + queue

        return words

    def getData(self, word):
        """ This returns the 'data' of the
        node identified by the given word """
        if not self.has_word(word):
            raise ValueError('{} not found in trie'.format(word))

        # Traverse to the bottom of the tree and get the data
        current_node = self.head
        for letter in word:
            current_node = current_node[letter]

        return current_node.data

    def reverseWord(self, word):
        return word[::-1]


if __name__ == '__main__':
    """ Example use """
    trie = Trie()
    path_list = []
    rev_end_list = []
    with open("word_search3.csv") as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter="\t")
        for line in tsvreader:
            path_list.append(line[0])

    for word in path_list:
        trie.add(word)
        # word = input("Enter word to be searched: ")
    end_list = trie.start_with_prefix('ing')
        # create a trie with reversed words to check if word ends with search word
    if (len(end_list) < 25):
        trie1 = Trie()
        for w in path_list:
            rev_word = trie1.reverseWord(w)
            trie1.add(rev_word)
        rev_end_list = trie1.start_with_prefix('gni')
        rev_end_list1 = [trie1.reverseWord(w) for w in rev_end_list]
        for i in rev_end_list1:
            if i not in end_list:
                end_list.append(i)
        print(end_list)
