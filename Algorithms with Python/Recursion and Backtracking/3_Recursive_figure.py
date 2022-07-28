def print_figure(n):
    if n == 0:
        return
    print('*' * n)#Pre-acton
    print_figure(n - 1)# когато стигне дъното , тоест n стане 0 , тогава ще слезе на ред 7 и след всяко изпълнение ще връща към предното
    # извикване , до първото
    print('#' * n)# Post-action

n = int(input())
print_figure(n)