# import matplotlib.pyplot as plt
import axelrod as axl
from prettytable import PrettyTable
from algs import SeededRandom, CupAlg


# Payoff matrix
matrix = [[(1, 1), (5, 0)], [(0, 5), (3, 3)]]
NUM_TURNS = 100


def main():
    """ Main loop for algorithms based on axl.Player from axelrod lib. """
    # Set players
    players = (
            axl.Cooperator(),
            axl.Defector(),
            axl.TitForTat(),
            axl.Adaptive(),
            SeededRandom(101),
            CupAlg(101),
            axl.Alternator(),
            # axl.CooperatorHunter(),
            )
    tournament = axl.Tournament(players, turns=NUM_TURNS, repetitions=3)
    results: axl.ResultSet = tournament.play()
    # print(*results.summarise(), sep='\n')
    # print(*results.scores, sep='\n')
    # for idx in results.ranking:
    #     print(results.players[idx], ' ', results.normalised_cooperation[idx])

    # plot = axl.Plot(results)
    # p = plot.payoff()
    # p.set_label('payoff')

    # plt.show()

    # Create table for output average payoffs
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

    # Create table for output cooperation rate
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
    main()
