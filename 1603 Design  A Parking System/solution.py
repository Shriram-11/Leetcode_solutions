'''Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed 
number of slots for each size.

Implement the ParkingSystem class:

ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class. The number of slots for each parking space
are given as part of the constructor.

bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants to get into the parking lot. 
carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively. A car can only park in a
parking space of its carType. If there is no space available, return false, else park the car in that size space and return true.'''


class ParkingSystem(object):

    # initialize a list with index 0,1,2 storing available parking space for big,medium and small respectively
    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.spaces = [big, medium, small]

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        # carType-1 matches the index of the particular carType in the list
        carType -= 1
        if self.spaces[carType] > 0:  # if space is available reduce it by 1 and return True
            self.spaces[carType] -= 1
            return True
        else:
            return False  # else return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
