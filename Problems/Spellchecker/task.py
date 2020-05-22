dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

word = input().split()
new = [i for i in word if i not in dictionary]
print('\n'.join(new) if new else "OK")
