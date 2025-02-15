
def evalRPN(tokens):
	"""
	Evaluate the value of an arithmetic expression in Reverse Polish Notation (RPN).
	
	:param tokens: List[str] - A list of tokens representing the RPN expression.
	:return: int - The evaluated result of the RPN expression.
	"""

	# Stack to store operands
	stack = []

	def evaluate(operand1, operand2, operator):
		"""
		Perform the arithmetic operation based on the given operator.

		:param operand1: int - The first operand.
		:param operand2: int - The second operand.
		:param operator: str - The arithmetic operator (+, -, *, /).
		:return: int - The result of the operation.
		"""
		if operator == "+":
			return operand1 + operand2
		elif operator == "-":
			return operand1 - operand2
		elif operator == "/":
			# Perform division and truncate towards zero
			result = int(float(operand1) / operand2)
			return result
		else:  # operator == "*"
			return operand1 * operand2

	def is_operand(token):
		"""
		Check if a given token is an operand (number) or an operator.

		:param token: str - The token to check.
		:return: bool - True if the token is an operand, False if it is an operator.
		"""
		return token not in {"+", "-", "*", "/"}

	# Process each token in the given RPN expression
	for token in tokens:
		if is_operand(token):
			# Convert operand to integer and push onto the stack
			stack.append(int(token))
		else:
			# Pop the last two operands from the stack
			second_operand = stack.pop()  # Second operand (top of stack)
			first_operand = stack.pop()   # First operand (pushed earlier)
			
			# Evaluate and push the result back onto the stack
			stack.append(evaluate(first_operand, second_operand, token))

	# The final result will be the last remaining element in the stack
	return stack[-1]
