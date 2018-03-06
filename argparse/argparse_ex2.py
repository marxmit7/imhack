import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square",type= int , help="to get the square of a giver no")
parser.add_argument("-v","--verbose",type=int, help="optional arguments")
args = parser.parse_args()

answer = args.square**2

if args.verbose==2:
    print("the square of {} is {}".format(args.square,answer))
elif args.verbose==1:
    print("the answer is ",answer)

else:
    print(answer)