from sys import path

path.append('../packages')

# ex1

# import extra.iota
# print(extra.iota.FunI())

# ex2

# from extra.iota import FunI
# print(FunI())

# ex3

# import extra.good.best.sigma
# from extra.good.best.tau import FunT

# print(extra.good.best.sigma.FunS())
# print(FunT())

# ex4

import extra.good.best.sigma as sig
import extra.good.alpha as alp

print(sig.FunS())
print(alp.FunA())


