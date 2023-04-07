import re
from itertools import permutations
import math
import functools
from sympy.ntheory import factorint
import inflect
import urllib.request
from functools import reduce
from itertools import combinations_with_replacement
import numpy as np
from fractions import Fraction


# Problem 1
# sum_of_multiples = 0
# for number in range(1000):
#     if number % 3 == 0:
#         sum_of_multiples += number
#     elif number % 5 == 0:
#         sum_of_multiples += number
# print(sum_of_multiples)

# Problem 2
# sum_of_even_fib = 0
# val1 = 0
# val2 = 1
# while val2 < 4000000:
#     if val2 % 2 == 0:
#         sum_of_even_fib += val2
#     temp = val2
#     val2 = val2 + val1
#     val1 = temp
# print(sum_of_even_fib)

# Problem 3
# number = 600851475143
# root = int(math.sqrt(number)) + 1
# for divider in range(2, root):
#     while number % divider == 0:
#         number = number // divider
#     if number == 1:
#         print(divider)
#         break

# Problem 4
# max_product = 0
# for num1 in range(1000):
#     for num2 in range(num1 + 1):
#         product = num1 * num2
#         if str(product) == str(product)[::-1]:
#             max_product = max(max_product, product)
# print(max_product)

# Problem 5
# num = 2520
# jump = 2520
# count = 10
# while count != 20:
#     for divider in range(2, count + 1):
#         if num % divider != 0:
#             # num += max(10, divider-1)
#             num += jump
#             break
#     else:
#         print(num)
#         jump = num
#         count += 1

# Problem 6
# sum1 = sum(range(101))**2
# sum2 = sum([number **2 for number in range(101)])
# print(f"{sum1} - {sum2} = {sum1-sum2}")

# Problem 7
# prime_counter = 0
# number = 2
# while prime_counter < 10001:
#     for divider in range(2, int(math.sqrt(number)) + 1):
#         if number % divider == 0:
#             break
#     else:
#         prime_counter += 1
#     number += 1
# print(number - 1)

# Problem 8
# number = """
# 73167176531330624919225119674426574742355349194934
# 96983520312774506326239578318016984801869478851843
# 85861560789112949495459501737958331952853208805511
# 12540698747158523863050715693290963295227443043557
# 66896648950445244523161731856403098711121722383113
# 62229893423380308135336276614282806444486645238749
# 30358907296290491560440772390713810515859307960866
# 70172427121883998797908792274921901699720888093776
# 65727333001053367881220235421809751254540594752243
# 52584907711670556013604839586446706324415722155397
# 53697817977846174064955149290862569321978468622482
# 83972241375657056057490261407972968652414535100474
# 82166370484403199890008895243450658541227588666881
# 16427171479924442928230863465674813919123162824586
# 17866458359124566529476545682848912883142607690042
# 24219022671055626321111109370544217506941658960408
# 07198403850962455444362981230987879927244284909188
# 84580156166097919133875499200524063689912560717606
# 05886116467109405077541002256983155200055935729725
# 71636269561882670428252483600823257530420752963450""".replace('\n','')
# max_product = 0
# for i in range(len(number)-12):
#     max_product = max(max_product, functools.reduce(lambda a,b: int(a)*int(b),number[i:i+13]))
# print(max_product)

# Problem 9
# for a in range(500):
#     for b in range(a):
#         if a + b + (math.sqrt(a**2 + b**2)) == 1000:
#             print(int(a * b * (math.sqrt(a**2 + b**2))))

# Problem 10
# sum_primes = 0
# for number in range(2, 2000000):
#     for divider in range(2, int(math.sqrt(number)) + 1):
#         if number % divider == 0:
#             break
#     else:
#         sum_primes += number
# print(sum_primes)

