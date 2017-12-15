# Least Significant Digit Radix Sort

This python package implements a Radix Sorting algorithm using the Least Significant Digit (LSD) method, and extends it to deal with negative integers in an array. It retains the usual time complexity of O(kn), where k is number of digits in the longest input integer, and n is the number of elements in the array, with a space complexity of O(n + b). Furthermore, this is a stable sorting algorith, meaning that it maintains the relative order of lists with equal keys (or values). This implementation only sorts integers, both positive and/or negative (no strings, although this is possible with extended versions of Radix Sort).

Radix Sort is an interesting sorting algorithm because, unlike many other well-known sorting algorithms such as QuickSort and Merge Sort, Radix Sort is non-comparitive, meaning that it does not compare items in the original unsorted list to build its sorted list. Comparison algorithms that sort lists of significant size cannot do better than (a worst case of) O(nlogn); however, if you don't use comparisons, like with Radix Sort, this restriction does not necessarily apply. As such, Radix Sort can perform a lot faster than other sorting algorithms (albeit under very certain conditions, primarily shining in terms of efficiency when integers in the array-to-be-sorted are only a small amount of digits long). See the "Suggested Applications of Radix Sort" section in this Readme to understand when it is most appropriate to use this algorithm over other methods, and when other methods might be better.


## How the algorithm works

As mentioned, Radix Sort is a non-comparative integer sorting algorithm that, thanks to its stable sorting ability, can aid in sorting data with integer keys by grouping keys by the individual digits which share the same significant position and value.

This implementation of Radix Sort is called the Least Significant Digit (LSD) Radix Sort because we start by considering the right most digit of each integer and move towards the left (i.e. we start with the least significant digit and move toward the most significant digt). At each parse, we group together and order the digits that have the same underlying value and position using buckets (which are lists within a larger list in this python implementation). The bucketing method operates similarly to an algorithm called bucket sort. Overall, we parse through each least significant digit (which on the first run will be the digit to the extreme right side of each integer) in the input array, while at the same time parsing through the actual array elements from **left to right**, and we copy and store integers in the index of the bucket that matches the temporarily selected digit of the integer.

After an iteration of bucketing integers based on their considered digits, these integers are copied back over to the original array element, overwriting what was there before. 

This process is repeated as many times as there are digits in the longest integer in the array. After the last iteration (i.e. once all digits have essentially be parsed over from right to left in all array elements), the final copy over to the array from the buckets will be the fully sorted list.

Note that it is important we parse from **left to right** of array elements so that we retain the original relative positions of items in the array (i.e. when we reconstruct the sorted list from the buckets, entries in the bucket will be in the correct relative order when it's time for them to be copied back into a sorted array). As such this is a stable sorting algorithm.

It must be noted that this algorithm uses 0 as a pivot point to divide an unsorted input array into a positive and negative array. The two arrays are run through the Radix Sorting Procedure independently and merged back together at the end.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

All you need to utilize Radix Sort is Python 3! No additional packages needed – just good ol' native.

### Installing

Installing this package is a one-liner. It's hosted over at PyPi so just use the line below to get it on your local machine running Python 3.

```
pip install lsd_radixsort
```

If you can't seem to grab it from PyPi, you can download it from github using this [link](https://github.com/Sethfuchs/lsd_radixsort/archive/0.3.tar.gz). Then extract the file locally, navigate to its director on your command line, and execute (in the root):

~~~~
python setup.py install --user
~~~~

Then, in a python instance, you can import the module by running:

~~~~
from lsd_radixsort import lsd_radixsort
~~~~

You're ready to go! 


## Example Implementation

After installing lsd_radixsort onto your local machine, try running the following on a python compiler:

`
low_digit_test_array = [-20,1,4,5,-10,6,7,8,9,0,1,100]
`

`
lsd_radixsort.lsd_radixsort(low_digit_test_array)
`

The result should be:

`
'> [-20, -10, 0, 1, 1, 4, 5, 6, 7, 8, 9, 100]'
`

Due to the variable nature of k, you may want to use a random number generator to generate arrays with different k and n in order to see if Radix Sort will perform faster than, say Quicksort.


## Time Complexity

#### Quick definitions:

n : number of items in the array to be sorted

k : number of digits in the longest number in the array to be sorted

#### Analysis

As you can see from the code in lsd_radixsort.py, we are looking at n items frequently when creating buckets in ```bucketInitialzier()``` – in reality we will only parse through n items (in order to create the buckets) as many times as there are digits in the longest number in the input array. 

For example, if we have the following list

```[100, 5]```

...we will do one parse for every digit in the integer with the most digits (in this case, 3 parses). What this means is that every time there is a new digit to consider, we will have to parse through the list once more. Essentially, this translates to a best, average, and worst case complexity of **O(kn)**.

While we usually get rid of coefficients when using Big-O notation, in Radix Sort, we must keep k because we are not sure how big k might be every input array (i.e. in a general sense, we cannot be sure how many digits are in the largest integer; there are situations when this is known, however.). In Big-O, we generally want to keep the fastest growing term, but depending on the size of the digits of the input array, sometimes k can be very large or very inconsistent with most integers in the array. When this is the case, Radix Sort can be slower than comparison sorting methods that operate in a worst case of O(nlogn), which offers a more predictable and flexible time complexity.

For example, consider Radix Sort (O(kn)) versus Quicksort (O(nlogn)) in the following three cases (note: average case time complexity for Quicksort is being used here): 

1) an array of 500 integers, with the longest integer having **2 digits**

