import math

score = {'score[1]' : 36, 'score[2]' : 42, 'score[3]' : 29, 'score[4]' : 55, 'score[5]' : 61,
         'score[6]' : 73, 'score[7]' : 51, 'score[8]' : 57, 'score[9]' : 78, 'score[10]' : -1}

vld_score = [s for s in score.values() if s != -1]
n = len(vld_score)
avr = sum(vld_score) / n

def calc_ssd(scorels, average):
    ssd = sum((s - average) ** 2 for s in scorels)
    return ssd

sum_sd = calc_ssd(vld_score, avr)
sd = math.sqrt(sum_sd / n)

print(n)
for key, value in score.items():
    print(key, ":", value)
print("Value of sd", sd)