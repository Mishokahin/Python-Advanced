from collections import deque

bullet_price = int(input())
gun_barrel = int(input())
bullets = deque(int(bullet) for bullet in input().split())
locks = deque(int(lock) for lock in input().split())
reward = int(input())
mag = gun_barrel
shots_fired = 0

while True:
    if not bullets:
        if locks:
            print(f"Couldn't get through. Locks left: {len(locks)}")
            break
        else:
            print(f"0 bullets left. Earned ${reward - shots_fired*bullet_price}")
            break
    if not locks:
        print(f"{len(bullets)} bullets left. Earned ${reward - shots_fired * bullet_price}")
        break

    current_bullet = bullets.pop()
    current_lock = locks.popleft()

    if current_bullet <= current_lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(current_lock)

    mag -= 1
    shots_fired += 1

    if mag == 0:
        if bullets:
            print("Reloading!")
            mag = gun_barrel