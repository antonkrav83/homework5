def dec(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper

@dec
def func1():
    print('hello world')

func1()
func1()
func1()
func1()
func1()
print(func1.count)