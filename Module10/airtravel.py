

class Flight:

    def __init__(self, number, aircraft) :
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()

    def number(self):
        return self._number

    def aircraft_model(self):
        return self._aircraft._model

class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row
    
    def registration(self):
        return self._registration

    def model(self):
        return self._model
    
    def seating_plan(self):
        return (range(1, self._num_rows + 1), "ABCDEFGHJ"[:self._num_seats_per_row])


f = Flight('SN060', Aircraft('G-EUPT', 'Airbus A319', num_rows = 22, num_seats_per_row = 6))
print(f.number())
print(f.aircraft_model())

