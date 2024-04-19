def setBits(N : int) -> int:
    if N&(N+1):
        return N|(N+1)
    return N    
