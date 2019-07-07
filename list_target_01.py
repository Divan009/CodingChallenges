a = [1,4,7,5]
b = [3,9,5,6]

def closest_sum(a1, a2, target):
	a1_sort = sorted(a1)
	a2_sort = sorted(a2)
	i = 0
	j = len(a2_sort) - 1

	small_diff = abs(a1_sort[0] + a2_sort[0] - target)
	close_pair = (a1_sort[0], a2_sort[0])

	while i < len(a1_sort) and j >= 0:
		v1 = a1_sort[i]
		v2 = a2_sort[j]
		curr_diff = v1 + v2 - target
		if abs(curr_diff) < small_diff:
			small_diff = abs(curr_diff)
			close_pair(v1,v2)

		if curr_diff == 0:
			return close_pair
		elif curr_diff < 0:
			i += 1
		else:
			j -= 1
	return close_pair

closest_sum(a,b,13)
