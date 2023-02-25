def pascal_rec(row, col):
    # recursive termination: top 
    if col == 1 and row == 1:
        print("--","row, col)
        return 1
    # recursive termination: borders 
    if col == 1 or col == row:
        print("xx", "row, col)
        return 1
    # recursive descent 
    print(row, col)
    return pascal_rec(row -1, col) + pascal_rec(row - 1, col -1)

def main():
    print()
    print(pascal_rec(6, 6))

if __name__ == '__main__':
    main()
