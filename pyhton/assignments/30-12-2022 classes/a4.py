class StringManipulation:
    def __init__(self,wlist):
        self.wlist=wlist
        print (wlist)

    def Words_of_length(self,length):
        l=[]
        for i in self.wlist:
            if len(i) == length:
                l.append(i)
        return l
        
    def Words_starts_with(self,char):
        l=[]
        for i in self.wlist:
            if i[0] == char:
                l.append(i)
        return l
        
    def Words_ends_with(self,char):
        l=[]
        for i in self.wlist:
            if i[-1] == char:
                l.append(i)
        return l
    
    def Palindromes(self):
        l=[]
        for i in self.wlist:
            if i == i[::-1]:
                l.append(i)
        return l
    
    def Total_words(self):
        return len(self.wlist)

    def Longest_word(self):
        lw=self.wlist[0]
        for i in self.wlist[1:]:
            if len(i) > len(lw):
                lw=i
        return lw

    def Smallest_word(self):
        lw=self.wlist[0]
        for i in self.wlist[1:]:
            if len(i) < len(lw):
                lw=i
        return lw
    
    def Count(self,word):
        return self.wlist.count(word)




word = input("enter the text : ")
s = StringManipulation(word.split(' '))
print(s.Words_of_length(6))
print(s.Words_starts_with('s'))
print(s.Words_ends_with('l'))
print(s.Palindromes())
print(s.Total_words())
print(s.Longest_word())
print(s.Smallest_word())
print(s.Count('it'))



