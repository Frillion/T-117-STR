# T-117-STR1 Discrete Mathematics I
# Template for Individual assignment 5

test_set1 = [1,2,3,4] 
test_set2 = ['Alice','Bob','David','Eve']

test_relation1 = [(1,1),(1,3),(2,2),(2,3),(3,3),(4,4)]
test_relation2 = [('Alice','Bob'),('Bob','Alice')]
# Problem 1a)
def is_reflexive(defined_set, relation_on_set):
    for element in defined_set:
        if (element,element) not in relation_on_set:
            return False
        
    return True


print("\nReflective")
print(is_reflexive(test_set1,test_relation1))
print(is_reflexive(test_set2,test_relation2))

# Problem 1b)
def is_symmetric(relation_on_set):
    for relation in relation_on_set:
        if relation[0] == relation[1]:
            continue

        if (relation[1],relation[0]) not in relation_on_set:
            return False
    
    return True


print("\nSymetric")
print(is_symmetric(test_relation1))
print(is_symmetric(test_relation2))

# Problem 1c)
def is_antisymmetric(relation_on_set):
    for relation in relation_on_set:
        if relation[1] == relation[0]:
            continue

        if (relation[1],relation[0]) in relation_on_set:
                return False

    return True           

print("\nAntisymetric")
print(is_antisymmetric(test_relation1))
print(is_antisymmetric(test_relation2))

# Problem 1d)
def is_transitive(relation_on_set):
    for relationx in relation_on_set:
        for relationy in relation_on_set:
            if relationx[1] != relationy[0]:
                continue
            
            if (relationx[0],relationy[1]) not in relation_on_set:
                return False
    
    return True

print("\nTransitive")
print(is_transitive([(1,1),(2,2)]))
print(is_transitive([('Alice','Bob'),('Bob','Alice')]))


# Problem 2    
def is_equivalence_relation(defined_set, relation_on_set):
    return is_reflexive(defined_set,relation_on_set) and is_transitive(relation_on_set) and is_symmetric(relation_on_set)

print("\nEquivalence")
print(is_equivalence_relation(test_set1,[(1,1),(2,2),(3,3),(4,4),(1,2),(2,1)]))
print(is_equivalence_relation(test_set2,test_relation2))

# Problem 3
def composite_relations(relation1, relation2):
    composite = []
    for x, y in relation1:
        for a, b in relation2:
            if y == a:
                composite.append((x,b))

    return composite


print("\nComposite")
print(composite_relations([(2, 1), (3, 1), (3, 2), (4, 2)], [(1, 2), (1, 3), (2, 3), (2, 4), (3, 1)]))
print(composite_relations([('b','c'),('a','a'),('a','c'),('c','b')], [('b','a'),('a','c')]))

# Problem 4a)
def aces_in_relation_a(A):
    return #TODO Implement

# Problem 4b)
def aces_in_relation_b(A):
    return #TODO Implement

# Problem 4c)
def aces_in_relation_c(A):
    return #TODO Implement
   
# Problem 4d)
def aces_in_relation_d(A):
    return #TODO Implement
    
# Problem 5e)
def aces_in_relation_e(A):
    return #TODO Implement































            