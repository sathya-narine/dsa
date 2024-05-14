def check_palindrome(x: int) -> bool:
    act_str = str(x)
    rev_str = act_str[::-1]
    if act_str == rev_str:
        return True
    return False
print(check_palindrome(10001))
