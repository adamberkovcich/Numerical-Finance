from LinearCongruential import*
from EcuyerCombined import*
from BoxMuller import*

uniform_lc = LinearCongruential(27, 17, 43, 100)
print("Linear Congruential gen: ")
for i in range(4):
    print(uniform_lc.Generate())
print("Mean and variance with Linear Congruential: ")
print(uniform_lc.Mean(10000))
print(uniform_lc.Variance(10000))


uniform_ec = EcuyerCombined()
print("Ecuyer Combined gen: ")
for i in range(4):
    print(uniform_ec.Generate())
print("Mean and variance with Ecuyer Combined: ")
print(uniform_ec.Mean(10000))
print(uniform_ec.Variance(10000))

normal_bm = BoxMuller(uniform_ec)
print("Box Muller gen: ")
for i in range(4):
    print(normal_bm.Generate())
print("Mean and variance with Box Muller: ")
print(normal_bm.Mean(10000))
print(normal_bm.Variance(10000))

normal_clt = CentralLimitThm(uniform_ec)
print("CLT gen: ")
for i in range(4):
    print(normal_clt.Generate())
print("Mean and variance with CLT: ")
print(normal_clt.Mean(10000))
print(normal_clt.Variance(10000))

