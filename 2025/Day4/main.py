"""
If you can optimize the work the forklifts are doing, maybe they would have time to spare to break through the wall.

The rolls of paper (@) are arranged on a large grid; the Elves even have a helpful diagram (your puzzle input) indicating where everything is located.

For example:

..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.

The forklifts can only access a roll of paper if there are fewer than four rolls of paper in the eight adjacent positions. If you can figure out which rolls of paper the forklifts can access, they'll spend less time looking and more time breaking down the wall to the cafeteria.

In this example, there are 13 rolls of paper that can be accessed by a forklift (marked with x):

..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.

Consider your complete diagram of the paper roll locations. How many rolls of paper can be accessed by a forklift?
"""
def partOne():
	with open('input.txt', 'r') as input:
		lines = input.readlines()
		lines = [list(line.strip()) for line in lines]

		# [print(line) for line in lines]

		# print("~ ~ ~ V ~ ~ ~")

		counts = [[0 for _ in line] for line in lines]

		for y in range(len(lines)-1):
			for x in range(len(lines[0])):
				if lines[y][x] == '@':
					counts[y+1][x] += 1
		for y in range(len(lines)-1,0,-1):
			for x in range(len(lines[0])):
				if lines[y][x] == '@':
					counts[y-1][x] += 1
		for x in range(len(lines)-1):
			for y in range(len(lines[0])):
				if lines[y][x] == '@':
					counts[y][x+1] += 1
		for x in range(len(lines)-1,0,-1):
			for y in range(len(lines[0])):
				if lines[y][x] == '@':
					counts[y][x-1] += 1
		
		for y in range(len(lines)-1):
			for x in range(len(lines[0])-1):
				if lines[y][x] == '@':
					counts[y+1][x+1] += 1
		for y in range(len(lines)-1):
			for x in range(len(lines[0])-1,0,-1):
				if lines[y][x] == '@':
					counts[y+1][x-1] += 1
		for y in range(len(lines)-1,0,-1):
			for x in range(len(lines[0])-1):
				if lines[y][x] == '@':
					counts[y-1][x+1] += 1
		for y in range(len(lines)-1,0,-1):
			for x in range(len(lines[0])-1,0,-1):
				if lines[y][x] == '@':
					counts[y-1][x-1] += 1

		total = 0
		for y in range(len(lines)):
			for x in range(len(lines[0])):
				if lines[y][x] == '@' and counts[y][x] < 4:
					lines[y][x] = 'x'
					total += 1

		# [print(line) for line in lines]
		# [print(count) for count in counts]
		print(f'Output: {total}')
partOne()
"""
--- Part Two ---
Now, the Elves just need help accessing as much of the paper as they can.

Once a roll of paper can be accessed by a forklift, it can be removed. Once a roll of paper is removed, the forklifts might be able to access more rolls of paper, which they might also be able to remove. How many total rolls of paper could the Elves remove if they keep repeating this process?

Starting with the same example as above, here is one way you could remove as many rolls of paper as possible, using highlighted @ to indicate that a roll of paper is about to be removed, and using x to indicate that a roll of paper was just removed:

Initial state:

..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.

Remove 13 rolls of paper:

..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.

Remove 12 rolls of paper:

.......x..
.@@.x.x.@x
x@@@@...@@
x.@@@@..x.
.@.@@@@.x.
.x@@@@@@.x
.x.@.@.@@@
..@@@.@@@@
.x@@@@@@@.
....@@@...

Remove 7 rolls of paper:

..........
.x@.....x.
.@@@@...xx
..@@@@....
.x.@@@@...
..@@@@@@..
...@.@.@@x
..@@@.@@@@
..x@@@@@@.
....@@@...

Remove 5 rolls of paper:

..........
..x.......
.x@@@.....
..@@@@....
...@@@@...
..x@@@@@..
...@.@.@@.
..x@@.@@@x
...@@@@@@.
....@@@...

Remove 2 rolls of paper:

..........
..........
..x@@.....
..@@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@x.
....@@@...

Remove 1 roll of paper:

..........
..........
...@@.....
..x@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:

..........
..........
...x@.....
...@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:

..........
..........
....x.....
...@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:

..........
..........
..........
...x@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Stop once no more rolls of paper are accessible by a forklift. In this example, a total of 43 rolls of paper can be removed.

Start with your original diagram. How many rolls of paper in total can be removed by the Elves and their forklifts?
"""
def removeRolls(rolls):
	counts = [[0 for _ in line] for line in rolls]
	for y in range(len(rolls)-1):
		for x in range(len(rolls[0])):
			if rolls[y][x] == '@':
				counts[y+1][x] += 1
	for y in range(len(rolls)-1,0,-1):
		for x in range(len(rolls[0])):
			if rolls[y][x] == '@':
				counts[y-1][x] += 1
	for x in range(len(rolls)-1):
		for y in range(len(rolls[0])):
			if rolls[y][x] == '@':
				counts[y][x+1] += 1
	for x in range(len(rolls)-1,0,-1):
		for y in range(len(rolls[0])):
			if rolls[y][x] == '@':
				counts[y][x-1] += 1
	
	for y in range(len(rolls)-1):
		for x in range(len(rolls[0])-1):
			if rolls[y][x] == '@':
				counts[y+1][x+1] += 1
	for y in range(len(rolls)-1):
		for x in range(len(rolls[0])-1,0,-1):
			if rolls[y][x] == '@':
				counts[y+1][x-1] += 1
	for y in range(len(rolls)-1,0,-1):
		for x in range(len(rolls[0])-1):
			if rolls[y][x] == '@':
				counts[y-1][x+1] += 1
	for y in range(len(rolls)-1,0,-1):
		for x in range(len(rolls[0])-1,0,-1):
			if rolls[y][x] == '@':
				counts[y-1][x-1] += 1

	total = 0
	for y in range(len(rolls)):
		for x in range(len(rolls[0])):
			if rolls[y][x] == '@' and counts[y][x] < 4:
				rolls[y][x] = 'x'
				total += 1
	if total == 0:
		return 0
	return total + removeRolls(rolls)

def partTwo():
	with open('input.txt', 'r') as input:
		lines = input.readlines()
		lines = [list(line.strip()) for line in lines]
		total = removeRolls(lines)
		print(f'Output: {total}')
partTwo()