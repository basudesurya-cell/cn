# Sliding Window with Go-Back-N

n = int(input("Enter number of frames: "))
w = int(input("Enter window size: "))

i = 1

while i <= n:
    end = min(i + w, n + 1)

    for j in range(i, end):
        print("Frame", j, "sent")

    lost = int(input("Enter lost frame (0 for none): "))

    if i <= lost < end:
        print("Frame", lost, "lost!")
        print("Go-Back-N: Resending frames")

        for j in range(lost, end):
            print("Frame", j, "sent again")

    print("Acknowledgement received\n")
    i += w

print("All frames sent successfully")
