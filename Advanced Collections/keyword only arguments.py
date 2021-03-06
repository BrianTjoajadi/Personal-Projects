def critical_func(arg1, suppressExceptions = False):
    pass

def critical_func_2(arg1, *, suppressExceptions = False):
    pass

def main():
    critical_func(1, suppressExceptions=True)
    # critical_func_2(2, True)
    critical_func_2(2, suppressExceptions=True)

if __name__ == "__main__":
    main()