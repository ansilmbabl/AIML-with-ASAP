"""
Write a class UserLoginInfo that has two variables: 
UserName that contains the
username 
old_passwords : a list that holds the history of the user’s passwords.
The last item of the old_passwords is the user’s current password.
Object creation format 1 u1 = UserLoginInfo(Username,Password)
At the time of object creation Username assign to UserName and Password will be
added in to old_passwords list without check any validation.
Rules for valid passwords are: 
Length of password should be greater than 7
The first character should be a letter and in upper case 
The remaining
characters are either numbers or letters or a combination of both.
The class UserLoginInfo should have the following methods:
RetrievePassword that returns the current password of the user.
ChangePassword(New_Password) that receives a string New_Password and updates
the user’s current password with New_Password . 
The ChangePassword the method
should only change the password if the New_Password is a valid password that is
different from the all of the user’s old passwords .
If this operation is successful, return the message Password updated successfully 
If New_Password is exists in the list of old_passwords , then return
the message Password already used . 
if New_Password is not a valid password
then return the message Invalid password
Login(Username, Password)
that receives strings UserName and Password and returns a message
Welcome Username if the Username and Password are matched to the current
username and current password respectively, otherwise, return
Username or Password incorrect message.
"""

class userloginfo:
    
    def __init__(self,username,passw):
        self.username = username
        self.old_passw = [passw]
        
    def check_pass(self,pwd):
        if len(pwd)<8:
            return False
        elif pwd[0].isalpha()==False or pwd[0].isupper()==False:
            return False
        elif pwd.isalnum()==False:
            return False
        else:
            return True
    
    def change_pass(self,newpass):
        if newpass in self.old_passw:
            return "password already used"
        else:
            if self.check_pass(newpass) == True:
                self.old_passw.append(newpass)
                return "password updated succesfully"
            else:
                return "invalid password"

    def retrieve_pass(self):
        return self.old_passw[-1]

    def login(self,user,pwd):
        if pwd == self.old_passw[-1] and user == self.username:
            return "welcome " + self.username
        else:
            return "user name or password incorrect"


ans=userloginfo("ans","Ansil123456")
print(ans.check_pass("Ansil123456"))
print("Ansil123456: ",ans.change_pass("Ansil123456"))
print(ans.check_pass("Ansil123456789"))
print("Ansil123456789: ",ans.change_pass("Ansil123456789"))
print("last password: ",ans.retrieve_pass())
print(ans.login("ansil","Ansil123456789"))
print(ans.login("ans","Ansil12345678900"))
print(ans.login("ans","Ansil123456789"))



        
        
        



        
        
        
