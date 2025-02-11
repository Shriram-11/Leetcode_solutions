def fullJustify(words, maxWidth):
	"""
	Justifies the given list of words such that each line has exactly maxWidth characters.

	:type words: List[str] - List of words to justify
	:type maxWidth: int - Maximum width of each line
	:rtype: List[str] - List of fully justified lines
	"""

	ans = []            # List to store the final justified lines
	curr_len = 0        # Current length of the line being processed
	temp = []           # Temporary list to hold words for the current line

	# Iterate through each word in the list
	for w in words:
		# Check if adding the new word exceeds the maxWidth
		if curr_len + len(w) > maxWidth:
			s = " ".join(temp)               # Join the current words with single spaces
			spaces = maxWidth - len(s)        # Calculate remaining spaces to be filled

			# If there's only one word, left-justify by adding spaces at the end
			if len(temp) == 1:
				s = s + " " * spaces
			else:
				s = ""                         # Reset the string to distribute spaces manually
				sp = spaces // (len(temp) - 1)  # Minimum spaces between words
				extra = spaces % (len(temp) - 1)  # Extra spaces to distribute evenly

				# Distribute spaces between words
				for i in range(0, len(temp) - 1):
					s = s + temp[i] + " " + " " * sp  # Add minimum spaces
					if i < extra:
						s += " "                    # Distribute extra space one by one
				s += temp[-1]                        # Add the last word without extra space

			ans.append(s)              # Add the justified line to the result
			temp = [w]                 # Start a new line with the current word
			curr_len = len(w) + 1      # Reset the current length (including space for next word)

		else:
			curr_len += len(w) + 1     # Add word length + 1 (for space) to the current line length
			temp.append(w)             # Add the word to the current line

	# Handle the last line (left-justified)
	if temp:
		s = " ".join(temp)             # Join remaining words with single spaces
		spaces = maxWidth - len(s)     # Calculate remaining spaces
		s = s + " " * spaces           # Add extra spaces to the end of the line
		ans.append(s)                  # Add the final line to the result

	return ans
