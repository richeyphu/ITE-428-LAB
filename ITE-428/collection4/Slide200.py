# Slide200

def stat_point_goalID(data):  # data -> list
    for i in data:
        pts = i["Result"]["W"] * 3 + i["Result"]["D"]
        gd = i["Goal"]["GF"] - i["Goal"]["GA"]
        print("{:>2} {:<25} Pts:{:>3} GD:{:>3}".format(i["Pos"], i["Team"].lower(), pts, gd))


def stat_percentages(data):  # data -> list
    data = sorted(data, key=lambda k: k["Team"])
    for i, v in enumerate(data):
        sum = v["Result"]["W"] + v["Result"]["D"] + v["Result"]["L"]
        win = v["Result"]["W"] / sum * 100
        draw = v["Result"]["D"] / sum * 100
        lose = v["Result"]["L"] / sum * 100
        print("{:>2} {:<25} Win[{:>5.2f}%] Draw[{:>5.2f}%] Lose[{:>5.2f}%]"
              .format(i + 1, v["Team"].upper(), win, draw, lose))


premier_league_2017_2018 = [
    {"Pos": 1, "Team": "Manchester City", "Result": {"W": 32, "D": 4, "L": 2}, "Goal": {"GF": 106, "GA": 27}},
    {"Pos": 2, "Team": "Manchester United", "Result": {"W": 25, "D": 6, "L": 7}, "Goal": {"GF": 68, "GA": 28}},
    {"Pos": 3, "Team": "Tottenham Hotspur", "Result": {"W": 23, "D": 8, "L": 7}, "Goal": {"GF": 74, "GA": 36}},
    {"Pos": 4, "Team": "Liverpool", "Result": {"W": 21, "D": 12, "L": 5}, "Goal": {"GF": 84, "GA": 38}},
    {"Pos": 5, "Team": "Chelsea", "Result": {"W": 21, "D": 7, "L": 10}, "Goal": {"GF": 62, "GA": 38}},
    {"Pos": 6, "Team": "Arsenal", "Result": {"W": 19, "D": 6, "L": 13}, "Goal": {"GF": 74, "GA": 51}},
    {"Pos": 7, "Team": "Burnley", "Result": {"W": 14, "D": 12, "L": 12}, "Goal": {"GF": 36, "GA": 39}},
    {"Pos": 8, "Team": "Everton", "Result": {"W": 13, "D": 10, "L": 15}, "Goal": {"GF": 44, "GA": 58}},
    {"Pos": 9, "Team": "Leicester City", "Result": {"W": 12, "D": 11, "L": 15}, "Goal": {"GF": 56, "GA": 60}},
    {"Pos": 10, "Team": "Newcastle United", "Result": {"W": 12, "D": 8, "L": 18}, "Goal": {"GF": 39, "GA": 47}},
    {"Pos": 11, "Team": "CrystalPalace", "Result": {"W": 11, "D": 11, "L": 16}, "Goal": {"GF": 45, "GA": 55}},
    {"Pos": 12, "Team": "Bournemouth", "Result": {"W": 11, "D": 11, "L": 16}, "Goal": {"GF": 45, "GA": 61}},
    {"Pos": 13, "Team": "West HamUnited", "Result": {"W": 10, "D": 12, "L": 16}, "Goal": {"GF": 48, "GA": 68}},
    {"Pos": 14, "Team": "Watford", "Result": {"W": 11, "D": 8, "L": 19}, "Goal": {"GF": 44, "GA": 64}},
    {"Pos": 15, "Team": "Brighton & Hove Albion", "Result": {"W": 9, "D": 13, "L": 16}, "Goal": {"GF": 34, "GA": 54}},
    {"Pos": 16, "Team": "HuddersfieldTown", "Result": {"W": 9, "D": 10, "L": 19}, "Goal": {"GF": 28, "GA": 58}},
    {"Pos": 17, "Team": "Southampton", "Result": {"W": 7, "D": 15, "L": 16}, "Goal": {"GF": 37, "GA": 56}},
    {"Pos": 18, "Team": "Swansea City", "Result": {"W": 8, "D": 9, "L": 21}, "Goal": {"GF": 28, "GA": 56}},
    {"Pos": 19, "Team": "Stoke City", "Result": {"W": 7, "D": 12, "L": 19}, "Goal": {"GF": 35, "GA": 68}},
    {"Pos": 20, "Team": "West Bromwich Albion", "Result": {"W": 6, "D": 13, "L": 19}, "Goal": {"GF": 31, "GA": 56}}]

# print("{}".format(premier_league_2017_2018))
# print("{}".format(premier_league_2017_2018[0]))
# print("{}".format(premier_league_2017_2018[0]["Result"]))
# print("{}".format(premier_league_2017_2018[0]["Result"]["W"]))

stat_point_goalID(premier_league_2017_2018)
print("-" * 70)
stat_percentages(premier_league_2017_2018)
