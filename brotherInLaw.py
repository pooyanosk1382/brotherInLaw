import threading
import time

# Define a barrier with 2 threads
barrier = threading.Barrier(2)


def firstBrotherInLaw():
    for _ in range(4):
        # Thread 1 waits for 2 seconds
        print("First family start going to next toll")
        time.sleep(2)

        # Thread 1 reaches the barrier
        print("First family reached the toll " + str(_+1))
        barrier.wait()

        # Thread 1 continues execution
        print("They meet the second family")


def secondBrotherInLaw():
    for _ in range(4):
        # Thread 2 waits for 4 seconds
        print("Second family start going to next toll")
        time.sleep(4)

        # Thread 2 reaches the barrier
        print("Second family reached the toll " + str(_+1))
        barrier.wait()

        # Thread 2 continues execution
        print("They meet the first family")


# Create and start the threads
firstGroom = threading.Thread(target=firstBrotherInLaw)
secondGroom = threading.Thread(target=secondBrotherInLaw)
firstGroom.start()
secondGroom.start()

# Wait for the threads to finish
firstGroom.join()
secondGroom.join()

print("All threads have completed.")
