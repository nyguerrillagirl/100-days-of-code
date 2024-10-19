def convert_usd_to_aud(amount, rate=0.75):
    return amount / rate

def convert_and_sum_list(usd_list, rate=0.75):
    total = 0
    for amount in usd_list:
        total += convert_usd_to_aud(amount, rate=rate)

    return total

def convert_and_sum_list_kwargs(usd_list, **kwargs):
    total = 0
    for amount in usd_list:
        total += convert_usd_to_aud(amount, **kwargs)

    return total

def my_test_function(usd_list, a='A', b='B', c='C'):
    my_str = ''
    for w in usd_list:
        my_str += ":" + w + a + b + c

    return my_str

def check_my_test_function(usd_list, **kwargs):
    return my_test_function(usd_list, **kwargs)

print(check_my_test_function(['one', 'two', 'three'], a='X', b='Y'))