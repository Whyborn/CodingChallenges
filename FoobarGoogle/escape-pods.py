class Room:
    # The master class

    # Initialise the room object with its ID and type
    def __init__(self, room_id):

        self.room_id = room_id
        self.number_bunnies = 0
        self.outgoing_connections = []
        self.incoming_connections = []

        return

    # Placeholder for child member functions
    def set_max_rates(self):
        pass

    def send_bunnies(self):
        pass

    def __repr__(self):
        return ("Room " + str(self.room_id) + " currently containing " + str(self.number_bunnies) + " bunnies")

class Entry(Room):

    def __init__(self, room_id):
        Room.__init__(self, room_id)

    def set_max_rates(self):
        self.max_outgoing = 0

        for exit in self.outgoing_connections:
            self.max_outgoing += exit.max_rate

        self.max_incoming = self.max_outgoing

    def send_bunnies(self):

        for exit in self.outgoing_connections:
            exit.target.number_bunnies += min(exit.max_rate, exit.target.max_outgoing - exit.target.number_bunnies)

        return 0

class Exit(Room):

    def __init__(self, room_id):
        Room.__init__(self, room_id)

    def set_max_rates(self):
        self.max_incoming = 0

        for entry in self.incoming_connections:
            self.max_incoming += entry.max_rate

        self.max_outgoing = self.max_incoming
    
    def send_bunnies(self):
        # The bunnies escape the system
        number_escapees = self.number_bunnies
        self.number_bunnies = 0
        return number_escapees

class Intermediate(Room):

    def __init__(self, room_id):
        Room.__init__(self, room_id)

    def set_max_rates(self):
        self.max_outgoing = 0
        self.max_incoming = 0
        
        for exit in self.outgoing_connections:
            self.max_outgoing += exit.max_rate

        for entry in self.incoming_connections:
            self.max_incoming += entry.max_rate

    def send_bunnies(self):
        
        for exit in self.outgoing_connections:
            number_to_send = min(exit.max_rate, exit.target.max_outgoing - exit.target.number_bunnies, self.number_bunnies)
            exit.target.number_bunnies += number_to_send
            self.number_bunnies -= number_to_send

        return 0

class Connection:

    def __init__(self, rate, origin, target):

        self.max_rate = rate
        self.current_rate = rate
        self.origin = origin
        self.target = target

    def __repr__(self):
        return "Connection from " + str(self.origin.room_id) + " to " + str(self.target.room_id) + " with a current bunny rate of " + str(self.current_rate) + " and max rate of " + str(self.max_rate) + "."


def establish_connections(paths, room_list):

    for i in range(len(paths)):
        for j in range(len(paths)):
            if paths[i][j] > 0:
                new_connection = Connection(paths[i][j], room_list[i], room_list[j])
                room_list[i].outgoing_connections.append(new_connection)
                room_list[j].incoming_connections.append(new_connection)

def solution(entries, exits, path):

    n = len(path)

    room_list = []
    for i in range(n):

        if i in entries:
            room_list.append(Entry(i))

        elif i in exits:
            room_list.append(Exit(i))

        else:
            room_list.append(Intermediate(i))

    establish_connections(path, room_list)

    for _ in range(5):
        total_escapees = 0
        for room in room_list:
            room.set_max_rates()

        for room in room_list:
            total_escapees += room.send_bunnies()

        print(total_escapees)

    return total_escapees

if __name__ == "__main__":

    #print(solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]))
    #print(solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
    print(solution([0, 1], [5], [[0, 0, 0, 0, 6, 0], [0, 0, 5, 0, 0, 0], [0, 0, 0, 0, 7, 0], [0, 0, 0, 0, 0, 5], [0, 6, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
    #print(solution([0], [3], [[0, 0, 0, 7], [0, 0, 2, 0], [0, 0, 0, 5], [0, 2, 0, 0]]))
