from array import array

vetor_inteiros = array('b', [1, 2, 3])
print(vetor_inteiros)

# 1 / 2 / 3 / 4

vetor_inteiros.insert(3, 4)

print(vetor_inteiros)

print(vetor_inteiros.index(2))