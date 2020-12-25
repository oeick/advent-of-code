privatekey_card = 11349501
privatekey_door = 5107328

loop_card = 0
loop_door = 0

subject_number = 7

value = 1
i = 1
while loop_door == 0 or loop_card == 0:
    value = (value * subject_number) % 20201227
    if value == privatekey_card:
        loop_card = i
    if value == privatekey_door:
        loop_door = i
    i += 1


def calculate_encryption_key(privatekey, loop_size):
    value = 1
    for i in range(loop_size):
        value = (value * privatekey) % 20201227
    return value


encryption_key_card = calculate_encryption_key(privatekey_door, loop_card)
encryption_key_door = calculate_encryption_key(privatekey_card, loop_door)

assert encryption_key_card == encryption_key_door

print(encryption_key_card)
