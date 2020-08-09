# Convert text to Smileys
message = input('> ').lower()
words = message.split(' ')

# mapping special characters to smileys i.e windows + ;
emojis = {
    ':)': '😊',  # happy
    ':(': '😞',  # sad
    '*': '😘',   # kiss
    ':x': '🤐',  # lips sealed
    ':o': '🥱'   # yawn
}

output = ''
for word in words:
    output += emojis.get(word, word) + ' '  # if word is not in emojis, return word
print(output)
