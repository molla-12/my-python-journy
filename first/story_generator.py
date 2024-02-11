with open("story.txt", "r") as f:
    story = f.read()

# words = [] use set to remove duplicate
words = set()
# to fine the starting index of the word
start_of_word = -1
target_start = "<"
target_end = ">"
# enumerate give access to the postion as well as the element
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i         
    
    if char == target_end and start_of_word != -1:
        # start_of_word:i + 1 the plus 1 to not add the end
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1
# use dictionary
answars = {}
for word in words:
    answar = input("Enter the word for " + word)
    answars[word] = answar

for word in words:
    story = story.replace(word, answars[word])

with open("story.txt", "w") as f:
    f.write(story)
