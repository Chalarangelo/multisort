import sys
import random
import time

# Number of sorting algorithms
NUM_OF_SORTERS = 10

# Runs one full pass of the bubble sort algorithm
def bubble_sort(items):
	for i in range(len(items)-1):
		if items[i] > items[i+1]: items[i], items[i+1] = items[i+1], items[i]

# Runs the insertion sort algorithm until the swaps reach timeout
def insertion_sort(items, timeout):
	swaps = 0
	for j in range(1, len(items)):
		while j > 0 and items[j] < items[j-1] and swaps < timeout:
			items[j], items[j-1], j, swaps = items[j-1], items[j], j-1, swaps+1

# Runs merge sort algorithm for a subset of the list (from start to stop-1)
def merge_sort(items, start, stop):
	if len(items) > 1:
		mid = int((stop-start)/2)
		left, right = items[start:start+mid], items[start+mid:stop]
		merge_sort(left,0,len(left))
		merge_sort(right,0,len(right))
		l, r = 0, 0
		for i in range(start,stop):
			lval, rval = left[l] if l < len(left) else None, right[r] if r < len(right) else None
			if (lval and rval and lval < rval) or rval is None: items[i], l = lval, l+1
			elif (lval and rval and lval >= rval) or lval is None: items[i], r = rval, r+1
			else: raise Exception('Could not merge, arrays do not match original!')

# Runs quick sort algorithm by splitting the list into two sublists (lower and upper and then merging them)
def quick_sort(items, pivot_index):
	items[:] = [i for i in items if i < items[pivot_index]] + [i for i in items if i >= items[pivot_index]]

# Runs the selection sort algorithm for a specific position in the list
def selection_sort(items, sorted_items, position):
	items[items.index(sorted_items[position])], items[position]  = items[position], sorted_items[position]

# Runs the bucket sort algorithm by properly assigning elements to a number of buckets
def bucket_sort(items, bucket_count):
	buckets =[[] for _ in range(bucket_count)]
	for i in items: buckets[i * bucket_count//(max(items)+1)].append(i)
	items[:] = sum([b for b in buckets],[])

# (DONTUSE) Runs the radix sort for the LSD of each element in the list
def radix_sort(items):
	buckets =[[] for _ in range(10)]
	for i in items: buckets[i%10].append(i)
	items[:] = sum([b for b in buckets],[])

# Runs one iteration of the patience sort algorithm
def patience_sort(items):
	piles = [[items[0]]]
	for (i,p_count) in [(i,p_count) for i in items[1:] for p_count in range(1)]:
		for p in piles:
			if p[len(p)-1] <= i:
				p.append(i)
				break
			else: p_count += 1
		if p_count == len(piles): piles.append([i])
	items[:] = sum([p for p in piles],[])

# Runs the gnome sort algorithm on a subset of the data
def gnome_sort(items, start, stop):
	pos = start
	while pos < stop:
		if(pos == start or items[pos] >= items[pos-1]): pos = pos + 1
		else: items[pos], items[pos-1], pos = items[pos-1], items[pos], pos -1

# Runs a step of the odd-even sort algorithm, based on the value provided
def odd_even_sort(items, start):
	if start != 0: start = 1
	for i in range(start, len(items)-1, 2):
		if items[i] > items[i+1]: items[i], items[i+1] = items[i+1], items[i]

# Runs the stooge sort algorithm on a subset of the data
def stooge_sort(items, start, end):
	if items[end] < items[start]: items[end], items[start] = items[start], items[end]
	if (end-start) > 1:
		t = (end-start+1)//3
		stooge_sort(items,start,end-t)
		stooge_sort(items,start+t,end)
		stooge_sort(items,start,end-t)

if len(sys.argv) < 3:
	print('Error! Please use "', str(sys.argv[0]),' [filename] [seed] [full_output]" to run the multisort program')
	print('[filename] - The name of the file from where the values will be read (space delimited).')
	print('[seed] - The seed used for the randomizer.')
	print('[full_output] - (Optional) 1 or 0 (1 meaning print all information, 0 print only the results).')
	print()
	sys.exit()
else:
	# Read data from file and create the numbers list
	numbers = [int(n) for n in ' '.join([line.strip() for line in open(str(sys.argv[1]))]).split()]
	debug = False
	if(len(sys.argv) > 3 and int(sys.argv[3]) == 1): debug = True
	# If the list is too short, exit
	if len(numbers) < 10:
		print('Please use a list of 10 or more elements! The program is now terminating...')
		print()
		sys.exit()
	# Create the required sorted list for checking, as well as the root length
	sorted_numbers, root_len = sorted(numbers), int(len(numbers)**(1/2))
	if debug:
		print('Length:',len(numbers),'Root:',root_len,'Min:',min(numbers),'Max:',max(numbers),'Sum:',sum(numbers))
		print('List:', numbers)
		print()
	# Start randomizer, iterator and timer
	random.seed(int(sys.argv[2]))
	iter, start_time = 0, time.time()
	# Loop over the data
	while (numbers != sorted_numbers):
		sorter = random.randint(0,NUM_OF_SORTERS-1)
		if sorter == 0:
			bubble_sort(numbers)
		elif sorter == 1:
			selection_sort(numbers, sorted_numbers, random.randint(0,len(numbers)-1))
		elif sorter == 2:
			insertion_sort(numbers, root_len)
		elif sorter == 3:
			bucket_sort(numbers, random.randint(2,3*root_len//4))
		elif sorter == 4:
			quick_sort(numbers, random.randint(0,len(numbers)-1))
		elif sorter == 5:
			start_pos = random.randint(0,len(numbers)-root_len-1)
			merge_sort(numbers, start_pos, random.randint(start_pos+root_len//3, start_pos+root_len-1))
		elif sorter == 6:
			start_pos = random.randint(0,len(numbers)-root_len-1)
			gnome_sort(numbers, start_pos, random.randint(start_pos+root_len//3, start_pos+root_len-1))
		elif sorter == 7:
			patience_sort(numbers)
		elif sorter == 8:
			odd_even_sort(numbers, random.randint(0,1))
		elif sorter == 9:
			start_pos = random.randint(0,len(numbers)-root_len-1)
			stooge_sort(numbers, start_pos, random.randint(start_pos+root_len//3, start_pos+root_len-1))
		if debug:
			print('Iteration',iter)
			print('List:', numbers)
			print()
		iter += 1
	# Get time and iterator
	end_time = time.time()
	print('Sorting completed after',iter,'steps, taking',end_time-start_time,'seconds.')
	print()
	print('List:', numbers)
	print()
