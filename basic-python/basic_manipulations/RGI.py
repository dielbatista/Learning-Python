"""Generator iterators are objects that allow you to iterate over a strea of 
data or large datasets without storing the entire dataset in memory at once. Instead, 
Generator iterators yield items on demand, which makes them memory efficient

with yield keyword, u can convert a normal python function into a generator function 
that return a generator iterator"""

def cumulative_average(numbers):
    total = 0
    for items, numbers in enumerate(numbers, 1):
        total += numbers
        yield total / items
    
values = [5, 3, 8, 2, 5] #simulates a large data set

for cum_average in cumulative_average(values):
    print(f"CUmulative Average: {cum_average:.2f}")
    
    
"""in this example, cumulative_average() is a generator that calculates and yields the
cumulative average of sequence of numbers. Because generator iterators yield items on 
demand, you only keep the original data in memory. The computed averages are generated
one by one, so at any given time, you only have one of those values in memory"""