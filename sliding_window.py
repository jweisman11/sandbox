# Author: Jeff Weisman
# Date Created:  2022-09-11
# Description: Learning the `sliding window` technique
# Challenge:  Given an array of integers of size ‘n’, calculate the maximum sum of ‘k’ consecutive elements in the array.
# https://www.geeksforgeeks.org/window-sliding-technique/


# Import libraries
import os
import sys
import time


# Decorator to measure performance
# https://stackoverflow.com/questions/57409385/how-do-i-see-the-time-it-took-to-run-my-program-in-visual-studio-code
def decoratortimer(decimal):
    def decoratorfunction(f):
        def wrap(*args, **kwargs):
            time1 = time.monotonic()
            result = f(*args, **kwargs)
            time2 = time.monotonic()
            print('{:s} function took {:.{}f} ms'.format(f.__name__, ((time2-time1)*1000.0), decimal ))
            return result
        return wrap
    return decoratorfunction


# BRUTE FORCE APPROACH
@decoratortimer(10)
def sliding_window_brute(arr: list, k: int) -> int:
    '''
    Uses nested for loop to evaluate all possible combinations
    '''

    max_sum = 0

    if len(arr) < k:
        return -1

    for i in range(0, len(arr) - k):
        current_sum = 0
        for j in range(0, k):
            current_sum += arr[i + j]

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum


INT_ARRAY = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
print(sliding_window_brute(INT_ARRAY, k))

INT_ARRAY = [1, 4]
k = 4
print(sliding_window_brute(INT_ARRAY, k))

INT_ARRAY = [237, 91, 273, 972, 454, 698, 74, 716, 609, 271, 619, 844, 141, 371, 668, 393, 604, 754, 423, 282, 812, 206, 190, 998, 838, 229, 527, 731, 182, 43, 867, 979, 759, 353, 825, 851, 416, 402, 205, 285, 392, 973, 599, 94, 623, 60, 290, 181, 429, 767, 153, 168, 332, 897, 947, 541, 688, 451, 920, 105, 36, 7, 19, 692, 378, 610, 71, 854, 328, 475, 529, 795, 942, 447, 202, 865, 167, 532, 96, 219, 729, 165, 579, 303, 514, 967, 570, 728, 718, 762, 902, 112, 715, 881, 34, 198, 608, 13, 293, 377, 615, 955, 631, 22, 963, 245, 893, 122, 411, 179, 980, 745, 405, 450, 526, 948, 327, 643, 898, 188, 997, 722, 295, 508, 260, 542, 974, 430, 903, 54, 651, 684, 42, 773, 949, 1, 593, 755, 439, 174, 874, 247, 569, 448, 222, 142, 252, 115, 93, 477, 277, 756, 517, 331, 968, 40, 789, 498, 705, 102, 366, 971, 73, 894, 341, 563, 374, 763, 560, 396, 35, 155, 534, 195, 630, 552, 503, 804, 732, 460, 359, 336, 44, 616, 484, 544, 647, 233, 386, 291, 145, 727, 17, 266, 820, 653, 509, 129, 632, 215, 689, 418, 900, 645, 823, 910, 80, 343, 408, 10, 877, 307, 184, 55, 301, 449, 375, 363, 564, 139, 983, 538, 474, 138, 387, 856, 485, 312, 969, 697, 611, 83, 907, 203, 730, 37, 497, 582, 412, 726, 279, 242, 137, 14, 250, 771, 670, 809, 384, 928, 709, 16, 136, 605, 457, 409, 150, 523, 131, 235, 270, 574, 488, 308, 99, 970, 344, 540, 781, 267, 811, 175, 63, 426, 210, 993, 832, 199, 806, 883, 21, 774, 965, 211, 57, 650, 577, 492, 67, 272, 50, 128, 975, 345, 213, 944, 321, 189, 358, 661, 699, 735, 589, 895, 323, 158, 424, 918, 956, 662, 201, 545, 381, 749, 79, 208, 435, 407, 480, 397, 521, 827, 470, 275, 833, 231, 996, 981, 276, 801, 510, 704, 263, 364, 862, 665, 180, 923, 38, 191, 880, 465, 712, 81, 365, 107, 660, 28, 197, 390, 334, 613, 220, 818, 922, 573, 265, 784, 389, 172, 829, 601, 461, 160, 863, 239, 45, 11, 48, 302, 721, 455, 161, 463, 173, 835, 603, 627, 317, 311, 51, 149, 425, 356, 861, 676, 848, 734, 177, 638, 421, 315, 49, 584, 908, 507, 62, 318, 20, 700, 121, 764, 351, 695, 357, 518, 805, 626, 25, 796, 280, 337, 154, 686, 466, 561, 551, 41, 710, 310, 543, 725, 533, 720, 931, 109, 2, 866, 352, 362, 113, 821, 5, 249, 736, 391, 927, 703, 595, 95, 808, 240, 555, 746, 539, 889, 875, 873, 666, 495, 119, 33, 929, 120, 274, 204, 799, 606, 537, 135, 667, 504, 244, 355, 253, 783, 309, 486, 899, 991, 445, 519, 525, 797, 410, 785, 313, 444, 76, 506, 325, 891, 954, 905, 702, 342, 629, 921, 884, 535, 772, 314, 431, 992, 68, 828, 3, 224, 516, 738]
k = 20
print(sliding_window_brute(INT_ARRAY, k))


