import math


def main():
    # the quadratic 0.001x^2 + 1000x + 0.001 = 0
    a = 0.001
    b = 1000
    c = 0.001
    real_roots = (-1e-6, -1e6)
    solutions_1 = get_solutions_by_method_1(a, b, c)
    print(solutions_1)
    print(
        f'error : {real_roots[0]-solutions_1[0]},{real_roots[1]-solutions_1[1]}')
    solutions_2 = get_solutions_by_method_2(a, b, c)
    print(solutions_2)
    print(
        f'error : {real_roots[0]-solutions_2[0]},{real_roots[1]-solutions_2[1]}')
    solutions_3 = get_solution_by_hybrid_method(a, b, c)
    print(solutions_3)
    print(
        f'error : {real_roots[0]-solutions_3[0]},{real_roots[1]-solutions_3[1]}')


def get_solutions_by_method_1(a, b, c):
    if a != 0:
        root_1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
        root_2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)

    else:
        root_1 = -c/b
        root_2 = root_1
    return (root_1, root_2)


def get_solutions_by_method_2(a, b, c):
    root_1 = 2*c/(-b-math.sqrt(b**2-4*a*c))
    root_2 = 2*c/(-b+math.sqrt(b**2-4*a*c))
    return(root_1, root_2)


def get_solution_by_hybrid_method(a, b, c):
    if b >= 0:
        root_1 = 2*c/(-b-math.sqrt(b**2-4*a*c))
        if a != 0:
            root_2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
        else:
            root_2 = root_1
    else:
        root_2 = 2*c/(-b+math.sqrt(b**2-4*a*c))
        if a != 0:
            root_1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
        else:
            root_1 = root_2
    return(root_1, root_2)


if __name__ == "__main__":
    main()
