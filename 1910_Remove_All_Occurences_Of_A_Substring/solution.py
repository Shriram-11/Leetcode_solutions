def removeOccurrences(s, part):
	"""
	:type s: str  # The input string in which we want to remove occurrences of 'part'
	:type part: str  # The substring 'part' we need to remove from 's'
	:rtype: str  # The modified string after removing all occurrences of 'part'
	"""
	
	len_s = len(s)  # Length of the input string 's'
	len_part = len(part)  # Length of the substring 'part'
	found_occurrence = True  # Flag to indicate if we found 'part' in 's'

	# Continue until no more occurrences of 'part' are found or the string is too short
	while found_occurrence and len(s) >= len_part:
		found_occurrence = False  # Reset the flag for each iteration
		# Iterate over possible starting indices of 'part' in 's'
		for i in range(len(s) - len_part + 1):
			# Check if the substring starting at index 'i' matches 'part'
			if s[i] == part[0] and s[i:i+len_part] == part:
				found_occurrence = True  # Set flag to True to indicate 'part' was found
				s = s[:i] + s[i + len_part:]  # Remove 'part' from 's'
				break  # Exit loop and restart searching for more occurrences

	return s  # Return the final string after all occurrences of 'part' are removed
