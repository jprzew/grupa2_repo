# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.3
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import random
import matplotlib.pyplot as plt




class Probability:
    """Descriptor for probability attributes."""

    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        setattr(obj, self.private_name, min(1, max(0, value)))


class Creature:
    """A creature with a probability of death and reproduction.

    Attributes:
        p_death (float): Probability of dying.
        p_reproduce (float): Probability of reproducing.
        alive (bool): Whether the creature is alive.
    """

    sigma = 0.02  # Standard deviation random component for mutation
    p_death = Probability()
    p_reproduce = Probability()

    def __init__(self, p_death=0.2, p_reproduce=0.2):
        self.p_death = p_death
        self.p_reproduce = p_reproduce
        self.alive = True

    def kill(self):
        if random.random() <= self.p_death:
            self.alive = False

    def reproduce(self):
        if random.random() <= self.p_reproduce and self.alive:
            return type(self)()


class Predator(Creature):

    p_death_hungry = Probability()
    _p_death = Probability()

    def __init__(self, 
                 p_death=0.2,
                 p_reproduce=0.2, 
                 p_death_hungry=0.8):
        
        super().__init__(p_death, p_reproduce)
        self.p_death_hungry = p_death_hungry
        self.hungry = False

    def hunt(self, prey):
         if random.random() <= prey.p_hunt and prey.alive:
             self.hungry = False
             prey.alive = False

    @property
    def p_death(self):
        return self.p_death_hungry if self.hungry else self._p_death

    @p_death.setter
    def p_death(self, value):
        self._p_death = value
        


class Prey(Creature):

    p_hunt = Probability()

    def __init__(self, 
                 p_death=0.2,
                 p_reproduce=0.2, 
                 p_hunt=0.3):
        
        super().__init__(p_death, p_reproduce)
        self.p_hunt = p_hunt


class Population:
    """A population of creatures.

    Attributes:
        creator (subtype of Creature): A class used to create creatures
        specimens (set): A set of Creature instances.
        history (list): A list of population sizes.
    """

    def __init__(self, creator, n=100):
        """Initialize the population with n creatures."""
        self.creator = creator
        self.specimens = {self.creator() for _ in range(n)}
        self.history = []

    @property
    def specimens(self):
        return self._specimens

    @specimens.setter
    def specimens(self, value):
        self._specimens = value
        self.n = len(value)

    def natural_selection(self):
        """Model of natural selection process: kill and reproduce."""
        newborns = {specimen.reproduce() for specimen in self.specimens} - {None}
        {specimen.kill() for specimen in self.specimens}
  
        self.history.append(self.n)
        self.specimens = {specimen for specimen in self.specimens
                          if specimen.alive} | newborns

    def plot_history(self):
        plt.plot(self.history)

    def plot_histogram(self, parameter):
        plt.hist([getattr(specimen, parameter) for specimen in self.specimens])


def hunting(prey, predators):
    for predator in predators.specimens:
        predator.hungry = True
    
    n_pairs = min(predators.n, prey.n)
    pairs = zip(list(predators.specimens)[:n_pairs], list(prey.specimens)[:n_pairs])

    for predator, prey in pairs:
        predator.hunt(prey)

def simulation(prey, predators, n):
    for _ in range(n):
        hunting(prey, predators)
        prey.natural_selection()
        predators.natural_selection()

def plot_history(prey, predators):
    plt.plot(list(zip(prey.history, predators.history)))



# %%
N_PREY = 300
N_PREDATOR = 100

population_prey = Population(creator=Prey, n=N_PREY)
population_predators = Population(creator=Predator, n=N_PREDATOR)

# %%
simulation(population_prey, population_predators, n=30)

# %%
plot_history(population_prey, population_predators)


# %%
population_predators.history

# %%

# %%

# %%

# %%
