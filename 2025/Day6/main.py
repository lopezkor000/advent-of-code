"""
Cephalopod math doesn't look that different from normal math. The math worksheet (your puzzle input) consists of a list of problems; each problem has a group of numbers that need to be either added (+) or multiplied (*) together.

However, the problems are arranged a little strangely; they seem to be presented next to each other in a very long horizontal list. For example:

123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
Each problem's numbers are arranged vertically; at the bottom of the problem is the symbol for the operation that needs to be performed. Problems are separated by a full column of only spaces. The left/right alignment of numbers within each problem can be ignored.

So, this worksheet contains four problems:

123 * 45 * 6 = 33210
328 + 64 + 98 = 490
51 * 387 * 215 = 4243455
64 + 23 + 314 = 401
To check their work, cephalopod students are given the grand total of adding together all of the answers to the individual problems. In this worksheet, the grand total is 33210 + 490 + 4243455 + 401 = 4277556.

Of course, the actual worksheet is much wider. You'll need to make sure to unroll it completely so that you can read the problems clearly.

Solve the problems on the math worksheet. What is the grand total found by adding together all of the answers to the individual problems?
"""
def partOne():
	with open('input.txt', 'r') as input:
		problems = input.readlines()
		problems = [problem.strip().split() for problem in problems]
		equations = [list() for _ in problems[0]]
		for y in range(len(problems)):
			for x in range(len(problems[0])):
				equations[x].append(problems[y][x])
		output = 0
		for equation in equations:
			if equation[-1] == '+':
				total = 0
				for num in equation[:-1]:
					total += int(num)
			else:
				total = 1
				for num in equation[:-1]:
					total *= int(num)
			output += total
		print(f'Total: {output}')
partOne()
"""
--- Part Two ---
The big cephalopods come back to check on how things are going. When they see that your grand total doesn't match the one expected by the worksheet, they realize they forgot to explain how to read cephalopod math.

Cephalopod math is written right-to-left in columns. Each number is given in its own column, with the most significant digit at the top and the least significant digit at the bottom. (Problems are still separated with a column consisting only of spaces, and the symbol at the bottom of the problem is still the operator to use.)

Here's the example worksheet again:

123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  

Reading the problems right-to-left one column at a time, the problems are now quite different:

The rightmost problem is 4 + 431 + 623 = 1058
The second problem from the right is 175 * 581 * 32 = 3253600
The third problem from the right is 8 + 248 + 369 = 625
Finally, the leftmost problem is 356 * 24 * 1 = 8544
Now, the grand total is 1058 + 3253600 + 625 + 8544 = 3263827.

Solve the problems on the math worksheet again. What is the grand total found by adding together all of the answers to the individual problems?
"""
def partTwo():
	with open('input.txt', 'r') as input:
		problems = input.readlines()
		problemsStripped = [problem.strip().split() for problem in problems]
		equations = [list() for _ in problemsStripped[0]]

		for y in range(len(problemsStripped)):
			for x in range(len(problemsStripped[0])):
				equations[x].append(problemsStripped[y][x])
		
		charLengths = []
		for equation in equations:
			charLengths.append(max([len(part) for part in equation]))

		processed = []
		for length in charLengths:
			equation:list[str] = []
			for i, line in enumerate(problems):
				equation.append(line[:length])
				problems[i] = line[length+1:]
			# for i, item in enumerate(equation[:-1]):
			# 	equation[i] = item.replace(' ', '0')
			equation[-1] = equation[-1].strip()
			processed.append(equation)
		
		translated = []
		for eq in processed:
			new = ['' for _ in eq[0]]
			for num in eq[:-1]:
				for i,x in enumerate(num):
					new[i] += x
			new.append(eq[-1])
			translated.append(new)

		output = 0
		for equation in translated:
			if equation[-1] == '+':
				total = 0
				for num in equation[:-1]:
					total += int(num)
			else:
				total = 1
				for num in equation[:-1]:
					total *= int(num)
			output += total
		print(f'Total: {output}')
partTwo()