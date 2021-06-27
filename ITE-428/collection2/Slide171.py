# Slide 171
# win = 3, draw = 1, lose = 0

def show_final_result(data):
    for i, v in enumerate(data):
        score = v[1][0] * 3 + v[1][1]
        print("{}\t{:<20}{:>5}".format(i + 1, v[0], score))
        if i == 3 or i == 16:
            print("-" * 30)


def lose_morethan_draw(data):
    for v in data:
        diff = v[1][2] - v[1][1]
        if diff > 0:
            print("{:<20}{:>9}".format(v[0], diff))


def line():
    print("=" * 30)


premier_league_2017_2018 = [["Manchester City", (32, 4, 2)], ["Manchester United", (25, 6, 7)],
                            ["Tottenham", (23, 8, 7)], ["Liverpool", (21, 12, 5)],
                            ["Chelsea", (21, 7, 10)], ["Arsenal", (19, 6, 13)], ["Burnley", (14, 12, 12)],
                            ["Everton", (13, 10, 15)], ["Leicester", (12, 11, 15)], ["Newcastle", (12, 8, 18)],
                            ["Crystal Palace", (11, 11, 16)], ["Bournemouth", (11, 11, 16)], ["WestHam", (10, 12, 16)],
                            ["Watford", (11, 8, 19)], ["Brighton", (9, 13, 16)],
                            ["Huddersfield", (9, 10, 19)], ["Southampton", (7, 15, 16)], ["Swansea", (8, 9, 21)],
                            ["Stoke", (7, 12, 19)], ["West Bromwich", (6, 13, 19)]]

line()
print("   PREMIER LEAGUE 2017-2018")
print("         FINAL RESULT")
line()
show_final_result(premier_league_2017_2018)
line()
print("      LOSE MORE THAN DRAW")
line()
lose_morethan_draw(premier_league_2017_2018)
line()
