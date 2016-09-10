#bowling.py

scores = []

f = []

with open('scores.txt', 'r') as score_file:
    for game in score_file:

        game_score = 0

        # make list of balls
        b = game.rstrip('\n').split(' ')
        balls = [int(i) if i.isdigit() else i for i in b]

        #create frames
        frames = {i: [[], 0] for i in range(1, 11)}

        current_frame = 1
        for ball in balls:
            if current_frame == 10:
                # add all remaining balls to the last frame
                frames[current_frame][0].append(ball)
            else:
                if len(frames[current_frame][0]) == 0:
                    # no items in current frame
                    frames[current_frame][0].append(ball)
                    if ball == 'X':
                        current_frame += 1
                elif len(frames[current_frame][0]) == 1:
                    # 1 item in current frame
                    frames[current_frame][0].append(ball)
                    current_frame += 1

        # score each frame
        for frame_number, values in frames.items():
            # values[0] is the balls
            # values[1] is the score for the frame

            # if 10th frame, just add everything together
            if frame_number == 10:
                for ball in values[0]:
                    if ball == 'X':
                        values[1] += 10
                    elif ball == '/':
                        values[1] = round(values[1], -1)
                    elif ball == '-':
                        pass
                    else:
                        values[1] += ball

            # if not 10th frame
            else:

                # if the value is an X
                if values[0][0] == 'X':
                    values[1] += 10

                    extra_value = 0     # total value to be added
                    extra_number = 0    # number of extra balls added so far

                    # check the next frame for 2 additional numbers to add
                    for ball in frames[frame_number+1][0]:
                        if extra_number == 2:
                            break
                        if ball == 'X':
                            extra_value += 10
                            extra_number += 1
                        elif ball == '/':
                            extra_value = 10
                            extra_number = 2
                        elif ball == '-':
                            extra_number += 1
                        else:
                            extra_value += ball
                            extra_number += 1

                    # if it was an X and we still need an additional number
                    if extra_number < 2:
                        if frames[frame_number + 2][0][0] == 'X':
                            extra_value += 10
                        elif frames[frame_number + 2][0][0] == '-':
                            pass
                        else:
                            extra_value += frames[frame_number + 2][0][0]


                    values[1] += extra_value

                # not an 'X'
                else:
                    set_value = 0
                    for ball in values[0]:
                        if ball == '-':
                            pass
                        elif ball == '/':
                            set_value = 10
                            if frames[frame_number+1][0][0] == 'X':
                                set_value += 10
                            elif frames[frame_number+1][0][0] == '-':
                                pass
                            else:
                                set_value += frames[frame_number+1][0][0]
                        else:
                            set_value += ball

                    values[1] = set_value

        print(frames)

        for item in frames.items():
            game_score += item[1][1]

        for i, a in frames.items():
            if len(a[0]) == 1:
                a[0].append(' ')
            if i == 10 and len(a[0]) == 1:
                a[0].append(' ')
            elif i == 10 and len(a[0]) == 2:
                a[0].append(' ')
                a[0].append(' ')

        f.append(frames)

        scores.append(game_score)

print(scores)
print(f)

def format(game):
    t = []
    t.append(game[1][1])
    t.append(t[0] + game[2][1])
    t.append(t[1] + game[3][1])
    t.append(t[2] + game[4][1])
    t.append(t[3] + game[5][1])
    t.append(t[4] + game[6][1])
    t.append(t[5] + game[7][1])
    t.append(t[6] + game[8][1])
    t.append(t[7] + game[9][1])
    t.append(t[8] + game[10][1])

    totals = []

    for a, i in enumerate(t):
        str_total = str(i)
        if a == 9:
            print('ayy')
            if len(str_total) == 0:
                print('a')
                str_total = '     '
            elif len(str_total) == 1:
                print('b')
                str_total = '    ' + str_total
            elif len(str_total) == 2:
                str_total = '   ' + str_total
                print('b')
            elif len(str_total) == 3:
                str_total = '  ' + str_total
                print('d')
            elif len(str_total) == 4:
                print('e')
                str_total = ' ' + str_total
            else:
                print('f')

        elif len(str_total) == 1:
            str_total = '  ' + str_total
        elif len(str_total) == 2:
            str_total = ' ' + str_total

        totals.append(str_total)

    f = """
  1   2   3   4   5   6   7   8   9    10
+---+---+---+---+---+---+---+---+---+-----+
|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {} {}|
|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|
+---+---+---+---+---+---+---+---+---+-----+
    """.format(game[1][0][0], game[1][0][1], game[2][0][0], game[2][0][1], game[3][0][0], game[3][0][1], game[4][0][0],
               game[4][0][1], game[5][0][0], game[5][0][1], game[6][0][0], game[6][0][1], game[7][0][0], game[7][0][1],
               game[8][0][0], game[8][0][1], game[9][0][0], game[9][0][1], game[10][0][0], game[10][0][1],
               game[10][0][2], totals[0], totals[1], totals[2], totals[3], totals[4], totals[5], totals[6], totals[7],
               totals[8], totals[9])

    print(f)



for game in f:
    print(format(game))
    print('\n')



