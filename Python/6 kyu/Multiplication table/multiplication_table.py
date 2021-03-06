#Description:
#Your task, is to create NxN multiplication table, of size provided in parameter.
def multiplication_table(size):
    return [[i*j for i in range(1,size+1)] for j in range(1,size+1)]