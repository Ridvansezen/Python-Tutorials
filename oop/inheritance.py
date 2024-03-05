class Animal:
    def __init__(self, type_, age):
        self.type_ = type_
        self.age = age
        
    def behaviors(self, feeding, movement):
        self.feeding = feeding
        self.movement = movement
        
    def display_info(self):
        print(f"Hayvanın türü: {self.type_}")
        print(f"Yaşı: {self.age}")
        print(f"Beslenme şekli: {self.feeding}")
        print(f"Hareket şekli: {self.movement}")

class Bird(Animal):
    def __init__(self, type_, age, feather_color, wing_width):
        super().__init__(type_, age)
        self.feather_color = feather_color
        self.wing_width = wing_width
        
    def behaviors(self, feeding, movement, flying, chirping):
        super().behaviors(feeding, movement)
        self.flying = flying
        self.chirping = chirping
        
    def display_info(self):
        super().display_info()
        print(f"Tüy rengi: {self.feather_color}")
        print(f"Kanat genişliği: {self.wing_width}")
        print(f"Uçma durumu: {self.flying}")
        print(f"Ötme durumu: {self.chirping}")


bird = Bird("Kuş", 6, "Gri", "1.50 metre")
bird.behaviors("Böceklerle beslenir", "Uçar", "Evet", "Evet")
bird.display_info()