# Problem 11
# grid = """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
# 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
# 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
# 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
# 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
# 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
# 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
# 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
# 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
# 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
# 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
# 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
# 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
# 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
# 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
# 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
# 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
# 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
# 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
# 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48""".split("\n")
# grid = [row.split(' ') for row in grid]
# grid = [[int(x) for x in row] for row in grid]
# rows = len(grid)
# columns = len(grid[0])
# max_product = 0
# for row in range(rows):
#     for column in range(columns):
#         down = 0
#         if row <= 16:
#             down = grid[row][column] * grid[row+1][column] * grid[row+2][column] * grid[row+3][column]
#         right = 0
#         if column <= 16:
#             right = grid[row][column] * grid[row][column+1] * grid[row][column+2] * grid[row][column+3]
#         right_down = 0
#         if row <= 16 and column <= 16:
#             right_down = grid[row][column] * grid[row+1][column+1] * grid[row+2][column+2] * grid[row+3][column+3]
#         right_up = 0
#         if row >= 3 and column <= 16:
#             right_up = grid[row][column] * grid[row-1][column+1] * grid[row-2][column+2] * grid[row-3][column+3]
#         max_product = max(max_product, right, down, right_up, right_down)
# print(max_product)

# Problem 12
# number = 2
# triangle = 1
# triangle_counter = 1
# max_div_counter = 0
# while True:
#     triangle += number
#     triangle_counter += 1
#     number += 1
#     divider_count = 1
#     # this is the slow part
#     # for divider in range(1, triangle+1):
#     #     if triangle % divider == 0:
#     #         divider_count += 1
#     # using this import instead:
#     prime_factors = factorint(triangle)
#     for item in prime_factors.items():
#         divider_count *= (item[1] + 1)
#     if divider_count > max_div_counter:
#         print(f"{triangle_counter} triangle number is {triangle} and it has {divider_count} divisors")
#         max_div_counter = divider_count
#     if divider_count > 500:
#         break

# Problem 13
# num = """37107287533902102798797998220837590246510135740250
# 46376937677490009712648124896970078050417018260538
# 74324986199524741059474233309513058123726617309629
# 91942213363574161572522430563301811072406154908250
# 23067588207539346171171980310421047513778063246676
# 89261670696623633820136378418383684178734361726757
# 28112879812849979408065481931592621691275889832738
# 44274228917432520321923589422876796487670272189318
# 47451445736001306439091167216856844588711603153276
# 70386486105843025439939619828917593665686757934951
# 62176457141856560629502157223196586755079324193331
# 64906352462741904929101432445813822663347944758178
# 92575867718337217661963751590579239728245598838407
# 58203565325359399008402633568948830189458628227828
# 80181199384826282014278194139940567587151170094390
# 35398664372827112653829987240784473053190104293586
# 86515506006295864861532075273371959191420517255829
# 71693888707715466499115593487603532921714970056938
# 54370070576826684624621495650076471787294438377604
# 53282654108756828443191190634694037855217779295145
# 36123272525000296071075082563815656710885258350721
# 45876576172410976447339110607218265236877223636045
# 17423706905851860660448207621209813287860733969412
# 81142660418086830619328460811191061556940512689692
# 51934325451728388641918047049293215058642563049483
# 62467221648435076201727918039944693004732956340691
# 15732444386908125794514089057706229429197107928209
# 55037687525678773091862540744969844508330393682126
# 18336384825330154686196124348767681297534375946515
# 80386287592878490201521685554828717201219257766954
# 78182833757993103614740356856449095527097864797581
# 16726320100436897842553539920931837441497806860984
# 48403098129077791799088218795327364475675590848030
# 87086987551392711854517078544161852424320693150332
# 59959406895756536782107074926966537676326235447210
# 69793950679652694742597709739166693763042633987085
# 41052684708299085211399427365734116182760315001271
# 65378607361501080857009149939512557028198746004375
# 35829035317434717326932123578154982629742552737307
# 94953759765105305946966067683156574377167401875275
# 88902802571733229619176668713819931811048770190271
# 25267680276078003013678680992525463401061632866526
# 36270218540497705585629946580636237993140746255962
# 24074486908231174977792365466257246923322810917141
# 91430288197103288597806669760892938638285025333403
# 34413065578016127815921815005561868836468420090470
# 23053081172816430487623791969842487255036638784583
# 11487696932154902810424020138335124462181441773470
# 63783299490636259666498587618221225225512486764533
# 67720186971698544312419572409913959008952310058822
# 95548255300263520781532296796249481641953868218774
# 76085327132285723110424803456124867697064507995236
# 37774242535411291684276865538926205024910326572967
# 23701913275725675285653248258265463092207058596522
# 29798860272258331913126375147341994889534765745501
# 18495701454879288984856827726077713721403798879715
# 38298203783031473527721580348144513491373226651381
# 34829543829199918180278916522431027392251122869539
# 40957953066405232632538044100059654939159879593635
# 29746152185502371307642255121183693803580388584903
# 41698116222072977186158236678424689157993532961922
# 62467957194401269043877107275048102390895523597457
# 23189706772547915061505504953922979530901129967519
# 86188088225875314529584099251203829009407770775672
# 11306739708304724483816533873502340845647058077308
# 82959174767140363198008187129011875491310547126581
# 97623331044818386269515456334926366572897563400500
# 42846280183517070527831839425882145521227251250327
# 55121603546981200581762165212827652751691296897789
# 32238195734329339946437501907836945765883352399886
# 75506164965184775180738168837861091527357929701337
# 62177842752192623401942399639168044983993173312731
# 32924185707147349566916674687634660915035914677504
# 99518671430235219628894890102423325116913619626622
# 73267460800591547471830798392868535206946944540724
# 76841822524674417161514036427982273348055556214818
# 97142617910342598647204516893989422179826088076852
# 87783646182799346313767754307809363333018982642090
# 10848802521674670883215120185883543223812876952786
# 71329612474782464538636993009049310363619763878039
# 62184073572399794223406235393808339651327408011116
# 66627891981488087797941876876144230030984490851411
# 60661826293682836764744779239180335110989069790714
# 85786944089552990653640447425576083659976645795096
# 66024396409905389607120198219976047599490197230297
# 64913982680032973156037120041377903785566085089252
# 16730939319872750275468906903707539413042652315011
# 94809377245048795150954100921645863754710598436791
# 78639167021187492431995700641917969777599028300699
# 15368713711936614952811305876380278410754449733078
# 40789923115535562561142322423255033685442488917353
# 44889911501440648020369068063960672322193204149535
# 41503128880339536053299340368006977710650566631954
# 81234880673210146739058568557934581403627822703280
# 82616570773948327592232845941706525094512325230608
# 22918802058777319719839450180888072429661980811197
# 77158542502016545090413245809786882778948721859617
# 72107838435069186155435662884062257473692284509516
# 20849603980134001723930671666823555245252804609722
# 53503534226472524250874054075591789781264330331690"""
# numbers = num.split('\n')
# numbers = [int(number) for number in numbers]
# print(str(sum(numbers))[:10])

