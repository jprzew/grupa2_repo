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


# %%
class Population:

    def __init__(self, n=100):
        self.speciemens = {Creature() for _ in range(n)}
        self.n = n

class Creature:
    alive = True
    p_death = 0.2
    p_reproduce = 0.2

    def kill(self):
        if random.random() <= self.p_death:
            self.alive = False

    def reproduce(self):
        if random.random() <= self.p_reproduce and self.alive:
            return Creature()

    

# %%
population = Population(n=5)

# %%
population.speciemens

# %%
population.n

# %%
population2 = Population(n=1000)

# %%
population2.n

# %%
{1, 1, 4, 7}

# %%
{1, 1, 4, 7} | {4, 7, 8}

# %%
{1, 1, 4, 7} - {4, 7, 8}

# %%
{1, 1, 4, 7} & {4, 7, 8}

# %%
{Creature()} * n

# %%
