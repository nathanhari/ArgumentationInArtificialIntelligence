# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from numpy import matrix
import collections

class ArgumentationFramework:
    #def __init__(self, arguments, attacks):
    def __init__(self, attacks):
        self.arguments_ = list(range(attacks.shape[0]))
        self.attacks_ = attacks
    
    def make_iterable_(self, stuff):
        if(isinstance(stuff, collections.Iterable)):
            return(stuff)
        else:
            return([stuff])

    def is_conflict_free(self, arguments):
        arguments = self.make_iterable_(arguments)
        return(self.attacks_[np.ix_(arguments, arguments)].sum() == 0)
    
    def attacks_any(self, attacker, target):
        attacker = self.make_iterable_(attacker)
        target = self.make_iterable_(target)
        return(self.attacks_[np.ix_(attacker, target)].sum() > 0)
    
    def attacks_all(self, attacker, target):
        attacker = self.make_iterable_(attacker)
        target = self.make_iterable_(target)
        attack_agg = self.attacks_[np.ix_(attacker, target)].sum(axis=1)
        n_attacked = sum(attack_agg > 0)
        return (n_attacked == len(target))
    
    def attackers(self, target):
        target = self.make_iterable_(target)
        attack_columns = self.attacks_[np.ix_(self.arguments_, target)]
        attack_agg = attack_columns.sum(axis=1)
        attackers = [a for a in self.arguments_ if attack_agg[a] > 0]
        return(attackers)

    def acceptable(self, defenders, target):
        defenders = self.make_iterable_(defenders)
        target = self.make_iterable_(target)
        attackers = self.attackers(target)
        return(self.attacks_all(defenders, attackers))
    
    def admissable(self, defenders, target):
        return(self.acceptable(self, defenders, target))
            

args = [0, 1, 2]
att = matrix([[0, 1, 0],
              [0, 0, 1],
              [0, 0, 0]])
att[np.ix_([0, 2], [0, 2])]
#af = ArgumentationFramework(args, att)
af = ArgumentationFramework(att)
af.is_conflict_free([0, 1])
af.is_conflict_free([0, 2])
af.attacks_any(0, 1)
att[0, 1]
af.attacks_any([1, 2], 0)
att[np.ix_(args, [1, 2])]
af.attackers([1, 2])