# Problem 14
# max_sequence = 0
# max_sequence_number = 0
# for num in range(2, 1000000):
#     number = num
#     print(number)
#     sequence = 0
#     while number != 1:
#         sequence += 1
#         if number % 2 == 0:
#             number //= 2
#         else:
#             number = 3*number + 1
#     if sequence > max_sequence:
#         max_sequence = sequence
#         max_sequence_number = num
# print(f"max sequence is: {max_sequence}, starting from number: {max_sequence_number}")

# Problem 15
# Combinatorics
# 40 choose 20 = 137846528820

# Problem 16
# print(sum(map(int, str(2**1000))))

# Problem 17
# p = inflect.engine()
# print(sum(map(len, [p.number_to_words(number).replace("-", "").replace(" ", "") for number in range(1, 1001)])))

# Problem 18
# Dynamic Programming
# memo = [[-1 for i in range(row + 1)] for row in range(15)]
# memo[14] = [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
# print(f"memoization before function call:\n{memo}")
#
# table = """75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""".split("\n")
# table = [row.split(" ") for row in table]
# table = [[int(number) for number in row] for row in table]
# print(f"the pyramid:\n{table}")
#
#
# def recursive_solve(row, column):
#     if memo[row][column] != -1:
#         return memo[row][column]
#     else:
#         memo[row][column] = table[row][column] + max(recursive_solve(row + 1, column), recursive_solve(row + 1, column + 1))
#         return memo[row][column]
#
#
# print(f"solve: {recursive_solve(0, 0)}")
# print(f"memoization after function call:\n{memo}")

# Problem 19
# not_leap_year = [31,28,31,30,31,30,31,31,30,31,30,31]
# leap_year = [31,29,31,30,31,30,31,31,30,31,30,31]
# day = 0
# sun_day_first_of_month = 0
# for year in range(1901, 2001):
#     if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#         for month_days in leap_year:
#             if day == 0:
#                 sun_day_first_of_month += 1
#             day = (day + month_days) % 7
#     else:
#         for month_days in not_leap_year:
#             if day == 0:
#                 sun_day_first_of_month += 1
#             day = (day + month_days) % 7
# print(sun_day_first_of_month)

