from random import Random
import axelrod as axl

# Dictionary with possible choices for a player
CHOICES = {
    'defect': 0,
    'cooperate': 1
}


class CupAlg(axl.Player):
    """
    Cooperates for first 5 turns.
    With each enemy's defect increas its defectivness,
    when defectivness reaches 1, it Defects.
    When opponent cooperates decrease its defectivness by forgivness_rate.
    """

    name = "MyAlg"
    classifier = {
        "memory_depth": 0,
        "stochastic": False,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }
    defectivness: float = 0.5
    defect_growth: float = 0.7
    forgivness_rate: float = 0.2

    def __init__(self, seed: int):
        super().__init__()
        self.rng: Random = Random()
        self.rng.seed(seed)

    def strategy(self, opponent: axl.Player) -> axl.Action:
        """Actual strategy definition that determines player's action."""
        if not opponent.history:
            return axl.Action.C

        # Increase defectivness when opponent played D
        if opponent.history[-1] == axl.Action.D:
            self.defectivness += self.defect_growth
        else:
            self.defectivness -= self.forgivness_rate

        # Play D when opponent played too much D
        if len(opponent.history) < 5:
            return axl.Action.C
        if self.defectivness > 1:
            self.defectivness -= self.forgivness_rate
            return axl.Action.D
        return axl.Action.C


class Test(axl.Player):
    """
    A player to test creation of player.
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
    """
    A player that playes randomly with 50/50 chance.
    Can be seeded on creation.
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


defectivness: float = 0.5
defect_growth: float = 0.7
forgivness_rate: float = 0.2


# My alg
def cupAlg(history):
    global defectivness, defect_growth, forgivness_rate
    """ Copy of CupAlgorithm in function form """
    if len(history) < 5:
        return CHOICES['cooperate']
    if history[-1][1] == CHOICES['defect']:
        defectivness += defect_growth
    else:
        defectivness -= forgivness_rate
    if defectivness > 1:
        defectivness -= forgivness_rate
        return CHOICES['defect']
    return CHOICES['cooperate']


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
