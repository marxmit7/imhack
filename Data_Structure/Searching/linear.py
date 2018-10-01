def linearSearch(myList, key):
	for i in range(len(myList)):
		if myList[i] == key:
			print(str(key) + " is at " + str(i+1) + " position.")
			return
	print("Not found!")

def main():
	myList = [2,4,10,1,8,50]
	key = int(input("Enter the number you want to search: "))
	linearSearch(myList, key)

if __name__ == '__main__':
	main()