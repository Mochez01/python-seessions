from phone import Smartphone
if __name__ == "__main__":
    # Create an instance of the Smartphone class
    my_phone = Smartphone("Apple", "iPhone 12", 50)

    # Check the initial status
    my_phone.status()

    # Charge the phone
    my_phone.charge()

    # Use the phone
    my_phone.use()

    # Check the status again
    my_phone.status()