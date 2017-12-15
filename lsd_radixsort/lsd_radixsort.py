# -*- coding: utf-8 -*-

# Note: This code has been verified for PEP8 compliance
# Final checks were performend with http://pep8online.com/

# set the Radix number to 10 because this function will only sort digits 0 -
# 9 (thus 10 characters in total) The Radix number is thus also used to
# assist with selecting the last digit of each number, iteratively as we
# move from right to left of each integer. See further comments for more
# information on this procedure
Radix = 10


def bucketInitialzier(array, decimal_placement, max_length):
    '''
    Takes in an unsorted array, initializes a temporary empty list of buckets
    according to the number of decimals up for analysis (10), analyzes each
    element in the array, and with each element, uses the decimal placement
    variable to analyze an individual digit of the element (going from right
    to left, called Least Signficant Decimal analysis). Relative to the digit
    being analyzed, the element will be placed into a bucket.

    Returns the temporary bucket list, as well as max_length which tells
    follow up functions whether all digits have been analyzed.

    Argument descriptions:

    array: list
        an unsorted array

    decimal_placement: int
        an integer that aids in the selection of the right-most un-analyzed
        digit during the bucketing procedure. After each full bucketing
        procedure for a group of digits, this integer increases by an order
        of magnitude to aid in the selection of the next, right-most digit
        from an element

    max_length: boolean
        helps determine whether all the digits from all integers in the array
        have been analyzed or not.

        True: all digits have been analyzed
        False: there are still digits left to analayze

    '''
    global Radix
    # initialize the buckets for this iteration we will use buckets to sort
    # individal digits in each element into its respective bucket based on
    # its index. Thus, the number of buckets much match the Radix number,
    # which is 10

    temp_bucket_list = [[] for x in range(Radix)]

    for i in array:
        # Radix sort begins by analzying each digit at the extreme
        # right side of each integer. This is called Least Signficant Decimal
        # (LSD) analysis. These digits are added to buckets initialize above,
        # and then re-added back into a list, until the last digit has been
        # analyzed, whereafter the list is in sorted order.

        # Thus, to select the appropriate digit in each iteration, we use the
        # selected_temp_integer variable below to ensure we are dealing with
        # the right part of the integer.

        # FOR EXAMPLE, if we are on the second iteration of the Radix Sort,
        # our new decimal_placement value will be 10 (since we now want to
        # conider only the second last value of the integer. Say that the full
        # number we are trying to bucket is 105. We considered and bucketed
        # '5' in the last iteration, and we now want to consider the 0
        # (recall that we iteratively bucket and re-sort from right to left
        # digit for each integer in Radix Sort, consentrating on one deciminal
        # point for each integer for each iteration of bucketing.). In order
        # to consider the 0, we need to reduce 105 to just 10 (a later query
        # will grab the 0, read on...). This is done by dividing the element
        # (105) by the current declimal placement (which is 10, because we're
        # on the second iteration). 105/10 is 10.5. The numbers after the
        # decimal point are discarded in this function.
        selected_temp_integer = i / decimal_placement

        # Following the previous example, we want to now grab the last digit
        # from our newly created temporary integer. We can do this by modding
        # the temporary integer with our Radix number (e.g. (105 / 10) % 10
        # = 0)
        selected_digit = selected_temp_integer % Radix

        # Now, we will add the entire element to a bucket based on its
        # selected digit, using the digit as an index indicator. Following
        # from the previous example, the integer 105 will be placed into a
        # bucket based on the its currently select digit – thus 105 will go
        # into the first bucket in the list of buckets (bucket[0]). Also take
        # note that because we are iterating through elements in our original
        # list from left to right, we will retain the correct relative order
        # of digits, should any digits be the same during a certain iteration.
        # If a bucket already has the same digit in it from a previous
        # iteration, the newly considered digital will just append to the end
        # of the list in that bucket. This makes Radix Sort a stable sorting
        # algorithm!

        temp_bucket_list[selected_digit].append(i)

        # both selected_temp_integer and max_length must be greater than 0
        # to set this to False and keep the while loop going in
        # radix_sorting_procedure(). When the selected_temp_integer is 0 AND
        # max_length is False (meaning that we have no more digits left to
        # analyze), it means this is bucketInitialzier()'s last run. It will
        # not run again.
        if selected_temp_integer and max_length > 0:
            max_length = False

    return temp_bucket_list, max_length


