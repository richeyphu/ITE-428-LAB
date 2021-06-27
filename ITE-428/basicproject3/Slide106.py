# Slide p.106
def mul_table(N, M):
    if N < M:
        for i in range(N, M + 1):
            for j in range(1, 13):
                print("\t{} x {}\t =\t{}".format(i, j, i * j))
            print("-" * 30)
    else:
        for i in reversed(range(M, N + 1)):
            for j in range(1, 13):
                print("\t{} x {}\t =\t{}".format(i, j, i * j))
            print("-" * 30)


n = float(input("Input Initial Number : ")).__floor__()
m = float(input("Input Final Number : ")).__float__()

print("=" * 30)

mul_table(n, m)
