__author__ = 'Ming'
"""
递归
1. 必须有一个明确的结束条件
2. 每次进入更深一层递归时，问题规模相比上一层递归应有所减少
3. 递归效率不高，递归层次过多回导致栈stack溢出
"""

def calc(n):
    print(n)
    if int(n/2) > 0:
        return calc( int(n/2) )
    print("最终结果->", n)

calc(10)