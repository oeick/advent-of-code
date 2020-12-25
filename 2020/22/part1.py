import re

with open('input.txt', 'r') as input_file:
    content = input_file.read()

player1_pattern = re.compile(r'Player 1:\n((\d+\n)+)')
player2_pattern = re.compile(r'Player 2:\n((\d+\n)+)')

match = player1_pattern.match(content)
player1 = [int(d) for d in match[1].split('\n') if d]

match = player2_pattern.search(content)
player2 = [int(d) for d in match[1].split('\n') if d]


while len(player1) > 0 and len(player2) > 0:
    if player1[0] > player2[0]:
        player1.append(player1.pop(0))
        player1.append(player2.pop(0))
    else:
        player2.append(player2.pop(0))
        player2.append(player1.pop(0))

winner = player1 if len(player1) > 0 else player2

m = 0
for i, c in enumerate(winner):
    m += c * (len(winner) - i)

print(m)


