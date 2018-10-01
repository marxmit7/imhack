def binarySearch(myList, key):
	left = 0
	right = len(myList) - 1
	while(left <= right):
		mid = (left+right)//2
		if myList[mid] == key:
			print(str(key) + " is at " + str(mid+1) + " position.")
			return
		elif myList[mid] < key:
			left = mid+1
		else:
			right = mid-1
	print("Not found!")

def main():
	myList = [2,4,10,1,8,50]
	key = int(input("Enter the number you want to search: "))
	binarySearch(myList, key)

if __name__ == '__main__':
	main()