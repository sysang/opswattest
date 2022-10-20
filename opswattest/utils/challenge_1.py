import math
import random
import string


def find_different_character(s1, s2):
    prob1 = [ord(character) for character in s1]
    prob2 = [ord(character) for character in s2]
    # print('prob1: ', prob1)
    # print('prob2: ', prob2)

    routes = []
    is_forward = True

    while True:
        prob1_cache = prob1
        prob2_cache = prob2
        distance = len(prob1)
        step_point = math.ceil(distance / 2)

        prob1 = prob1[0:step_point]
        prob2 = prob2[0:step_point]

        new_step = step_point if is_forward else step_point - distance
        routes.append(new_step)

        # print('routes: ', routes, sum(routes))
        # print('distance: ', distance, ' - step_point: ', step_point, ' - prob1: ', prob1, ' - prob1_cache: ', prob1_cache)

        if len(prob1) == 1 and sum(prob1) != sum(prob2):
            return prob1[0], prob2[0], sum(routes) - 1

        if sum(prob1) == sum(prob2):
            prob1 = prob1_cache[step_point:]
            prob2 = prob2_cache[step_point:]
            is_forward = True
        else:
            is_forward = False


# s1 = 'qwer1234'
# s2 = 'qwer1235'

# diff1, diff2, pos = find_different_character(s1, s2)
# print(diff1, diff2, pos)
# assert '4' == s1[pos]
# assert '5' == s2[pos]

# s1 = 'qwer1234'
# s2 = 'qwer1224'

# diff1, diff2, pos = find_different_character(s1, s2)
# print(diff1, diff2, pos)
# assert '3' == s1[pos]
# assert '2' == s2[pos]

# s1 = 'Qwer1234'
# s2 = 'qwer1234'

# diff1, diff2, pos = find_different_character(s1, s2)
# print(diff1, diff2, pos)
# assert 'Q' == s1[pos]
# assert 'q' == s2[pos]

# s1 = 'Qwer1234'
# s2 = 'qwer1234'

# diff1, diff2, pos = find_different_character(s1, s2)
# print(diff1, diff2, pos)
# assert 'Q' == s1[pos]
# assert 'q' == s2[pos]

# s1 = 'qWer1234'
# s2 = 'qwer1234'

# diff1, diff2, pos = find_different_character(s1, s2)
# print(diff1, diff2, pos)
# assert 'W' == s1[pos]
# assert 'w' == s2[pos]

# s1 = 'qweR1234'
# s2 = 'qwer1234'

# diff1, diff2, pos = find_different_character(s1, s2)
# print(diff1, diff2, pos)
# assert 'R' == s1[pos]
# assert 'r' == s2[pos]

# s1 = 'qwer1234'
# s2 = 'qwer0234'

# diff1, diff2, pos = find_different_character(s1, s2)
# print(diff1, diff2, pos)
# assert '1' == s1[pos]
# assert '0' == s2[pos]

# s1 = 'qwer12345'
# s2 = 'qwer12346'

# diff1, diff2, pos = find_different_character(s1, s2)
# print(diff1, diff2, pos)
# assert '5' == s1[pos]
# assert '6' == s2[pos]

# s1 = 'Qwer12345'
# s2 = 'qwer12345'

# diff1, diff2, pos = find_different_character(s1, s2)
# print(diff1, diff2, pos)
# assert 'Q' == s1[pos]
# assert 'q' == s2[pos]

# s1 = 'qwer12345'
# s2 = 'qwer22345'

# diff1, diff2, pos = find_different_character(s1, s2)
# print(diff1, diff2, pos)
# assert '1' == s1[pos]
# assert '2' == s2[pos]

N = 10
var_char = 'a'
index = random.choice(range(N))
s1 = ''.join(random.choices(string.ascii_letters + string.digits, k=N))
s2 = s1[:index] + var_char + s1[index+1:]

print(s1, s2)
diff1, diff2, pos = find_different_character(s1, s2)
print(diff1, diff2, s2[pos])
