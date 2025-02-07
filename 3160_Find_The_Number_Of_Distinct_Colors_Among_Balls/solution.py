
def queryResults(limit, queries):
	"""
	:type limit: int
	:type queries: List[List[int]]
	:rtype: List[int]
	"""
	# List to store the number of distinct colors after each query
	distinct_colors_after_queries = []

	# Dictionary to keep track of the count of each color
	color_count = dict()

	# Dictionary to map each ball to its current color
	ball_color_map = dict()

	# Process each query
	for query in queries:
		ball = query[0]   # Ball label
		color = query[1]  # Color to be assigned

		# If the ball is already colored
		if ball in ball_color_map:
			# Only update if the new color is different from the current color
			if ball_color_map[ball] != color:
				old_color = ball_color_map[ball]  # Store the current color before updating
				ball_color_map[ball] = color      # Update the ball with the new color

				# Decrease the count of the old color
				if old_color in color_count:
					if color_count[old_color] > 1:
						color_count[old_color] -= 1
					else:
						color_count.pop(old_color)  # Remove color if no balls have it anymore

				# Increase the count of the new color
				if color in color_count:
					color_count[color] += 1
				else:
					color_count[color] = 1

		# If the ball has not been colored yet
		else:
			ball_color_map[ball] = color  # Assign the color to the ball
			if color in color_count:
				color_count[color] += 1
			else:
				color_count[color] = 1

		# Append the current number of distinct colors to the result
		distinct_colors_after_queries.append(len(color_count))

	return distinct_colors_after_queries
