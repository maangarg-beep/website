def compute_area(x1, y1, x2, y2):
    return (x2 - x1) * (y2 - y1)

def overlap_area(r1, r2):
    x_overlap = max(0, min(r1[2], r2[2]) - max(r1[0], r2[0]))
    y_overlap = max(0, min(r1[3], r2[3]) - max(r1[1], r2[1]))
    return x_overlap * y_overlap

r1 = list(map(int, input().split()))
r2 = list(map(int, input().split()))

area1 = compute_area(*r1)
area2 = compute_area(*r2)
overlap = overlap_area(r1, r2)

print(area1 + area2 - overlap)