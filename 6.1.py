class UserAccount:
    def __init__(self, username, email, password):
        self.username = username  
        self.email = email        
        self.password = password  

    def set_password(self, new_password):
        self.password = new_password
        print("Пароль успешно изменён.")

    def check_password(self, password):
        return self.password == password

user_account = UserAccount("Yurka", "tata@gmail.com", "initialPassword")
user_account.set_password("newSecurePassword")
print(user_account.check_password("newSecurePassword"))
print(user_account.check_password("initialPassword"))