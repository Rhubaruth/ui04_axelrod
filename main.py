# import matplotlib.pyplot as plt
import axelrod as axl
from prettytable import PrettyTable
from algs import TitForTat, \
        AlwaysDefect, \
        AlwaysCoop, \
        Test, \
        SeededRandom, \
        MyAlg


# Payoff matrix
matrix = [[(1, 1), (5, 0)], [(0, 5), (3, 3)]]
NUM_TURNS = 100


# Play for 200 rounds
def battle(alg1, alg2):
    # History will be in a form of:
    # [(round 1 player1 choice, round 1 player2 choice),
    #  (round 2 player1 choice, round 2 player2 choice), ...]
    history = []
    score = {
        'player1': 0,
        'player2': 0
    }

    for i in range(5):
        # player2 should get history in a format:
        # (player2 choice, player1 choice)
        reversedHistory = [tup[::-1] for tup in history]

        # get a players choices
        player1_choice = alg1(history)
        player2_choice = alg2(reversedHistory)

        # append the current round to history
        history.append((player1_choice,
                        player2_choice))

        # get scores
        score1, score2 = matrix[player1_choice][player2_choice]
        score['player1'] += score1
        score['player2'] += score2

    # print('Round', i+1, ':', history[-1], '- score', score1, ':', score2)
    return score


def main():
    tournament_algs = [
        TitForTat,
        AlwaysDefect,
        AlwaysCoop,
        axl.TitForTat,
        ]

    print(f"Tournament with {len(tournament_algs)} participants")
    for alg1 in tournament_algs:
        for alg2 in tournament_algs:
            print(f"{alg1.__name__} vs {alg2.__name__}: ", end=' ')
            print(battle(alg1, alg2))
            if alg1 == alg2:
                break

    # # Print results
    # print(battle(AlwaysDefect, TitForTat))


def mainAxl():
    players = (
            axl.Cooperator(),
            axl.Defector(),
            axl.TitForTat(),
            axl.Adaptive(),
            SeededRandom(404),
            MyAlg(404),
            Test(),
            axl.Alternator(),
            axl.CooperatorHunter(),
            )
    tournament = axl.Tournament(players, turns=NUM_TURNS, repetitions=3)
    results: axl.ResultSet = tournament.play()
    # print(*results.summarise(), sep='\n')
    # print(*results.scores, sep='\n')
    for idx in results.ranking:
        print(results.players[idx], ' ', results.normalised_cooperation[idx])

    # plot = axl.Plot(results)
    # p = plot.payoff()
    # p.set_label('payoff')

    # plt.show()

    table_payoffs = PrettyTable()
    table_payoffs.field_names = [""] + ["Average", " "] + results.ranked_names
    for idx in results.ranking:
        # pop to get only one element from repetitions
        sorted_payoffs = [f'{results.payoffs[idx][j].pop():.3f}'
                          for j in results.ranking]
        avg_payoff = sum(map(eval, sorted_payoffs)) / len(sorted_payoffs)
        row = [results.players[idx], f'{avg_payoff:.3f}', '']
        row += sorted_payoffs
        table_payoffs.add_row(row)

    table_payoffs.align = "r"
    table_payoffs.align[""] = "l"

    print(table_payoffs)

    table_coop = PrettyTable()
    table_coop.field_names = [""] + results.ranked_names
    for idx in results.ranking:
        sorted_coop = [f'{results.normalised_cooperation[idx][j]:.3f}'
                       for j in results.ranking]
        row = [results.players[idx]] + sorted_coop
        table_coop.add_row(row)

    table_coop.align = "r"
    table_coop.align[""] = "l"

    print(table_coop)


if __name__ == '__main__':
    # main()
    mainAxl()