def add_bucket_to_list(array, temp_bucket_list):
    '''
    Take in unsorted array and a list of buckets outputted from
    bucketInitialzier(), and according to how integers have been placed in
    buckets, re-enters them back into the array, overwriting what was there
    before. On the last iteration (i.e when all digits have been analyzed,
    bucketed in relation to their respective analyzed digits, the respective
    list will be fully sorted)

    Arguments:

    array: list
        originally the unsorted list, iteratively re-filled by buckets
        generated by bucketInitialzier() during the Radix Sort procedure
    '''
    global Radix
    # a tracker is intialized to 0 so that we can integers to the correct
    # place in the new array

    index_tracker = 0

    # for each bucket in the bucket list
    for bucket in range(Radix):

        # there may be buckets with multiple elements, thus we must use
        # another for-loop to make sure we iterative over all elements in
        # each bucket
        sub_bucket = temp_bucket_list[bucket]
        for element in sub_bucket:

            # following index order of buckets, add element back into main
            # array
            array[index_tracker] = element
            index_tracker += 1

    return array


def split_absolute_pos_neg(array):
    '''
    Takes in one array, iterates over each element in the array, and splits
    elements depending on their valence (positive including 0, or negative)

    Return two arrays – one of the positive integers, and one of originally
    identified negative numbers that have been multipled by negative one
    (necessary for the Radix Procedure. See end ofradixSort() to see how
    negative numbers from this output are sorted, then reversed, and negated
    to be joined with the positive sorted list)

    Use in context: Aids Radix Sort by extending the algorithm to sort a
    list that contains both positive and negative numbers

    Arguments:

    array: list
        of integers only
    '''
    positive = []
    negative = []
    for i in array:
        if i >= 0:
            positive.append(i)
        else:
            negative.append(-1*i)
    return positive, negative


def radix_sorting_procedure(array):
    '''
    Takes in an unsorted array of positive or negative integers and
    executes the subroutines necessary to sort the list. The function returns
    the sorted version of the array parsed into it. This function is separate
    from the lsd_radixsort() function below so as to accomodate the separate
    sorting procedures for positive and negative integers.
    '''
    # Buckets should be initialized up to the point where we have reached the
    # maximum number of digits for the integer in the list that has the most
    # amount of digits. Thus, we do not need to initialize any more buckets
    # once we have iterated over all digits of all integers, and at this
    # point the  radix sorting mechanism is complete (max_length reached; =
    # True)
    max_length = False
    decimal_placement = 1

    while max_length is False:

        # immediately set max_length to True (assumption), so that we
        # may initiate a test at the end of this bucketInitialzier() for
        # whether we have in fact reached the maximum digit place of all
        # integers
        max_length = True

        temp_bucket_list, max_length = bucketInitialzier(array,
                                                         decimal_placement,
                                                         max_length)

        abs_negative_array = add_bucket_to_list(array, temp_bucket_list)

        decimal_placement *= Radix

    return array


def lsd_radixsort(array):
    '''
    Executes the radix sorting procedure using supplementary functions within
    this module.

    This is the function that must be called upon from the lsd_radixsort
    module to sort a given array of intergers.

    Primary reason for separation of this function from
    radix_sorting_procedure() above is to faciliate the splitting of
    positive and negative integers for independent radix sorting and
    re-merging.

    Arguments:

    array: list
        unsorted list of integers that the function will sort using radix
        sorting
    '''

    # Tests
    # raise error if empty list
    if len(array) >= 1:
        pass
    else:
        raise Exception('Your list must contain one or more integer in order \
            for Radix sort to operate')

    # TEST: RadixSort can not sort floating decimal numbers
    if all(isinstance(item, int) for item in array) is True:
        pass
    else:
        raise Exception('This function can only sort integers without \
            decimal floats.')

    # original Radix Sort modified to include negative number analysis
    # Procedure: split original unsorted input array into positive and
    # negative numbers (one parse through entire list), and run
    # Radix sort on both lists separately (Note: in order for Radix
    # Sort procedure to work on the negative integer list, we must
    # first convert all integers in the list to positive (*-1, this
    # split_pos_neg() function)). Afterwards, the list is negated and
    # reversed, and merged with the positive sorted list to form a
    # complete sorted list
    positive_array, abs_negative_array = split_absolute_pos_neg(array)

    # Radix value will always be 10, since the procedure will
    # analyze digits 0 - 9, 10 digits total, in order to sort
    # integers into buckets – see the bucketInitialzier() function

    sorted_positive_array = radix_sorting_procedure(positive_array)

    # save time by not sorting the negative portion of the input array
    # if there were no negative numbers in the initial unsorted array
    if len(abs_negative_array) >= 1:
        sorted_abs_negative_array = radix_sorting_procedure(abs_negative_array)

        temp_negative_array = list(reversed(sorted_abs_negative_array))
        sorted_negative_array = [-x for x in temp_negative_array]
        return sorted_negative_array + sorted_positive_array

    else:
        # simply return only the previously sorted positive array (which is
        # essentially the entire original array, now sorted)
        return sorted_positive_array


# testing
# big_array = random.sample(range(-1000, 10000), 10000)
# test_array = [-20,1,4,5,-10,6,7,8,9,0,1,100]
# neg_only_array = [-20,-100,-5,-3,-1000,-10000,-10430343,-50,-3]
# test_empty_array = [1,2]
# print lsd_radixsort(neg_only_array)
