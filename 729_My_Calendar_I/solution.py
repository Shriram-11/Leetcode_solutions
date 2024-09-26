class MyCalendar(object):

    def __init__(self):
        """
        Initialize the MyCalendar object.
        
        The constructor initializes an empty list called `dates`, which will store
        all the booked time intervals as a list of pairs, where each pair represents
        the start and end time of a booking.
        """
        self.dates = []  # List to store booked time intervals

    def book(self, start, end):
        """
        Try to book a new event in the calendar.

        The function checks if a new event (given by `start` and `end` times) can be 
        booked without overlapping any of the previously booked events. If there is 
        no overlap, the event is added to the calendar and the function returns True. 
        If the event overlaps with an existing booking, it returns False.

        Time Complexity: O(n), where n is the number of previously booked events. This 
        is because we check every existing event for overlaps.

        :param start: int
            The start time of the event to be booked.
        :param end: int
            The end time of the event to be booked (non-inclusive).
        
        :return: bool
            - True if the event can be booked without any conflict.
            - False if there is an overlap with any previously booked event.
        
        Example:
            obj = MyCalendar()
            obj.book(10, 20) -> True
            obj.book(15, 25) -> False (overlaps with the previous event)
            obj.book(20, 30) -> True (no overlap)
        """
        # If there are no existing bookings, add the event
        if self.dates == []:
            self.dates.append([start, end])  # Add the first booking
            return True
        
        # Check for overlap with existing bookings
        for a in self.dates:
            # Overlap condition 1: If `start` is within an already booked range
            if a[0] <= start < a[1]:
                return False
            # Overlap condition 2: If `end` extends into an already booked range
            if start < a[0] and end > a[0]:
                return False

        # If no overlap found, add the new booking
        self.dates.append([start, end])
        return True


# Example usage:
# obj = MyCalendar()
# param_1 = obj.book(start, end)
