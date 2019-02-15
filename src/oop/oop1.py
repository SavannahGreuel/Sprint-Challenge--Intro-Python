# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Vehicle- base
class Vehicle:
    pass

# FlightVehicle(vehicle)
class FlightVehicle(Vehicle):
    pass

# Starship(FlightVehicle)
class Starship(FlightVehicle):
    pass

# Airplane(FlightVehicle)
class Airplane(FlightVehicle):
    pass

# GroundVehicle(vehicle)
class GroundVehicle(Vehicle):
    pass

# Car(GroundVehicle)
class Car(GroundVehicle):
    pass

# Motercycle(GroundVehicle)
class Motorcycle(GroundVehicle):
    pass


