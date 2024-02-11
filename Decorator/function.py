from custom_decorator import decorator


@decorator
def bank_account(name, balance, *args, **kwargs):
    return f"\nBank account holder : {name}\nAccount balance : {balance} $\n"


bank = bank_account("James Walter", 1500)

print(bank)