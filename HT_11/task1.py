"""
Сайт для виконання завдання: https://jsonplaceholder.typicode.com
Написати програму, яка буде робити наступне:
1. Робить запрос на https://jsonplaceholder.typicode.com/users і вертає коротку інформацію про користувачів
(ID, ім'я, нікнейм)
2. Запропонувати обрати користувача (ввести ID)
3. Розробити наступну менюшку (із вкладеними пунктами):
   1. Повна інформація про користувача
   2. Пости:
      - перелік постів користувача (ID та заголовок)
      - інформація про конкретний пост (ID, заголовок, текст, кількість коментарів + перелік їхніх ID)
   3. ТУДУшка:
      - список невиконаних задач
      - список виконаних задач
   4. Вивести URL рандомної картинки
"""

import requests
from random import randrange


def menu(user):
    choice = input(f'Select the option you want:\n'
                   f'1 for full info about {user["username"]}\n'
                   f'2 for posts from {user["username"]}\n'
                   f'3 for todo`s from {user["username"]}\n'
                   f'4 for random photo\n'
                   f'5 for Exit\n')
    choices = {
        '1': full_info,
        '2': posts,
        '3': todo,
        '4': picture,
        '5': finish

    }
    choices[choice](user)


def start():
    user = users()
    menu(user)


def run_again(user):
    if input('Do you want to do something else?(yes/no)   ') == 'yes':
        start()
    else:
        finish(user)


def finish(user):
    print("GoodBye")
    exit()


def users():
    raw_users = requests.get('https://jsonplaceholder.typicode.com/users')
    raw_users = raw_users.json()
    print('Id'.ljust(2), 'Username'.ljust(15), 'Name',
          sep=' | ', end='\n------------------------------------------------\n')
    for user in raw_users:
        user_id = str(user['id'])
        name = user['name']
        username = user['username']

        print(user_id.ljust(2), username.ljust(15), name,
              sep=' | ', end='\n------------------------------------------------\n')
    choise = int(input('Select a user and enter his id '))
    if 1 <= choise <= 10:
        for user in raw_users:
            if user['id'] == choise:
                return user
    else:
        print('Wrong choice, please, select user from 1 to 10')
        run_again('1')


def full_info(user):
    print('Id:', user['id'], 'Userneme:', user['username'])
    print(user['name'], '\nContacts: Email: ', user['email'], 'Phone', user['phone'])
    print('Adress: ', end=', ')
    for element in user['address']:
        print(element, '-', user['address'][element], end=' ')
    print('Website: ', user['website'], 'Company:', end=' ')
    for element in user['company']:
        print(element, '-', user['company'][element], end=', ')
    print('\n')
    run_again(user)


def posts(user):
    raw_posts = requests.get('https://jsonplaceholder.typicode.com/posts', params={'userId': user['id']})
    raw_posts = raw_posts.json()
    id_s = []
    for post in raw_posts:
        id_s.append(post['id'])
        print('Id:', post['id'], '   Title:', post['title'])
    choice = int(input('Input post id here   '))
    if choice in id_s:
        for post in raw_posts:
            if post['id'] == choice:
                print(post['id'], ':', post['title'])
                print(post['body'])
                raw_comments = requests.get('https://jsonplaceholder.typicode.com/comments',
                                            params={'postId': post['id']}).json()
                print('Comments: ', len(raw_comments))
                for comment in raw_comments:
                    print(comment['id'])
    else:
        print('Incorrect post id')
    run_again(user)


def todo(user):
    raw_todos = requests.get('https://jsonplaceholder.typicode.com/todos', params={'userId': user['id']}).json()
    complited = [task for task in raw_todos if task['completed'] == True]
    failed = [task for task in raw_todos if task['completed'] == False]
    print('Completed: ')
    for task in complited:
        print('*  ', task['title'])
    print('Unfulfilled: ')
    for task in failed:
        print('*  ', task['title'])
    run_again(user)


def picture(user):
    photo = requests.get('https://jsonplaceholder.typicode.com/photos', params={'id': randrange(1, 5000)}).json()
    print('A random photo is better than nothing)', photo[0]['url'], sep='\n')
    run_again(user)


if __name__ == '__main__':
    start()
