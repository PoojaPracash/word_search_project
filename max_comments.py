# This program outputs the person who tweeted the most


# A class to initialize dictionary and to perform basic functions
class DictInit:
    # Constructor
    def __init__(self):
        self.iDict = dict()

    # Function to add item to dictionary
    def addItem(self, x):
        if x in self.iDict:
            self.iDict[x] += 1
        else:
            self.iDict[x] = 1

        return self.iDict

    # Function to find max tweeted person
    def findMax(self, y):
        return [key for key in oDict if oDict[key] == max(oDict.values())]


if __name__ == '__main__':

    # create an object from class
    dictionary = DictInit()
    # Total number of test cases
    test_cases = int(input())
    # Final resultant list with max tweeted person's name
    Final_list = []

    for i in range(test_cases):
        tweet_num = int(input())
        for i in range(tweet_num):
            a = input().split()
            b = a[0].strip()
            oDict = dictionary.addItem(a[0])

        m = dictionary.findMax(oDict)

        for item in m:
            Final_list.append(item)

    for name in Final_list:
        print(name, "%d" % oDict[name])
