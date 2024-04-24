with open('words.txt', 'r') as file:
    words = [line.strip() for line in file]
max_length = max(len(word) for word in words)
longest_words = [word for word in words if len(word) == max_length]
for word in longest_words:
    print(word)
