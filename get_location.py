import sys

try:
    import os
    from platform import system
    from pyfiglet import figlet_format
    from termcolor import colored
    from geopy.geocoders import Nominatim
    from geopy import distance
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!]Press Any Key To Exit...", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


class Location:
    def __init__(self, location=None) -> None:
        self.location = location
        self.geocoder = Nominatim(user_agent="I know python")

    def latitude(self) -> float:
        try:
            location = self.geocoder.geocode(self.location)
            return location.latitude
        except Exception as e:
            print(colored(e, color="red"))
            sys.exit()

    def longitude(self) -> float:
        try:
            location = self.geocoder.geocode(self.location)
            return location.longitude
        except Exception as e:
            print(colored(e, color="red"))
            sys.exit()

    def Address(self):
        try:
            location = self.geocoder.geocode(self.location)
            return location.address
        except Exception as e:
            print(colored(e, color="red"))
            sys.exit()

    def Distance(self, first_location: str, second_location: str):
        try:
            location1 = self.geocoder.geocode(first_location)
            location2 = self.geocoder.geocode(second_location)
            first, second = (location1.latitude, location1.longitude), (location2.latitude, location2.longitude)
            return distance.distance(first, second)
        except Exception as e:
            print(colored(e, color="red"))
            sys.exit()


if __name__ == '__main__':
    clear()
    print()
    print(colored(figlet_format("Location"), color="blue"))
    print("\n")
    print(colored("""
[1] Get Latitude
[2] Get Longitude
[3] Get Address
[4] Get Distance
[99] Exit  
""", color="blue"))
    try:
        mode = int(input(colored("[?]MODE >", color="blue")))
        print("\n")
        if mode == 1:
            location_ = input(colored("[+]Location >", color="blue"))
            region = Location(location=location_)
            print(colored(f"[-]The Latitude is : {region.latitude()}", color="blue"))
        elif mode == 2:
            location_ = input(colored("[+]Location >", color="blue"))
            region = Location(location=location_)
            print(colored(f"[-]The Longitude is : {region.longitude()}", color="blue"))
        elif mode == 3:
            location_ = input(colored("[+]Location >", color="blue"))
            region = Location(location=location_)
            print(colored(f"[-]The Address is : {region.Address()}", color="blue"))
        elif mode == 4:
            firstLocation = input(colored("[+]First Location >", color="blue"))
            secondLocation = input(colored("[+]Second Location >", color="blue"))
            region = Location()
            print(colored(f"[-]The Distance is {region.Distance(firstLocation, secondLocation)}", color="blue"))
        elif mode == 99:
            sys.exit()
        else:
            print(colored("[!]Choose 1, 2, 3, 4 or 99", color="red"))
            sys.exit()
    except ValueError as er:
        print(colored(er, color="red"))
        sys.exit()

