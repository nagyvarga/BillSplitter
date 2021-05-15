import random
friends = {}


def get_integer():
    """"""
    try:
        value = int(input())
    except (ValueError, TypeError):
        print('Please, enter a number.')
        return None
    else:
        return value


def get_lucky_friend(friends_name):
    """"""
    return random.choice(friends_name)


print('\nEnter the number of friends joining (including you):')
number_of_people = get_integer()
if number_of_people is not None and number_of_people > 0:
    print('\nEnter the name of every friend (including you), each on a new line:')
    for _ in range(number_of_people):
        name_of_friend = input()
        friends[name_of_friend] = 0
    print('\nEnter the total bill value:')
    bill = get_integer()
    try:
        bill_per_person = round(bill / number_of_people, 2)
    except TypeError:
        pass
    else:
        friends = {name: bill_per_person for name in friends.keys()}
    # print(f'\n{friends}')
    print('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky_feature_choice = input()
    if lucky_feature_choice == 'Yes':
        lucky_friend = get_lucky_friend(list(friends.keys()))
        print(f'\n{lucky_friend} is the lucky one!')
        try:
            updated_bill_per_person = round(bill / (number_of_people - 1), 2)
        except ZeroDivisionError:
            pass
        else:
            updated_friends = {name: updated_bill_per_person for name in friends.keys()}
            friends.update(updated_friends)
            friends[lucky_friend] = 0
    elif lucky_feature_choice == 'No':
        print('\nNo one is going to be lucky')
    print(f'\n{friends}')
else:
    print('\nNo one is joining for the party')
