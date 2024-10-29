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
def factorial(n):
    """Computes factorial.

    Arguments:
    n -- non-negative integer
    """

    if not isinstance(n, int) or n < 0:
        raise ValueError('Value of n should be a non-negative integer')
    
    result = 1
    for i in range(1, n+1):
        result *= i

    return result


# %%
factorial(5)

# %%
factorial('tralala')

# %%
factorial.__doc__

# %%
# ?factorial

# %%
