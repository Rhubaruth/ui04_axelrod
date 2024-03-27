from random import Random
import axelrod as axl

# Dictionary with possible choices for a player
CHOICES = {
    'defect': 0,
    'cooperate': 1
}


class MyAlg(axl.Player):
    """
    A player.
    """

    name = "MyAlg"
    classifier = {
        "memory_depth": 0,
        "stochastic": True,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }
    defect_persistance: float = 0.7
    defect_rate: float = 0.85
    defectivness: float = 0.15

    def __init__(self, seed: int):
        super().__init__()
        self.rng: Random = Random()
        self.rng.seed(seed)

    def strategy(self, opponent: axl.Player) -> axl.Action:
        """Actual strategy definition that determines player's action."""
        if not opponent.history:
            return axl.Action.C

        self.defectivness *= self.defect_persistance
        if opponent.history[-1] == axl.Action.D:
            self.defectivness += self.defect_rate
        self.defectivness -= self.defect_rate / 2.0

        if self.rng.random() < self.defectivness:
            return axl.Action.D
        return axl.Action.C


class Test(axl.Player):
    """A player who only ever cooperates.

    Names:

    - Cooperator: [Axelrod1984]_
    - ALLC: [Press2012]_
    - Always cooperate: [Mittal2009]_
    """

    name = "Test TFT"
    classifier = {
        "memory_depth": 0,
        "stochastic": False,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    @staticmethod
    def strategy(opponent: axl.Player) -> axl.Action:
        """Actual strategy definition that determines player's action."""
        if len(opponent.history) < 1:
            return axl.Action.C
        return opponent.history[-1]


class SeededRandom(axl.Player):
    """A player who only ever cooperates.

    Names:

    - Cooperator: [Axelrod1984]_
    - ALLC: [Press2012]_
    - Always cooperate: [Mittal2009]_
    """

    name = "Random seed"
    classifier = {
        "memory_depth": 0,
        "stochastic": True,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    actions = [axl.Action.C, axl.Action.D]

    def __init__(self, seed: int):
        super().__init__()
        self.rng: Random = Random()
        self.rng.seed(seed)

    def strategy(self, opponent: axl.Player) -> axl.Action:
        """Actual strategy definition that determines player's action."""
        return self.rng.choice(self.actions)


# Tit for tat strategy
def TitForTat(history):
    if len(history) == 0:
        return CHOICES['cooperate']
    else:
        return history[-1][1]


# Always defect strategy
def AlwaysDefect(history):
    return CHOICES['defect']


# Always coop strategy
def AlwaysCoop(history):
    return CHOICES['cooperate']
