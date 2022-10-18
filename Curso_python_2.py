
list_nested = []
scores = []
names_2lowest_score = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    list_nested.append([name,score])
    
    if score > 0:
        scores.append(score)
    else:
        continue

sorted(list(set(scores)))
names_2lowest_score = [list_nested[i][0] for i in range(0, len(list_nested)) if list_nested[i][1] == scores[1]]
names_2lowest_score.sort()
for name in names_2lowest_score:
    print(name)
