# generate a number sequence folloing a certain pattern

class Solution:

    def generate_sequence(self, n: int):

        # 0 generate a sequence of "1,2,3,2,_2,3,4,3,_3,4,5,4,..."
        # basic version 
        res_0 = []
        for i in range(n):
            res_0.append(i)
        print("sequence 0:")
        print(res_0)
        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

        # 0a, generate number with patterns
        res_0a = []
        for i in range(1, n, 1):
            res_0a.extend((range(i, i+3)))    # +1, +1, +1 , [1, 2, 3
            res_0a.append(i+1)              # +1 , [2
        print("sequence 0a:")
        print(res_0a)
        # [1, 2, 3, _, 2, __, 2, 3, 4, _, 3, __, 3, 4, 5, 4, 4, 5, 6, 5, 5, 6, 7, 6...

        # 0b, same pattern as 0a, use itertools 
        def pattern():
            i = 1 
            while True:
                yield i
                yield i + 1 
                yield i + 2
                yield i + 1     # 1 2 3 2
                i += 2          # next start point
        import itertools 
        print("sequence 0b:")
        print(*itertools.islice(pattern(), 20))
        # 1 2 3 2   3 4 5 4   5 6 7 6   7 8 9 8   9 10 11 10 ...

        # 1
        # generate a sequence of "1,2,3,2,_2,3,4,3,_3,4,5,4,..."
        # remove "_" to not print it
        print("sequence 1:")
        print(
            ",_".join("{},{},{},{}".format(i, i+1, i+2, i+1) for i in range (1, n, 1))
        )
        # 1,2,3,2,_2,3,4,3,_3,4,5,4,_4,5,6,5,_5,6,7,6, ...

        # 1a generate numbers 
        print("sequence 1a:")
        print(
            ','.join(str(i) for i in range(n) if i % 4 in (1,2))
        )
        # 1,2,5,6,9,10,13,14,17,18

        # 1b
        print("sequence 1b:")
        print(
            ','.join(map(str, sorted(list(range(1, n, 4))) + list(range(2, n, 4))))
        )
        # 1,5,9,13,17,2,6,10,14,18

        # 1c 
        res_1c = [1]
        while res_1c[-1] < n:
            res_1c.append(res_1c[-1] + 1)
            res_1c.append(res_1c[-1] + 3)
        print("sequence 1c:")    
        print(','.join(map(str, res_1c)))
        # 1,2,5,6,9,10,13,14,17,18,21

        # 1d 
        res_1d = []
        for num in range(1,n):
            if num % 4 == 1 or num % 4 == 2:
                res_1d.append(num)
                continue
            pass 
        print("sequence 1d:") 
        print(res_1d)
        # [1, 2, 5, 6, 9, 10, 13, 14, 17, 18]

        # 1e
        print("sequence 1e:") 
        print(','.join(str(i) for i in range(n) if i % 4 in (1, 2)))
        # 1,2,5,6,9,10,13,14,17,18

        # 2, print a sequence who numbers has remainder of 1 or 4 when divided by 4
        print("sequence 2:", [i for i in range(1, n) if (i % 4 ==1 or i % 4 == 2 )])
        # [1, 2, 5, 6, 9, 10, 13, 14, 17, 18]

        # print even numbers only 
        print("even numbers: ", [i for i in range(1,n) if (i%2 !=1) ], sep=',')
        # [2, 4, 6, 8, 10, 12, 14, 16, 18]

        # while loop
        result = [] 
        x = 1
        diff = 1
        while x < n:
            result.append(x)
            x += diff 
            # alternate step of value 1 and 3 
            diff = 3 if diff ==1 else 1
        print("skip 2 numbers", (result))
        # [1, 2, 5, 6, 9, 10, 13, 14, 17, 18]

        # reverse numbers 
        def reverse(n):
            for i in range(n, -1, -1): 
                yield i
        res = []   # store in list to print in 1 line
        for i in reverse(n):
            res.append(i)
        print(res)
        # [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        

        # 


test = Solution()
test.generate_sequence(20)        