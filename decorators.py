
def decorator(func):
    def decorated(input_text):
        print('func start!!!')
        func(input_text)
        print('func end...')

    return decorated

@decorator
def new_create(input_text):
    print(input_text)


new_create('first create')

