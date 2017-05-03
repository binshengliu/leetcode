def is_digit(char):
    return char in '0123456789'


def is_sign(char):
    return char in '-+'


def is_dot(char):
    return char == '.'


def is_e(char):
    return char == 'e'


STATE0 = 0
STATE1 = 1
STATE2 = 2
STATE3 = 3
STATE4 = 4
STATE5 = 5
STATE6 = 6
STATE7 = 7
STATE8 = 8


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        rules = {
            STATE0: [(is_digit, STATE2),
                     (is_sign, STATE1),
                     (is_dot, STATE4)],
            STATE1: [(is_digit, STATE2),
                     (is_dot, STATE4)],
            STATE2: [(is_digit, STATE2),
                     (is_dot, STATE3),
                     (is_e, STATE6)],
            STATE3: [(is_digit, STATE5),
                     (is_e, STATE6)],
            STATE4: [(is_digit, STATE5)],
            STATE5: [(is_digit, STATE5),
                     (is_e, STATE6)],
            STATE6: [(is_digit, STATE8),
                     (is_sign, STATE7)],
            STATE7: [(is_digit, STATE8)],
            STATE8: [(is_digit, STATE8)],
        }

        end_state = [STATE2, STATE3, STATE5, STATE8]
        current = STATE0
        s = s.strip()
        for char in s:
            rule = rules[current]

            is_valid = False
            for (check, state) in rule:
                if check(char):
                    is_valid = True
                    current = state

            if not is_valid:
                return False

        return current in end_state
