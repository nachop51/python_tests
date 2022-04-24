def bouncing_ball(h, bounce, window):
    # your code
    count = -1
    if 0 < bounce < 1:
        while h > window > 0:
            h *= bounce
            count += 2
    return count

print(bouncing_ball(2, 0.5, 1))
print(bouncing_ball(2, 1, 1))
print(bouncing_ball(3, 0.66, 1.5))
print(bouncing_ball(30, 0.66, 1.5))
print(bouncing_ball(30, 0.75, 1.5))