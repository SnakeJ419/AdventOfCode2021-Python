import Utils


def part_one():
    array = Utils.special('Inputs/Day8.txt')
    count = 0
    for line in array:
        for s in line.split(' | ')[1].split(' '):
            if len(s) == 2 or len(s) == 4 or len(s) == 3 or len(s) == 7:
                count += 1
    print(count)

# What Everything Will Be Mapped To
#  topp
# t    r
# c    r
#  tctc
# b    r
# c    r
#  bcbc


class Mapper:
    right = []
    top = []
    top_corner = []
    bottom_corner = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

    def __init__(self, important: list):
        self.right = []
        self.top = []
        self.top_corner = []
        self.bottom_corner = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        for s in important:
            if len(s) == 2:
                self.potential_to(s, self.right)
            elif len(s) == 3:
                self.potential_to(s, self.top)
            elif len(s) == 4:
                self.potential_to(s, self.top_corner)

        print(f'Right: {self.right}\nTop Corner: {self.top_corner}\nBottom Corner: {self.bottom_corner}\nTop: {self.top}')
        for c in self.right:
            self.top.remove(c)
            self.top_corner.remove(c)

        for c in (self.right + self.top + self.top_corner):
            self.bottom_corner.remove(c)

    def potential_to(self, s: str, *targets: list):
        for target in targets:
            for c in s:
                if not target.__contains__(c):
                    target.append(c)

    def convert_sequence(self, s: str):
        if len(s) == 2:
            return 1
        elif len(s) == 3:
            return 7
        elif len(s) == 4:
            return 4
        elif len(s) == 7:
            return 8

        # right=0, top=1, bottom_corner=2, top_corner=3
        counts = [0] * 4
        for c in s:
            if self.right.__contains__(c):
                counts[0] += 1
            elif self.top.__contains__(c):
                counts[1] += 1
            elif self.bottom_corner.__contains__(c):
                counts[2] += 1
            elif self.top_corner.__contains__(c):
                counts[3] += 1
        if counts[0] == 2 and counts[1] == 1 and counts[2] == 2 and counts[3] == 1:
            return 0
        elif counts[0] == 1 and counts[1] == 1 and counts[2] == 2 and counts[3] == 1:
            return 2
        elif counts[0] == 2 and counts[1] == 1 and counts[2] == 1 and counts[3] == 1:
            return 3
        elif counts[0] == 1 and counts[1] == 1 and counts[2] == 1 and counts[3] == 2:
            return 5
        elif counts[0] == 1 and counts[1] == 1 and counts[2] == 2 and counts[3] == 2:
            return 6
        elif counts[0] == 2 and counts[1] == 1 and counts[2] == 1 and counts[3] == 2:
            return 9
        else:
            exit(1)


def part_two():
    array = Utils.special('Inputs/Day8.txt')
    count = 0
    for line in array:
        matters = []
        for s in line.split(' | ')[0].split(' '):
            if len(s) == 2 or len(s) == 4 or len(s) == 3:
                matters.append(s)
        display_map = Mapper(matters)
        string_rep = ''
        for s in line.split(' | ')[1].split(' '):
            string_rep += str(display_map.convert_sequence(s))
        count += int(string_rep)
    print(count)


part_two()