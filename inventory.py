class Inventory:
    def __init__(self):
        self.gear = []
        self.ammo = {
            'pistol': 0,
            'rifle': 0,
            'shotgun': 0
        }

    def add_gear(self, gear):
        self.gear.append(gear)

    def add_ammo(self, ammo_type, amount):
        if ammo_type in self.ammo:
            self.ammo[ammo_type] += amount
