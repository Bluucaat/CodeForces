case_amount = int(input())
for i in range(case_amount):
    runners = list(map(int, input().split()))
    timur_score = runners[0]
    print(sum(1 for n in runners if n > timur_score))