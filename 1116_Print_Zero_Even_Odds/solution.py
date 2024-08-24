from threading import Semaphore

class ZeroEvenOdd(object):
    """
    A class that synchronizes the printing of numbers in a specific sequence:
    zeroes, then even numbers, and then odd numbers. The printing must follow
    the sequence: 0, 1, 0, 2, 0, 3, ... where zero is printed before every 
    even or odd number.

    The class uses semaphores to control the printing sequence and ensure 
    proper synchronization between threads.

    Attributes:
        n (int): The maximum number to print.
        e (Semaphore): Semaphore to manage access to printing even numbers.
        o (Semaphore): Semaphore to manage access to printing odd numbers.
        z (Semaphore): Semaphore to manage access to printing zeroes.
        turn (int): Indicator for which type of number should be printed next.
    """

    def __init__(self, n):
        """
        Initializes the ZeroEvenOdd instance.

        :param n: The maximum number to print.
        :type n: int
        """
        self.n = n
        self.e = Semaphore(0)  # Semaphore for even numbers
        self.o = Semaphore(0)  # Semaphore for odd numbers
        self.z = Semaphore(1)  # Semaphore for zeroes
        self.turn = 1

    def zero(self, printNumber):
        """
        Prints zeroes and releases semaphores for even or odd numbers.

        :param printNumber: Method to print the number.
        :type printNumber: method
        """
        for i in range(1, self.n + 1):
            self.z.acquire()  # Acquire semaphore for zero
            printNumber(0)    # Print zero
            if i % 2 == 0:
                self.e.release()  # Release semaphore for even numbers
            else:
                self.o.release()  # Release semaphore for odd numbers

    def even(self, printNumber):
        """
        Prints even numbers and releases semaphore for zeroes.

        :param printNumber: Method to print the number.
        :type printNumber: method
        """
        for i in range(2, self.n + 1, 2):
            self.e.acquire()  # Acquire semaphore for even numbers
            printNumber(i)    # Print even number
            self.z.release()  # Release semaphore for zeroes

    def odd(self, printNumber):
        """
        Prints odd numbers and releases semaphore for zeroes.

        :param printNumber: Method to print the number.
        :type printNumber: method
        """
        for i in range(1, self.n + 1, 2):
            self.o.acquire()  # Acquire semaphore for odd numbers
            printNumber(i)    # Print odd number
            self.z.release()  # Release semaphore for zeroes
