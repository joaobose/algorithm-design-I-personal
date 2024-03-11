def LCP(w, SA):
    PHI = [0] * len(SA)
    PLCP = [0] * len(SA)
    LCP = [0] * len(SA)

    PHI[SA[0]] = -1

    for i in range(1, len(SA)):
        PHI[SA[i]] = SA[i - 1]

    L = 0
    for i in range(len(SA)):
        if PHI[i] == -1:
            PLCP[i] = 0
            continue

        while (i + L) < len(w) and (PHI[i] + L) < len(w) and w[i + L] == w[PHI[i] + L]:
            L += 1

        PLCP[i] = L
        L = max(L - 1, 0)

    for i in range(len(SA)):
        LCP[i] = PLCP[SA[i]]

    return LCP, PLCP


w = '1710490'
SA = [7, 6, 3, 2, 0, 4, 1, 5]


# w = 'kamehamehe'
# SA = [10, 5, 1, 9, 7, 3, 8, 4, 0, 6, 2]

w_lcp, w_plcp = LCP(w, SA)
print(f'w: {w}')
print(f'SA: {SA}')
print(f'PLCP: {w_plcp}')
print(f'LCP: {w_lcp}')
