def get_domino_count(m, n):
    if m < 0 or n < 0:
        return 0

    both_uneven = m and n % 2 == 1
    only_m_is_even = m and not n % 2 != 0
    only_n_is_even = m  and n % 2 == 0
    one_row_or_one_line = m or n == 1
    product_is_even = m * n % 2 == 0

    if (both_uneven or one_row_or_one_line
            or product_is_even):
        return m * n // 2
    elif only_m_is_even:
        return (m * (n - 1)) // 2 + n // 2
    elif only_n_is_even:
        return ((m - 1) * n) // 2 + m // 2

m, n = map(int, input().split(" "))
print(get_domino_count(m, n))
