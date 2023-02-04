#! _*_ coding:utf-8 _*_
# __author__ = "Ming"

from conf import settings
from core import accounts
from core import logger
# transaction logger

def make_transaction(log_obj, account_data, tran_type, amount, **others):
    """
    deal all the user transactions
    :param account_data: user account data
    :param tran_type: transaction type
    :param amount: transaction amount
    :param others: mainly for logging usage
    :return:
    """
    amount = float(amount)
    if tran_type in settings.TRANSACTION_TYPE:
        
        interest = amount * settings.TRANSACTION_TYPE[tran_type]['interest']
        old_balance = account_data['balance']
        if settings.TRANSACTION_TYPE[tran_type]['action'] == 'plus':
            new_balance = old_balance + amount + interest
        elif settings.TRANSACTION_TYPE[tran_type]['action'] == 'minus':
            new_balance = old_balance - amount - interest
            # check credit
            if new_balance < 0:
                print(f"""\033[31;1mYour credit {account_data['credit']} is not enough for this transaction -({amount}+{interest}),\
                    your current balance is {old_balance}]""")
                return
        account_data['balance'] = new_balance
        accounts.dump_account(account_data) # save the new balance back to file
        log_obj.info(f"account:{account_data['id']}    action:{tran_type}   amount:{amount}   interest:{interest}")
        return account_data
    else:
        print(f"\033[31;1mTransaction type {tran_type} is not exist!\033[0m")