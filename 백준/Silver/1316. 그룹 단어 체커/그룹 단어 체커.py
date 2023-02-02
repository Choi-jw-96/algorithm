T = int(input())
cnt = 0

for t in range(T):
    word = input()
    word_dic = {}
    line_word = ""
    for s in word:
        if s not in word_dic:
            word_dic[s] = 1
        else:
            word_dic[s] += 1
    
    for K, V in word_dic.items():
        line_word += K * V
    
    if line_word == word:
        cnt += 1
print(cnt)