* Radix sort: n \* k = 500 \* 2 = 1000
* Quicksort: nlogn = 500log(500) = 1350
    * Here, Radix Sort performs faster

2) an array of 500 integers, with the longest integer having **9 digits**

* Radix sort: n \* k = 500 \* 9 = 4500
* Quicksort: nlogn = 500log(500) = 1350
    * Here, Quicksort performs faster

3) an array of 8 million integers, with the longest integer having **3 digits**

* Radix sort: n \* k = 8M \* 3 = 24M
* Quicksort: nlogn = 8Mlog(8M) = 55M
    * Here, Radix Sort performs faster

Overall, when k is less, Radix Sort wins. When it's high, it looses out to O(nlogn) algorithms. Notably though, unlike Radix Sort, Quicksort is independent of number of digits in a key, and because of that is tends to be more practical when dealing with diverse datasets.


## Space complexity

#### Quick definitions:

b : stands for 'base' and is essentially the total number of possible digits (or the Radix). In this implementation b is 10.

#### Analysis:

This implementation uses several storage mechanism to achieve the end result of O(n + b) space complexity.

The n part of this complexity comes from the fact that we first create two temporary lists of negative and positive integers, which are each independently radix sorted (list 1 + list 2 = size n). 

Decimal digits range from 0 to 9, thus, if we sort 2 decimal numbers (100, 5) using the radix sorting procedure for each digit (i.e using iterative bucket creation), it will create an array with a max size of b = 10, where b is the base.

This effectively means that the total space used during the entire period of bucket creation would be the total number of digits * (n + base). Assuming a constant number of total digits, the space complexity for Radix Sort is O(n + b).

This might not be a problem for a few kilobytes of data, but can be troubling when you have gigabytes of data (where Quicksort's O(logn) space complexity will be preferable).


## When should you use Radix Sort?

When you know the nature of your data, and your data tends to have lower k values, Radix Sort will save lots of time, but for very large data sets Radix Sort trades off time for additional (and sometimes not easily cacheable) space. For example, when your database has arrays consisting of millions of integers that have a lower k to the point where you save lots of time over Quicksort, and you can afford the space easily, use Radix Sort.

If you do not know your data well, and thus aren't sure about k, as well is if space comes at a big price and saving it is crucial, use the in-order comparison Quicksort or Merge Sort.


## Authors

* **Seth Michael Fuchs** - *All code and package set up*

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

## Acknowledgments

* Professor Phillip Sterne from the Minerva Schools at KGI for an excellent semester in algorithms that led to the inspiration to look further than the usual comparison algorithms into something unique like Radix Sort.
