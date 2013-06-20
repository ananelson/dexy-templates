### @export "fib"
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

### @export "main-check"
if __name__ == 'main':
    print "fibonacci.py being called directly"
