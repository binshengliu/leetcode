from solution import Solution

def test_add_1():
    s = Solution()
    ans = s._add('1', '2')
    assert ans == '3'

def test_add_2():
    s = Solution()
    # import pudb.b
    ans = s._add('999', '999')
    assert ans == '1998'

def test_add_3():
    s = Solution()
    ans = s._add('1981', '19')
    assert ans == '2000'

def test_add_4():
    s = Solution()
    ans = s._add('999999999999999999', '888888888888888888')
    assert ans == '1888888888888888887'

def test_add_empty():
    s = Solution()
    ans = s._add('', '888888888888888888')
    assert ans == '888888888888888888'

    ans = s._add('888888888888888888', '')
    assert ans == '888888888888888888'

def test_multiply_1():
    s = Solution()
    ans = s.multiply('3', '3')
    assert ans == '9'

def test_multiply_2():
    s = Solution()
    ans = s.multiply('9', '8')
    assert ans == '72'

def test_multiply_3():
    s = Solution()
    ans = s.multiply('900000000000000', '0')
    assert ans == '0'

def test_multiply_4():
    s = Solution()
    ans = s.multiply('34', '2')
    assert ans == '68'

def test_multiply_5():
    s = Solution()
    # import pudb.b
    ans = s.multiply('123', '456')
    assert ans == '56088'

def test_multiply_6():
    s = Solution()
    # import pudb.b
    ans = s.multiply('2', '987654321')
    assert ans == '1975308642'

    ans = s.multiply('123456789', '987654321')
    assert ans == '121932631112635269'
