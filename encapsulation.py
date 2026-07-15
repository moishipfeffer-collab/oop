class UserProfile:
    def __init__(self,username):
        self.__username=username
    @property
    def username(self):
        return self.__username
m=UserProfile("moishi")
print(m.username)
n=UserProfile("rachel")
n.__username="moishi"

#2
class UserProfile:
    def __init__(self,username,email):
        self.__username=username
        self.__email=email
    @property
    def username(self):
        return self.__username
    @property
    def email(self):
        return self.__email
m=UserProfile("moishi","moishipfeffer@gmail.com")
print(m.email)
print(m.username)

#3
class UserProfile:
    def __init__(self,username):
        self.__username=username
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self,new_name):
        if len(new_name)>=3:
            self.__username=new_name
        else:
            print("Username too short")
m=UserProfile("moishi")
m.username="mk"
print(m.username) 
m.username="rachel" 
m.__username="moi"
print(m.__dict__)

#4
class UserProfile:
    def __init__(self,username):
        self.username=username
        self.__followers=0
    @property
    def followers(self):
        return self.__followers
    def follow(self):
        self.__followers+=1
    def unfollow(self):
        if self.__followers > 0:
            self.__followers-=1
n=UserProfile("moishi")
n.follow()
n.follow()
n.follow()
n.unfollow()
print(n.followers)

#5
class UserProfile:
    def __init__(self,username,bio):
        self.username=username
        self._bio=bio
    @property
    def bio(self):
        return self._bio
class VerifiedUser(UserProfile):
    def __init__(self, username, bio,badge):
        super().__init__(username, bio)
        self.badge=badge
    def full_UserProfile(self):
        print(f"{self.username} [{self.badge}]: {self._bio}")
c=VerifiedUser("celeb","singer and songwriter","V")
c.full_UserProfile()

#6
class UserProfile:
    def __init__(self,username,age):
        self.username=username
        self.__age=age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,new_age):
        if 13<=new_age<=120:
            self.__age=new_age
        else:
            print(f"Invalid age.")
p = UserProfile("dan", 18)
p.age = 10
p.age = 200
p.age = 25
print(f"age: {p.age}")
p.__age=20
print(p.__dict__)

#7
class UserAccount:
    def __init__(self,username,password):
        self.username=username
        self.__password=password
    def check_password(self,attempt):
        return attempt == self.__password
    def change_password(self,old,new):
        if old==self.__password:
            self.__password=new
            print("Password changed")
        else:
            print(f"Incorrect old password")
m=UserAccount("admin", "secret")
print(m.check_password("wrong"))
m.change_password("secret", "new123")
print(m.check_password("new123"))

#8
class Post:
    def __init__(self,author, content):
        self.author=author
        self.content=content
        self.__likes = 0
        self.__liked_by = []
    @property 
    def likes(self):
        return self.content
    def like(self,username):
        if username not in self.__liked_by:
            self.__liked_by.append(username)
            self.__likes+=1
    def unlike(self,username):
        if username in self.__liked_by:
            self.__liked_by.remove(username)
            self.__likes-=1
    def status(self):
        print(f"Post by {self.author}: {self.__likes} likes")
b=Post("moishi","hello!")
b.like("nati")
b.like("chaim")
b.like("penelope")
b.unlike("nati")
b.like("penelope")
b.status()

#9
class UserProfile:
    def __init__(self,username):
        self.__is_public=True
        self.__show_email=False
        self.__show_age=False
    @property
    def public(self):
        return self.__is_public
    @public.setter
    def public(self,field):
        if type(field)==bool:
            self.__is_public = field
        else:
            print("field must be True or False!")
    @property
    def email(self):
        return self.__show_email
    @email.setter
    def email(self,field):
        if type(field)==bool:
            self.__show_email = field
        else:
            print("field must be True or False!")
        
    @property
    def age(self):
        return self.__show_age
    @age.setter
    def age(self,field):
        if type(field)==bool:
            self.__show_age = field
        else:
            print("{field} must be True or False!")
    def privacy_summary(self):
        print(f"public: {self.public}")
        print(f"sow email: {self.email}")
        print(f"show age: {self.age}")
b1=UserProfile("moishi")
b1.email=True
b1.public="yes"
b1.privacy_summary()

#10
class UserAccount:
    def __init__(self,username,email,password,age):
        self.__username=username
        self.__email=email
        self.__password=password
        self.__age=age
        self._login_count=0
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self,new_usewname):
        if len(new_usewname)>=3:
            self.__username=new_usewname
        else:
            print("username must be atleast 3 chars.")
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,new_email):
        if "@" in new_email:
            self.__email=new_email
        else:
            print("email nut enclood @")
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,new_age):
        if 120>=new_age>=13:
            self.__age=new_age
        else:
            print(f"age must be between 13 and 120")
    def check_password(self,attempt):
        return attempt == self.__password
    def change_password(self,old,new):
        if old == self.__password:
            self.__password=new
        else:
            ("old password not right.")
    def login(self,password):
        if password == self.__password:
            self._login_count+=1
            print("welcome!")
        else:
            print("login faild")
    def account_summary(self):
        print(f"username: {self.__username} | email: {self.__email} | age: {self.__age} | login: {self._login_count} times")
rachel=UserAccount("user1", "u@mail.com", "pass123", 20)
rachel.login(123)
rachel.login(190)
rachel.login("pass123") 
rachel.email="moishi@"
rachel.age=120
rachel.account_summary()


    

    







        