def minimumPushes(word):
    """
    Calculate the minimum number of pushes required to type the given word 
    on a T9-like keypad where characters are mapped to push values based 
    on their frequency in descending order.

    :type word: str
    :rtype: int
    """
    # Dictionary to store character frequencies
    char_frequency = {}
    
    # Count the occurrences of each character in the word
    for char in word:
        if char not in char_frequency:
            char_frequency[char] = 0
        char_frequency[char] += 1
    
    # Convert dictionary items to a list and sort by frequency (descending)
    sorted_char_freq = list(char_frequency.items())
    sorted_char_freq.sort(key=lambda item: -item[1])
    
    # Dictionary to map characters to push values
    push_value_map = {}
    current_push_value = 1
    current_char_count = 0
    
    # Assign push values to characters based on their sorted frequency
    for char, freq in sorted_char_freq:
        push_value_map[char] = current_push_value
        current_char_count += 1
        
        # Increment push value every 9 characters
        if current_char_count % 9 == 0:
            current_push_value += 1
    
    # Calculate the total number of pushes needed for the word
    total_pushes = 0
    for char in word:
        total_pushes += push_value_map[char]
    
    return total_pushes
