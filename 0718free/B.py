import sys
import io


def main():
	read = sys.stdin.read
	readline = sys.stdin.readline
	readlines = sys.stdin.readlines
	func_list = []
	for i, l in enumerate(readlines()):
		if i == 0:
			N, M = map(int, l.split())
		elif i == 1:
			func_list.append(list(map(int, l.split())))
		else:
			l = list(map(int, l.split()))
			for func in func_list:
				if func[0] > l[0]:
					if compare(func, l):
						print("Yes")
						return
				elif func[0] == l[0]:
					if compare(func, l) or compare(l, func):
						print("Yes")
						return
				else:
					if compare(l, func):
						
						print("Yes")
						return
			func_list.append(l)
				
	print("No")

def compare(list_a, list_b):
#list_b > list_a
	if list_a[0] >= list_b[0]:
		Ca = list_a[1]
		Cb = list_b[1]
		start_b = 2
		Flag = False
		for i in range(2, Ca+2):
			Fa = list_a[i]
			for j in range(start_b, 2+Cb):
				if Fa == list_b[j]:
					start_b = j
					break
				elif Fa < list_b[j]:
					return False
				elif not Flag:
					Flag = True
				if j == 2 + Cb - 1:
					return False   
		
		if list_a[0] > list_b[0]:
			return True
		elif list_a[1] < list_b[1]:
			return True
		else:
			return False
	else:
		return False

def compare2(list_a, list_b):
	if list_a[0] >= list_b[0]:
		if set(list_b[2:]).issuperset(set(list_a[2:])):
			if list_a[0] > list_b[0] or list_a[1] < list_b[1]:
				return True
			

	

if __name__ == "__main__":
	main()
	#compare([4, 2, 2, 3], [3, 1, 2])
