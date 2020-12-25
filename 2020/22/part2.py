import re

with open('input.txt', 'r') as input_file:
    content = input_file.read()

player1_pattern = re.compile(r'Player 1:\n((\d+\n)+)')
player2_pattern = re.compile(r'Player 2:\n((\d+\n)+)')

match = player1_pattern.match(content)
initial_player1 = [int(d) for d in match[1].split('\n') if d]

match = player2_pattern.search(content)
initial_player2 = [int(d) for d in match[1].split('\n') if d]


def play(player1, player2):
    winner = None
    history = []
    while not winner:
        state = {'player1': list(player1), 'player2': list(player2)}
        if state in history:
            winner = ('player1', list(player1))
            break
        p1_card = player1.pop(0)
        p2_card = player2.pop(0)
        if len(player1) >= p1_card and len(player2) >= p2_card:
            round_winner = play(list(player1[:p1_card]),
                                list(player2[:p2_card]))[0]
        else:
            round_winner = 'player1' if p1_card > p2_card else 'player2'
        if round_winner == 'player1':
            player1.append(p1_card)
            player1.append(p2_card)
            if len(player2) == 0:
                winner = ('player1', player1)
        elif round_winner == 'player2':
            player2.append(p2_card)
            player2.append(p1_card)
            if len(player1) == 0:
                winner = ('player2', player2)
        history.append(state)
    return winner


resulting_winner = play(initial_player1, initial_player2)

m = 0
for i, c in enumerate(resulting_winner[1]):
    m += c * (len(resulting_winner[1]) - i)

print(m)
