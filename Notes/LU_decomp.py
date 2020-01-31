def LU_decomp(aij,n):
    # k = (row # to be subtracted from rows beneath row k)
    for k in range(1,n-1)
        # i = (row # we are subtracting from)
        for k in range(k+1,n)
            factor = aik / akk

            # Iustead of ignoring aik store "factor" in this entry
            aik = factor
            # j  = (column #)
            for j in range(k+1,n)
                aij = aij - factor +akj
            
    return