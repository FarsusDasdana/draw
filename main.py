import pandas as pd
import random

def kura(names:list, sample_size:int=2, seed:int=52):
  random.seed(seed)

  grp_list = []
  while len(names) > sample_size:
    grp = random.sample(names, sample_size)
    grp_list.append(grp)
    names = list(set(names) - set(grp))
  grp_list.append(names)
  return grp_list


# participant list
names = ['daenerys','sansa','jon','tyrion','joffrey','arya','ramsey','night king']
# roll the dice!
kura(names)