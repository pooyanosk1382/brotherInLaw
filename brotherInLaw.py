import threading
import time

barrier = threading.Barrier(2)


def firstBrotherInLaw():
    print("First family start the trip")
    time.sleep(1)
    for _ in range(4):
        print("First family start going to next toll")
        for i in range(142):
            time.sleep(0.02)

        print("First family reached the toll " + str(_+1))
        barrier.wait()

        print("First family meet the second family")
    print("First family reach the destination")


def secondBrotherInLaw():
    print("second family start the trip")
    time.sleep(1)
    for _ in range(4):
        print("Second family start going to next toll")
        for i in range(142):
            time.sleep(0.04)

        print("Second family reached the toll " + str(_+1))
        barrier.wait()

        print("Second family meet the first family")
    print("Second family reach the destination")


firstGroom = threading.Thread(target=firstBrotherInLaw)
secondGroom = threading.Thread(target=secondBrotherInLaw)
firstGroom.start()
secondGroom.start()

firstGroom.join()
secondGroom.join()

print("All threads have completed.")