# Problem 20
#
#
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
#
#
# print(sum(map( int , str(fact(100)))))

# Problem 21
# def count_divisors(number):
#     sum_of_div = 1
#     for divisor in range(2, int(math.sqrt(number)) + 1):
#         if number % divisor == 0:
#             sum_of_div += divisor + (number // divisor)
#     return sum_of_div
#
# amicable = []
# for number in range(10000):
#     divisors = count_divisors(number)
#     if number == count_divisors(divisors) and number != divisors:
#         if number not in amicable:
#             amicable.append(number)
#         if divisors not in amicable:
#             amicable.append(divisors)
#
# print(sum(amicable))

# Problem 22
# data = urllib.request.urlopen("https://projecteuler.net/project/resources/p022_names.txt")
# names = ""
# for line in data:
#     names += line.decode('utf-8')
# names = list(map(lambda x: x.replace("\"", ""), names.split(',')))
# names.sort()
# name_val_func = lambda acc, char: ord(char.lower()) - ord('a') + 1 + acc
# names_values = [reduce(name_val_func, name, 0) * (index + 1) for index, name in enumerate(names)]
# print(sum(names_values))

# Problem 23
# numbers = [x for x in range(1, 28123)]
# sum_of_num_divisors = [sum([div if num % div == 0 else 0 for div in range(1, num)]) for num in numbers]
# abundant = [numbers[index] for index in range(len(numbers)) if sum_of_num_divisors[index] > numbers[index]]
# all_numbers_comb = [sum(comb) for comb in combinations_with_replacement(abundant, 2)]
# # not_summable = [num for num in numbers if num not in all_numbers_comb]
# numbers = np.array(numbers)
# all_numbers_comb = np.array(all_numbers_comb)
# not_summable = np.setdiff1d(numbers, all_numbers_comb)
# print(np.sum(not_summable))

# Problem 24
# per = list(permutations(range(10)))
# mili_per = sorted(per)[1000000-1]
# sol = ''.join(list(map(lambda char: str(char), mili_per)))
# print(sol)

# Problem 25
# boundary = 10**(999)
# fib1 = 0
# fib2 = 1
# counter = 1
# while fib2 < boundary:
#     fib2, fib1 = fib2 + fib1, fib2
#     counter += 1
# print(counter)

# Problem 26
# def divide(a, b):
#     '''Returns the decimal representation of the fraction a / b in three parts:
#     integer part, non-recurring fractional part, and recurring part.'''
#     assert b > 0
#     integer = a // b
#     remainder = a % b
#     seen = {remainder: 0}  # Holds position where each remainder was first seen.
#     digits = []
#     while True:  # Loop executed at most b times (as remainders must be distinct)
#         remainder *= 10
#         digits.append(remainder // b)
#         remainder = remainder % b
#         if remainder in seen:  # Digits have begun to recur.
#             where = seen[remainder]
#             # print(f"{a}/{b} => rec: {len(digits[where:])}")
#             return integer, digits[:where], digits[where:]
#         else:
#             seen[remainder] = len(digits)
#
#
# def func(cur_max, number):
#     res = divide(1, number)
#     if len(res[2]) > cur_max[0]:
#         return len(res[2]), number
#     else:
#         return cur_max
#
#
# max_length = reduce(func, range(1, 1000), (0, 0))
# print(max_length[1])

