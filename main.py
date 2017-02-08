class Ship:
    '''
    It's a ship
    '''

    def __init__(self, coordinates):
        '''
        coordinates is [(0, 0), (9, 3), ...]
        '''
        self.coordinates = coordinates
        self.orientation = 'H' if coordinates[0][0] == coordinates[-1][0] else 'V'
        self.length = (1, len(coordinates)) if self.orientation == 'H' else (len(coordinates), 1)


class Field:
    '''
    It's a field
    '''

    def __init__(self, filename=None, rand=False):
        if not filename and not rand:
            self.lines = ['-' * 10 for _ in range(10)]
        elif rand:  # generate_field
            from random import randrange
            from random import choice
            from itertools import product

            self.lines = ['-' * 10 for _ in range(10)]
            self.ships = []
            self.blocked = []

            for i in range(4, 0, -1):
                for o in range(5 - i):
                    while True:
                        direction = choice(['H', 'V'])
                        coord = (randrange(11 - i), randrange(11 - i))
                        curShip = [coord]
                        if coord not in self.blocked:
                            if direction == 'H':
                                corrplacement = True
                                for p in range(1, i):
                                    if (coord[0], coord[1] + p) in self.blocked:
                                        corrplacement = False
                                        break
                                    else:
                                        curShip.append((coord[0], coord[1] + p))
                            else:
                                corrplacement = True
                                for p in range(1, i):
                                    if (coord[0] + p, coord[1]) in self.blocked:
                                        corrplacement = False
                                        break
                                    else:
                                        curShip.append((coord[0] + p, coord[1]))
                            if corrplacement:
                                # Blocking area around ship
                                for v in product(range(curShip[0][0] - 1 if curShip[0][0] != 0 else 0,
                                                       curShip[-1][0] + 2 if curShip[-1][0] < 10 else 10),
                                                 range(curShip[0][1] - 1 if curShip[0][1] != 0 else 0,
                                                       curShip[-1][1] + 2 if curShip[-1][1] < 10 else 10)):
                                    self.blocked.append(v)
                                self.ships.append(Ship(curShip))
                                break

            for ship in self.ships:
                for c in ship.coordinates:
                    try:
                        self.lines[c[0]] = self.lines[c[0]][:c[1]] + '*' + self.lines[c[0]][c[1] + 1:]
                    except IndexError:
                        self.lines[c[0]] = self.lines[c[0]][:c[1]] + '*' + self.lines[c[0]][c[1]:]

        else:  # read_field
            try:
                with open(filename) as f:
                    self.lines = []
                    self.ships = []
                    self.blocked = []
                    # read field
                    for line in f:
                        self.lines.append(line.strip())
                    # read ships
                    from itertools import product

                    for c in product(range(10), range(10)):
                        if self.lines[c[0]][c[1]] == '*':
                            curShip = [c]
                            horizontal = True
                            for i in range(1, 4):
                                try:
                                    if self.lines[c[0]][c[1] + i] == '*':
                                        curShip.append(c)
                                        horizontal = False
                                    else:
                                        break
                                except IndexError:
                                    break
                            if horizontal:
                                for i in range(1, 4):
                                    try:
                                        if self.lines[c[0] + i][c[1]] == '*':
                                            curShip.append(c)
                                        else:
                                            break
                                    except IndexError:
                                        break
                            # Blocking area around ship
                            for v in product(range(curShip[0][0] - 1 if curShip[0][0] != 0 else 0,
                                                   curShip[-1][0] + 2 if curShip[-1][0] < 10 else 10),
                                             range(curShip[0][1] - 1 if curShip[0][1] != 0 else 0,
                                                   curShip[-1][1] + 2 if curShip[-1][1] < 10 else 10)):
                                self.blocked.append(v)
                            self.ships.append(Ship(curShip))
            except FileNotFoundError:
                self.lines = ['-' * 10 for _ in range(10)]

    def field_to_str(self, filename):
        '''
        Writes field into file
        :param filename:
        :return: None
        '''
        with open(filename, 'w') as f:
            for line in self.lines:
                f.write(line + '\n')

    def has_ship(self, coordinate):
        '''
        Checks if klitynka has a ship
        :param coordinate:
        :return: bool
        '''
        for ship in self.ships:
            if coordinate in ship.coordinates:
                return True
        return False

    def ship_size(self, coordinate):
        '''
        :param coordinate:
        :return: size of ship
        '''
        for ship in self.ships:
            if coordinate in ship.coordinates:
                return ship.length
        return 0

    def is_valid(self):
        '''
        Check if current field is valid
        :return:
        '''
        counter = [0, 0, 0, 0]
        for ship in self.ships:
            counter[ship.length - 1] += 1
        if counter == [4, 3, 2, 1]:
            return True
        else:
            return False


class Player:
    def __init__(self):
        pass

    def pew(self, coordinate):
        pass


class Game:  # what is game?
    pass
