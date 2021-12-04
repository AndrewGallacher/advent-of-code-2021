
def get_total_of_uncalled_numbers(card):
    score = 0
    for row in card:
        for cell in row:
            if cell != None:
                score += cell
    return score

def is_winning_card(card):  
    for i in range(5):
        count_i = 0
        count_j = 0
        for j in range(5):
            if card[i][j] == None:  
                count_i += 1
            if card[j][i] == None:
                count_j += 1 
        if count_i == 5 or count_j == 5:
            return True
    return False

def mark_called_numnber(card, number):
    for row in range(5):
        for column in range(5):
            if card[row][column] == number:
                card[row][column] = None
                return
    
#---------------------------------------------------

input = open('test.txt', 'r')
input = open('input.txt', 'r')

lines = []
for line in input.readlines():
    lines.append(line)

numbers_to_draw_text = lines[0].split(',')
numbers_to_draw = []

for item in numbers_to_draw_text:
    numbers_to_draw.append(int(item))

print(numbers_to_draw)

cards = []
scores = []
line_number = 1

while line_number < len(lines) - 1:
    while lines[line_number].strip() == '':
        line_number += 1

    card = []
    for i in range(5):
        array_as_text = lines[line_number]\
            .strip()\
            .replace('  ', ' ')\
            .replace('\n', '')\
            .split(' ')
        row = list(map(lambda x: int(x), array_as_text))
        
        card.append(row)
        line_number += 1

    cards.append(card)
    scores.append(0)

print(cards) 

winning_card_found = False
last_winning_score = 0
for number in numbers_to_draw:
    print('--------------------')
    print('Number drawn:', number)
    no = 0
    for card in cards:
        mark_called_numnber(card, number)
        score = get_total_of_uncalled_numbers(card)
        is_winning = is_winning_card(card)
        print(no + 1, score, is_winning)

        if is_winning and scores[no] == 0:
            print('--------------------')
            print('Card', no + 1, 'wins now')
            scores[no] = score * number
            last_winning_score = score * number
            winning_card_found = True
            #break

        no += 1

    # if winning_card_found:
        # break

print(scores)
print('last winning score', last_winning_score)