# Problem 27 - Dumb way (long)
# def print_matrix(matrix):
#     for row in matrix:
#         for slot in row:
#             print(slot, end="\t")
#         print()
#     print()
#
#
# size = 1001
# matrix = [[0 for column in range(size)] for rows in range(size)]
# # matrix = np.matrix(matrix)
# # print_matrix(matrix)
# row = size // 2
# column = size // 2
# pattern = [[1, 0], [0, -1], [-2, 0], [0, 2], [2, 0]]
# current_path = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
# index = 0
# for slot in range(1, size ** 2 + 1):
#     matrix[row][column] = slot
#     while pattern[index] == current_path[index]:
#         index += 1
#         if index == len(pattern):
#             current_path = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
#             pattern = [pattern[0], [0, pattern[1][1] - 2], [pattern[2][0] - 2, 0], [0, pattern[3][1] + 2], [pattern[4][0] + 2, 0]]
#             index = 0
#     if pattern[index][0] == 0:
#         # need to move on Y-axis
#         if pattern[index][1] - current_path[index][1] > 0:
#             current_path[index][1] += 1
#             row -= 1
#         else:
#             current_path[index][1] -= 1
#             row += 1
#     else:
#         # need to move on X-axis
#         if pattern[index][0] - current_path[index][0] > 0:
#             current_path[index][0] += 1
#             column += 1
#         else:
#             current_path[index][0] -= 1
#             column -= 1
# # print_matrix(matrix)
#
#
# def calc_diagonals(matrix):
#     sum_of_diagonal = 0
#     for index in range(len(matrix)):
#         sum_of_diagonal += matrix[index][index]
#         sum_of_diagonal += matrix[index][len(matrix) - 1 - index]
#     # 1 is on both diagonals, counted twice
#     return sum_of_diagonal - 1
#
#
# print(calc_diagonals(matrix))

# Problem 28 - Recursion
# def calc_diagonals(size):
#     if size == 1:
#         return 1
#     else:
#         return calc_corners(size) + calc_diagonals(size - 2)
#
#
# def calc_corners(size):
#     up_right = size ** 2
#     up_left = up_right - size + 1
#     down_left = up_left - size + 1
#     down_right = down_left - size + 1
#     return up_left + up_right + down_right + down_left
#
#
# print(calc_diagonals(1001))

# Problem 29
# distinct_numbers = set()
# for a in range(2, 101):
#     for b in range(2, 101):
#         distinct_numbers.add(a ** b)
# print(len(distinct_numbers))

# Problem 30
# special_nums = []
# for number in range(2, 1000000):
#     num_str = str(number)
#     num_sum = reduce(lambda acc, cur: acc + (int(cur) ** 5), num_str, 0)
#     special_nums.append(number) if num_sum == number else None
# print(sum(special_nums))

# Problem 31
# def coins_sum(left, index, change):
#     if left < 0 or index < 0:
#         return 0
#     elif left == 0:
#         return 1
#     else:
#         return coins_sum(left, index - 1, change) + coins_sum(left - change[index], index, change)
#
# print(coins_sum(200, 7, [1, 2, 5, 10, 20, 50, 100, 200]))
# write a memo for this one, good practice!

# Problem From Geeks for Geeks
# https://www.geeksforgeeks.org/puzzle-6x6-grid-how-many-ways/
# 10 choose 5 - combinatorics
# def path(x, y):
#     if x == 0 and y == 0:
#         return 1
#     elif x < 0 or y < 0:
#         return 0
#     else:
#         return path(x - 1, y) + path(x, y - 1)
#
#
# def path_dp():
#     memo = [[-1 for i in range(6)] for j in range(6)]
#     for i in range(6):
#         memo[0][i] = 1
#         memo[i][0] = 1
#     for row in range(1, 6):
#         for column in range(1, 6):
#             memo[row][column] = memo[row - 1][column] + memo[row][column - 1]
#     return memo[5][5]
#
# print(path(5, 5))
# print(path_dp())

# Problem 32
# product_set = set()
# for first in range(10000):
#     for second in range(first):
#         product = first * second
#         all_digits = str(product)+str(first)+str(second)
#         if len(all_digits) == 9:
#             list_of_digits = re.findall(r"\d", all_digits)
#             if set(list_of_digits) == set(["1","2","3","4","5","6","7","8","9"]):
#                 product_set.add(product)
# print(sum(product_set))

# Problem 33
# fracs = []
# for denominator in range(10, 100):
#     for numerator in range(10, denominator):
#         if not(denominator % 10 == 0 or numerator % 10 == 0):
#             list_frac = [(numerator // 10) / (denominator // 10), (numerator // 10) / (denominator % 10),
#                     (numerator % 10) / (denominator // 10), (numerator % 10) / (denominator % 10)]
#             list_same_digit = [(numerator % 10) == (denominator % 10), (numerator % 10) == (denominator // 10),
#                     (numerator // 10) == (denominator % 10), (numerator // 10) == (denominator // 10)]
#             for i in range(4):
#                 if list_frac[i] == numerator / denominator and list_same_digit[i]:
#                     fracs.append(Fraction(numerator, denominator))
# print(reduce(lambda x,y: x*y, fracs).denominator)


