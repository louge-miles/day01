from typing import Iterable


def sum_even(lst: Iterable[int]) -> int:
    """返回可迭代整数序列中所有偶数的和。忽略非整数值。

    示例:
        sum_even([1, 2, 3, 4]) -> 6
    """
    return sum(x for x in lst if isinstance(x, int) and x % 2 == 0)


if __name__ == "__main__":
    # 示例：期望输出 12
    print(sum_even([1, 2, 3, 4, 5, 6]))
