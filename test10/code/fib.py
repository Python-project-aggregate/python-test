class Point:
    def __init__(self):
        print('init')
    def __enter__(self):
        print('enter')
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
p = Point()
with p as f:
    print('in with -------')
    print(p == f)
    print('with over')
