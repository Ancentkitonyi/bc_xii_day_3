def find_missing(list1, list2):
	set1 = set(list1)
	set2 = set(list2)
	missing = set1 ^ set2
	missing_list = list(missing)
	if missing_list == []:
		return 0
	for i in missing_list:
		return i