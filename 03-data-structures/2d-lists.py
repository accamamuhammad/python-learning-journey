# 2D list - list made up of lists

cars = ['bmw', 'mercedes', 'tesla', 'ford']
planes = ['737', '757', '767', '787']
players = ['foden', 'kdb', 'pogba', 'lookman']

lifestyle = [cars, planes, players]

for collection in lifestyle:
    for things in collection:
        print(things, end=' ')
    print()
    
# Calculator Layout
row1 = ['1', '2', '3']
row2 = ['4', '5', '6']
row3 = ['7', '8', '9']
row4 = ['*', '0', '#']

all_rows = [row1, row2, row3, row4]

for rows in all_rows:
    for row in rows:
        print(row, end=" ")
    print()
    
    
# Quiz Game
questions = (
    'fasters Car',
    'best car colour',
    'best car brand',
    'best ferrari',
)

options = (
(
'A. ferrari', 'B. honda', 'C. Bugatti', 'D. koenigsegg'
),
(
'A. red', 'B. blue', 'C. yellow', 'D. pink'
),
(
'A. bmw', 'B. mercedes', 'C. ferrari', 'D. bugatti'
), (
'A. la-ferrari', 'B. 812', 'C. california', 'D. 458'
))

answers = ('D', 'A', 'C', 'A')
guesses = []
score = 0
question_num = 0

for question in questions:
    print('----------------')
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input('Enter (A, B, C, D): ').upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print('Correct')
    else:
        print('Wrong')
        print(f'{answers[question_num]} is the correct answer')
    
    question_num += 1

print('--------------------')
print('------RESULTS-------')
print('--------------------')

print('answrs: ', end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print('guesses: ', end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f'Your score is: {score}%')
