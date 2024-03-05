class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password
        
        
    def get_password(self):        
        return self.__password
    
    def change_password(self, new_password):
        self.__password = new_password
        
    def show_info(self):
        print(f"Kullanıcı adı: {self.username}\nE-Mail adresi: {self.email}")


user = User("testuser", "test@gmail.com", "Şifre123")
user.show_info()
user.get_password()
user.change_password("1234")
user.get_password()


