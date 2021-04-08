from datetime import datetime
# read and write in text file

# --------start--------
import sys

sys.stdin = open("../input.txt", "r")
sys.stdout = open("../output.txt", "w")

# --------end--------

# Complete the time_delta function below.
def time_delta(t1, t2):
    date_string = "%a %d %b %Y %H:%M:%S %z"
    return str(int(abs(datetime.strptime(t1, date_string) - datetime.strptime(t2, date_string)).total_seconds()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()