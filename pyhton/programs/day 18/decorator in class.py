#decorator in class

class person:
    def __init__(self,name):
        self.name = name

    def about_me(self):
        print("I am ", self.name)

    @staticmethod
    def speak(msg):
        print(msg)

ans=person("ans")
ans.about_me()
person.speak("hiiii")
ans.speak("helloo")

        
