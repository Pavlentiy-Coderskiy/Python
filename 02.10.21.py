oSet = set()
oSet2 ={0}
oSet3 = oSet.union()
oSet.add("Raptor") 
oSet.add("Tiranozavr")
oSet.add("Tiranozavr")
print(oSet.isdisjoint(oSet2))
print(oSet)
oSet2.update(oSet)
print(oSet3)
print(oSet.issubset(oSet3))
print(oSet3.issubset(oSet))
print(oSet.intersection(oSet3))
print(oSet.difference(oSet3))
print(oSet.symmetric_difference(oSet3))
oSet.intersection_update(oSet3)
oSet.difference_update(oSet3)
oSet3.symmetric_difference_update(oSet3)
oSet.discard("Raptor")
oSet.remove("Raptor")
oSet.pop()








