from phone import Smartphone  # Importing the Smartphone class from phone module
class Tablet(Smartphone):
    # Constructor to initialize the attributes (same as Smartphone)
    def __init__(self, brand, model, battery_level, screen_size):
        super().__init__(brand, model, battery_level)  # Initialize the parent class
        self.screen_size = screen_size  # Additional attribute for Tablet
    
    # Overriding the use method to have a different behavior for Tablets
    def use(self):
        if self.battery_level > 0:
            self.battery_level -= 5  # Tablets use less battery than phones
            print(f"Using the tablet... Battery is now {self.battery_level}%")
        else:
            print("Battery is empty, please charge your tablet!")
    
    # Method to display the tablet's status
    def status(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Screen Size: {self.screen_size} inches, Battery: {self.battery_level}%")