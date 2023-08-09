class Battery:
    def __init__(self, capacity):
        self.capacity = capacity

    def increase_capacity(self, amount):
        self.capacity += amount

    def decrease_capacity(self, amount):
        self.capacity -= amount

class Mobile:
    def __init__(self, name, color, price, battery_capacity):
        self.name = name
        self.color = color
        self.price = price
        self.battery = Battery(battery_capacity)

    def calls(self, duration):
        self.battery.decrease_capacity(duration)

    def netflix(self, hours):
        self.battery.decrease_capacity(hours)

    def games(self, hours):
        self.battery.decrease_capacity(hours)

    def plug_into_charge(self):
        self.battery.increase_capacity(10)  # Assuming 10 units of battery capacity are gained when charging.

my_mobile = Mobile("Example Phone", "Black", 500, 100)
print("Initial battery capacity:", my_mobile.battery.capacity)

my_mobile.calls(2)
print("Battery capacity after calls:", my_mobile.battery.capacity)

my_mobile.netflix(3)
print("Battery capacity after watching Netflix:", my_mobile.battery.capacity)

my_mobile.games(1)
print("Battery capacity after playing games:", my_mobile.battery.capacity)

my_mobile.plug_into_charge()
print("Battery capacity after charging:", my_mobile.battery.capacity)        
