name1, score1 = input().split()
name2, score2 = input().split()
name3, score3 = input().split()
name4, score4 = input().split()
name5, score5 = input().split()
dic = {name1:score1, name2:score2, name3:score3, name4:score4, name5:score5}

print("Which student's score?")
name = input()

if name in dic:
    print(name + "'s score: " + dic[name])
else:
    print(name + " is not in the database.")

    

