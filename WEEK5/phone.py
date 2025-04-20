class Smartphone:
    # Constructor to initialize the attributes
    def __init__(self, brand, model, battery_level):
        self.brand = brand  # brand of the smartphone
        self.model = model  # model of the smartphone
        self.battery_level = battery_level  # battery level from 0 to 100
    
    # Method to charge the phone
    def charge(self):
        if self.battery_level < 100:
            self.battery_level += 20
            if self.battery_level > 100:
                self.battery_level = 100
            print(f"Charging... Battery is now {self.battery_level}%")
        else:
            print("Battery is already full!")
    
    # Method to use the phone, which drains the battery
    def use(self):
        if self.battery_level > 0:
            self.battery_level -= 10
            print(f"Using the phone... Battery is now {self.battery_level}%")
        else:
            print("Battery is empty, please charge your phone!")

    # Method to display the phone's status
    def status(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Battery: {self.battery_level}%")
