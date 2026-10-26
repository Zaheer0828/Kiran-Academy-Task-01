
from abc import ABC, abstractmethod


class Flight:
    def __init__(self, flight_code, airline, source, destination,
                 available_seats, base_fare):
        self.__flight_code = flight_code
        self.__airline = airline
        self.__source = source
        self.__destination = destination
        self.__available_seats = available_seats
        self.__base_fare = base_fare

    @property
    def flight_code(self):
        return self.__flight_code

    @property
    def airline(self):
        return self.__airline

    @property
    def source(self):
        return self.__source

    @property
    def destination(self):
        return self.__destination

    @property
    def available_seats(self):
        return self.__available_seats

    @property
    def base_fare(self):
        return self.__base_fare

    def book_seats(self, count):
        if 0 < count <= self.__available_seats:
            self.__available_seats -= count
            return True
        return False

    def display_flight(self):
        print(
            f"{self.flight_code:<8} | {self.airline:<15} | "
            f"{self.source} to {self.destination} | "
            f"Seats: {self.available_seats} | "
            f"Base fare: Rs. {self.base_fare}"
        )


class Passenger(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_discount(self):
        pass


class RegularPassenger(Passenger):
    def get_discount(self):
        return 0.0


class StudentPassenger(Passenger):
    def get_discount(self):
        return 0.10


class Booking:
    def __init__(self, booking_id, flight, passenger, ticket_count):
        self.booking_id = booking_id
        self.flight = flight
        self.passenger = passenger
        self.ticket_count = ticket_count

        self.subtotal = flight.base_fare * ticket_count
        self.discount_rate = passenger.get_discount()
        self.discount = self.subtotal * self.discount_rate
        self.total_fare = self.subtotal - self.discount

    def display_summary(self):
        print("\n========== BOOKING SUMMARY ==========")
        print("Booking ID:", self.booking_id)
        print("Passenger:", self.passenger.name)
        print("Age:", self.passenger.age)
        print("Passenger type:", type(self.passenger).__name__)
        print("Flight:", self.flight.flight_code)
        print("Airline:", self.flight.airline)
        print("Route:", self.flight.source, "to", self.flight.destination)
        print("Tickets:", self.ticket_count)
        print(f"Base fare per ticket: Rs. {self.flight.base_fare:.2f}")
        print(f"Subtotal: Rs. {self.subtotal:.2f}")
        print(
            f"Discount ({self.discount_rate:.0%}): "
            f"Rs. {self.discount:.2f}"
        )
        print(f"Final amount: Rs. {self.total_fare:.2f}")
        print("=====================================")


class FlightBookingSystem:
    def __init__(self):
        self.flights = [
            Flight("PN101", "Kiran Air", "Pune", "Delhi", 20, 4000),
            Flight("MB202", "Sky India", "Mumbai", "Bengaluru", 15, 3500),
            Flight("PN303", "Air Connect", "Pune", "Hyderabad", 10, 3000)
        ]
        self.bookings = []
        self.booking_counter = 1001

    def display_flights(self):
        print("\n--------------- AVAILABLE FLIGHTS ---------------")
        for flight in self.flights:
            flight.display_flight()

    def find_flight(self, code):
        for flight in self.flights:
            if flight.flight_code.lower() == code.strip().lower():
                return flight
        return None

    def validate_booking(self, name, age, tickets, flight):
        if not name.strip():
            raise ValueError("Passenger name cannot be blank.")
        if age <= 0:
            raise ValueError("Age must be greater than zero.")
        if tickets <= 0:
            raise ValueError("Ticket count must be greater than zero.")
        if tickets > flight.available_seats:
            raise ValueError(
                f"Not enough seats. Only {flight.available_seats} "
                "seat(s) are available."
            )

    def book_flight(self):
        self.display_flights()
        code = input("\nEnter flight code: ").strip()
        flight = self.find_flight(code)

        if flight is None:
            print("Booking failed: Flight code not found.")
            return

        name = input("Enter passenger name: ").strip()

        try:
            age = int(input("Enter passenger age: "))
            passenger_type = input(
                "Passenger type (Regular/Student): "
            ).strip().lower()
            tickets = int(input("Enter number of tickets: "))

            if passenger_type not in ("regular", "student"):
                raise ValueError("Choose Regular or Student.")

            self.validate_booking(name, age, tickets, flight)

            if passenger_type == "student":
                passenger = StudentPassenger(name, age)
            else:
                passenger = RegularPassenger(name, age)

            # Seats are changed only after successful validation.
            if not flight.book_seats(tickets):
                print("Booking failed: Not enough seats available.")
                return

            booking = Booking(
                f"BK{self.booking_counter}",
                flight,
                passenger,
                tickets
            )

            self.bookings.append(booking)
            self.booking_counter += 1

            print("\nBooking confirmed!")
            booking.display_summary()

        except ValueError as error:
            print("Booking failed:", error)

    def view_booking(self):
        if not self.bookings:
            print("\nNo confirmed booking exists yet.")
            return

        print("\nMost recent confirmed booking:")
        self.bookings[-1].display_summary()

    def run(self):
        while True:
            print("\n====== KIRAN AIR BOOKING ======")
            print("1. View Flights")
            print("2. Book Flight")
            print("3. View Booking")
            print("4. Exit")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                self.display_flights()
            elif choice == "2":
                self.book_flight()
            elif choice == "3":
                self.view_booking()
            elif choice == "4":
                print("Thank you for using Kiran Air Booking!")
                break
            else:
                print("Invalid choice. Select 1, 2, 3, or 4.")


if __name__ == "__main__":
    system = FlightBookingSystem()
    system.run()