# Problem 34
# sum_of_nums = 0
# for number in range(10, 100000):
#     digits = [int(x) for x in str(number)]
#     sum_fac = reduce(lambda acc, curr: acc + math.factorial(curr), digits, 0)
#     if sum_fac == number:
#         sum_of_nums += number
# print(sum_of_nums)

# Problem 35
# def is_prime(number):
#     d = 2
#     while d * d <= number:
#         if number % d == 0:
#             return False
#         d += 1
#     return True
#
# def conv_tuple_to_int(tup):
#     num = 0
#     mul = 1
#     for digit in reversed(tup):
#         num = num + digit * mul
#         mul *= 10
#     return num
#
#
# count = 0
# l = []
# prime_hash = {}
# for number in range(2, 1000000):
#     number = str(number)
#     comb = [int(number[i:]+number[:i]) for i in range(len(number))]
#     for num in comb:
#         # num = conv_tuple_to_int(tup)
#         if num not in prime_hash:
#             prime_hash[num] = is_prime(num)
#         if not prime_hash[num]:
#             break
#     else:
#         count += 1
# print(count)

# Problem 36
# def to_binary(number):
#     binary = ""
#     while number != 0:
#         binary = str(number % 2) + binary
#         number //= 2
#     return binary
#
#
# def check_pol(number: str):
#     length = len(number)
#     for i in range(length // 2 + 1):
#         if number[i] != number[length - 1 - i]:
#             return False
#     return True
#
# # print(to_binary(11))
# # print(check_pol("10121201"))
#
# l = []
# for number in range(1, 1000000):
#     num_str = str(number)
#     if check_pol(num_str):
#         num_bin = to_binary(number)
#         if check_pol(num_bin):
#             l.append(number)
# print(sum(l))

# Problem 37
# def is_prime(number):
#     if number < 2:
#         return False
#     d = 2
#     while d * d <= number:
#         if number % d == 0:
#             return False
#         d += 1
#     return True
#
#
# l = []
# for number in range(10, 1000000):
#     num_str = str(number)
#     for i in range(len(num_str)):
#         if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:i+1])):
#             break
#     else:
#         l.append(number)
# print(sum(l))

# Problem 38
# max_pan_num = 0
# for number in range(10000):
#     pan = str(number)
#     flag = False
#     for i in range(2, 10):
#         if len(pan) + len(str(number * i)) > 9:
#             break
#         pan += str(number*i)
#         flag = True
#     for i in range(1, 10):
#         if str(i) not in pan:
#             flag = False
#             break
#     if int(pan) > max_pan_num and flag:
#         max_pan_num = int(pan)
# print(max_pan_num)


# Problem 39
# d = {}
# for a in range(500):
#     for b in range(a + 1):
#         p = a + b + math.sqrt(a ** 2 + b ** 2)
#         if p == int(p):
#             p = int(p)
#             d[p] = d.get(p, 0) + 1
# print(max(d, key=d.get))

# Problem 40
# def d(n):
#     counter = 0
#     number = 1
#     frac = ""
#     while counter <= n:
#         num_str = str(number)
#         frac += num_str
#         counter += len(num_str)
#         number += 1
#     return int(frac[n-1])
#
# print(d(1)*d(10)*d(100)*d(1000)*d(10000)*d(100000)*d(1000000))

# Problem 41
# def is_prime(number):
#     d = 2
#     while d * d <= number:
#         if number % d == 0:
#             return False
#         d += 1
#     return True
#
# def is_pandigital(number):
#     num_str = str(number)
#     for i in range(1, 8):
#         if str(i) not in num_str:
#             return False
#     return True
#
#
# number = 7654321
# while not is_pandigital(number) or not is_prime(number):
#     number -= 1
# print(number)


# Problem 42
# t_nums = set()
# for n in range(1000):
#     t_nums.add(0.5 * n * (n+1))
# file = urllib.request.urlopen("https://projecteuler.net/project/resources/p042_words.txt")
# words = []
# for line in file:
#     words.append(line.decode('UTF-8'))
# words = words[0].split(",")
# count = 0
# for word in words:
#     word = word[1:len(word) - 1]
#     val = reduce(lambda acc, curr: acc + ord(curr) - ord('A') + 1, word, 0)
#     if val in t_nums:
#         count += 1
# print(count)
