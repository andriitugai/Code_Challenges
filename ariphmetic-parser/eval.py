import random
def get_rand_len(l):
    d = random.randint(10**(l-1), 10**(l)-1)
    return d

def write_to_file(filename, num, width):
    with open(filename, "w") as f:
        for _ in range(num):
            f.write(str(get_rand_len(width))+ '\n')


def get_num():
    with open("random_file.txt") as input_file:
        for line in input_file:
            yield int(line)

width = 8
write_to_file("random_file.txt", 1000, 8)
#  Choose number of buckets
num_buckets = 100
buckets = []
for idx in range(num_buckets):
    buckets.append(open(f"tmp{idx}.txt", "w"))

for num in get_num():
    # get num_of_bucket
    num_of_bucket = num // 10**(width - 2)
    print(num_of_bucket)
    buckets[num_of_bucket].write(str(num)+"\n")

for i in range(num_buckets):
    buckets[i].close()

for idx in range(num_buckets):
    lst = []
    with open(f"tmp{idx}.txt") as f:
        for line in f:
            lst.append(line)

    lst.sort()
    with open(f"tmp{idx}.txt","w") as f:
        for line in lst:
            f.write(line+"\n")

with open("sorted_file.txt", "w") as sorted_file:
    for idx in range(num_buckets):
        with open(f"tmp{idx}.txt") as f:
            for line in f:
                sorted_file.write(line + "\n")