@decoratortimer(10)
def sliding_window(arr: list, k:int) -> int:
    '''
    Same function as above but instead of using a nested for loop,
    we will accomplish the same task using only a single for loop
    '''

    n = len(arr)

    if n < k:
        return -1

    current_sum = sum(arr[:k])
    max_sum = current_sum

    for i in range(0, n - k):
        current_sum = current_sum - arr[i] + arr[i + k]
        max_sum = max(current_sum, max_sum)

    return max_sum

INT_ARRAY = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
print(sliding_window(INT_ARRAY, k))

INT_ARRAY = [1, 4]
k = 4
print(sliding_window(INT_ARRAY, k))

INT_ARRAY = [237, 91, 273, 972, 454, 698, 74, 716, 609, 271, 619, 844, 141, 371, 668, 393, 604, 754, 423, 282, 812, 206, 190, 998, 838, 229, 527, 731, 182, 43, 867, 979, 759, 353, 825, 851, 416, 402, 205, 285, 392, 973, 599, 94, 623, 60, 290, 181, 429, 767, 153, 168, 332, 897, 947, 541, 688, 451, 920, 105, 36, 7, 19, 692, 378, 610, 71, 854, 328, 475, 529, 795, 942, 447, 202, 865, 167, 532, 96, 219, 729, 165, 579, 303, 514, 967, 570, 728, 718, 762, 902, 112, 715, 881, 34, 198, 608, 13, 293, 377, 615, 955, 631, 22, 963, 245, 893, 122, 411, 179, 980, 745, 405, 450, 526, 948, 327, 643, 898, 188, 997, 722, 295, 508, 260, 542, 974, 430, 903, 54, 651, 684, 42, 773, 949, 1, 593, 755, 439, 174, 874, 247, 569, 448, 222, 142, 252, 115, 93, 477, 277, 756, 517, 331, 968, 40, 789, 498, 705, 102, 366, 971, 73, 894, 341, 563, 374, 763, 560, 396, 35, 155, 534, 195, 630, 552, 503, 804, 732, 460, 359, 336, 44, 616, 484, 544, 647, 233, 386, 291, 145, 727, 17, 266, 820, 653, 509, 129, 632, 215, 689, 418, 900, 645, 823, 910, 80, 343, 408, 10, 877, 307, 184, 55, 301, 449, 375, 363, 564, 139, 983, 538, 474, 138, 387, 856, 485, 312, 969, 697, 611, 83, 907, 203, 730, 37, 497, 582, 412, 726, 279, 242, 137, 14, 250, 771, 670, 809, 384, 928, 709, 16, 136, 605, 457, 409, 150, 523, 131, 235, 270, 574, 488, 308, 99, 970, 344, 540, 781, 267, 811, 175, 63, 426, 210, 993, 832, 199, 806, 883, 21, 774, 965, 211, 57, 650, 577, 492, 67, 272, 50, 128, 975, 345, 213, 944, 321, 189, 358, 661, 699, 735, 589, 895, 323, 158, 424, 918, 956, 662, 201, 545, 381, 749, 79, 208, 435, 407, 480, 397, 521, 827, 470, 275, 833, 231, 996, 981, 276, 801, 510, 704, 263, 364, 862, 665, 180, 923, 38, 191, 880, 465, 712, 81, 365, 107, 660, 28, 197, 390, 334, 613, 220, 818, 922, 573, 265, 784, 389, 172, 829, 601, 461, 160, 863, 239, 45, 11, 48, 302, 721, 455, 161, 463, 173, 835, 603, 627, 317, 311, 51, 149, 425, 356, 861, 676, 848, 734, 177, 638, 421, 315, 49, 584, 908, 507, 62, 318, 20, 700, 121, 764, 351, 695, 357, 518, 805, 626, 25, 796, 280, 337, 154, 686, 466, 561, 551, 41, 710, 310, 543, 725, 533, 720, 931, 109, 2, 866, 352, 362, 113, 821, 5, 249, 736, 391, 927, 703, 595, 95, 808, 240, 555, 746, 539, 889, 875, 873, 666, 495, 119, 33, 929, 120, 274, 204, 799, 606, 537, 135, 667, 504, 244, 355, 253, 783, 309, 486, 899, 991, 445, 519, 525, 797, 410, 785, 313, 444, 76, 506, 325, 891, 954, 905, 702, 342, 629, 921, 884, 535, 772, 314, 431, 992, 68, 828, 3, 224, 516, 738]
k = 20
print(sliding_window(INT_ARRAY, k))
