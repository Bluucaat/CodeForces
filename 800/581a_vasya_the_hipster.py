a, b = map(int, input().split())
different_color_pairs = min(a,b)
same_color_pairs = (max(a,b)-different_color_pairs) // 2
print(different_color_pairs, same_color_pairs)