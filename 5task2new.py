def dec(func):
  def wrapper(a,b):
    res = func(a,b)
    f = open('result','a')
    f.write('result'+" "+ str(res) + '\n')
    f.close()
    print('result',res)
    return func(a,b)
  return wrapper


