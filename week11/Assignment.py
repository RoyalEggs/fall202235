class Package:
    def __init__(self, name):
        self.name = name
    def dropOff(self, driver):
        print(f"Delivered {self.name} by {driver}")

class AmazonTruck:
    packages = []
    driver = "nobody"

    def load(self, package):
        self.packages.append(package)   # add the package to the truck

    def deliver(self):
            for package in self.packages:
                package.dropOff(self.driver)

xbox = Package("xbox")
tshirt = Package("tshirt")
blades = Package("rollerblades")

truck = AmazonTruck()
truck.driver = "Fandango"
truck.load(xbox)
truck.load(tshirt)
truck.load(blades)

truck.deliver()