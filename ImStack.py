#EXERCISE NO. 6 - STACK
#Ellene Gay S. Daniel

class ImStack:
    def __init__(self):
        self.items = ["Scrarlet Heart(Moon Lovers)",
                      "Weightlifting Fairy Kim Bok Joo",
                      "Goblin",
                      "Strong Woman Do Bong Soon",
                      "Reply 1988 (2016)",
                      "My Suspicious Partner",
                      "While You Were Sleeping",
                      "Cinderella and Four Knights",
                      "Fignt for my Way",
                      "Playful Kiss",
                      "Healer",
                      "The Heirs",
                      "I am not a Robot",]
        self.items2 = sorted(self.items)  #to peek the sorted items in the original list
        self.items3 = self.items2[::-1]   #to peek the reversed original list

    def sort(self):
        return sorted(self.items2)
    def reverse(self):
        return self.items2[::-1]
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peekname(self):
        return self.items3[len(self.items)-1]
    def peeknamenext(self):
        return self.items3[len(self.items)-2]
    def peektime(self):
        return self.items[len(self.items)-1]
    def peektimenext(self):
        return self.items[len(self.items)-2]
    def size(self):
        return len(self.items)




if __name__ == "__main__":
    dan = ImStack()
    print "Welcome to Korean Drama"
    print "KDrama has",dan.size(),"Dramas"
    x = input("Sort by:\n1. Name(A-Z)\n2.Time(new-old)\n\tEnter your choice: ")
    if x == 1:
        while dan.size() >= 2:
            print "Currently playing ",dan.peekname()
            print "Next Kdrama is ",dan.peeknamenext(), "\n - - - - - - - - - - - - - - - - - - "
            dan.pop()
    elif x == 2:
        while dan.size() >= 2:
            print "Now Watching ",dan.peektime()
            print "Next KDrama is ", dan.peektimenext(), "\n - - - - - - - - - - - - - - - - - - "
            dan.pop()
    else:
        print "INVALID SORTING"
        



