scores = [96, 47, 113, 89, 100, 102]

counter = 0
for score in scores:
    if score >= 100:
        counter += 1
    # else:
    #     continue      <<< not necessary 
print(counter)

#list comprehension 
high_scores = [score for score in scores if score >= 100]
print(len(high_scores))