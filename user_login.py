class User:
    def __init__(self):
        self.name = ''
        self.email = ''
        self.password = ''
        self.logged_in = False

    def login(self):
        email = input("Enter your Email: ")
        password = input("Enter Password: ")

        if email == self.email and password == self.password:
            self.logged_in = True
            print("Login Successful!")
        else:
            print("Login Failed!")

    def logout(self):
        self.logged_in = False
        print("Logged Out!")

    def is_logged_in(self):
        return self.logged_in

    def profile(self):
        if self.is_logged_in():
            print(self.name, "\n", self.email)
        else:
            print("User is not logged in!")

user1 = User()
user1.name = "Allen Masud"
user1.email = "masud@befairgroup.com"
user1.password = "12345"


user1.login()

if user1.is_logged_in():
    user1.profile()
else:
    print("Profile not available because the user is not logged in.")
