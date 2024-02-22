from enum import Enum


class Dir(str, Enum):
    RIGHT = 'R'
    LEFT = 'L'
    UP = 'U'
    DOWN = 'D'


command_sum = {
    Dir.RIGHT: {
        Dir.RIGHT: Dir.DOWN,
        Dir.LEFT: Dir.UP,
    },
    Dir.LEFT: {
        Dir.RIGHT: Dir.UP,
        Dir.LEFT: Dir.DOWN,
    },
    Dir.UP: {
        Dir.RIGHT: Dir.RIGHT,
        Dir.LEFT: Dir.LEFT,
    },
    Dir.DOWN: {
        Dir.RIGHT: Dir.LEFT,
        Dir.LEFT: Dir.RIGHT,
    },
}


current_dir = Dir.UP


room = []

[n, m] = list(map(int, input().split(' ')))

for i in range(n):
    room.append([*input()])

[y, x] = list(map(int, input().split(' ')))

z = input() #не используется

commands = input()


visited = set()

def set_visited(x,y):
    visited.add(str(x) + '|' + str(y))

set_visited(x,y)

for i in range(len(commands)):
    command = commands[i]
    if command == Dir.LEFT or command == Dir.RIGHT:
        current_dir = command_sum[current_dir][command]
    elif command == 'M':
        new_x = x
        new_y = y
        match current_dir:
            case Dir.UP:
                new_y -= 1
            case Dir.DOWN:
                new_y += 1
            case Dir.LEFT:
                new_x -= 1
            case Dir.RIGHT:
                new_x += 1
        if new_x > m or new_x < 1 or new_y > n or new_y < 1 or room[new_y - 1][new_x - 1] == '#':
            continue
        else:
            x = new_x
            y = new_y
            set_visited(x,y)

    # print('command',command,'current_dir',current_dir,'visited',visited, 'x',x,'y',y)

print(len(visited))








