#Convert text to Smileys
def emoji_converter(message):
	words = message.split(' ')
	#mapping special characters to smileys using windows + ;
	emojis = {
	    ':)': '😊',  #happy
	    ':(': '😞',  #sad
	    '*': '😘',   #kiss
	}

	output = ''
	for word in words:
		output += emojis.get(word, word) + ' ' #if word is not in emojis, return word
	return output


message = input('> ')
print(emoji_converter(message))
