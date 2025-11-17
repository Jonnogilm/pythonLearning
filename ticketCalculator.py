class Ticket:
    def __init__ (self, price, serial_number):
        self.price = price
        self.serial_number = serial_number

    def calculate_total(self, quantity):
        return self.price * quantity
    
    def is_ticket(self):
        if self.serial_number.endswith("0110"):
            return True
        else:
            return False
        
    def climate_impact(self):
        about_climate = "The impact of ticket production on climate change is significant due to resource consumption and emissions."
        return about_climate
    
    
ticket = Ticket(10, "A123450110")
total = ticket.calculate_total(5)  # Calling the method
print(f"Total ticket price for 5 tickets: {total}"+"USD")
print(f"Is valid ticket: {ticket.is_ticket()}")
print(ticket.climate_impact())
