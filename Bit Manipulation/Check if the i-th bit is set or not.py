def isKthBitSet(n: int, k: int) -> bool:
    return (n&(1<<(k-1)))!=0
