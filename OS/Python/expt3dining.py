import threading
import time

room = threading.Semaphore(4)
chopstick = [threading.Semaphore(1) for i in range(5)]

def philosopher(num):
    phil = num
    room.acquire()
    print(f"Philosopher {phil} has entered the room")
    chopstick[phil].acquire()
    chopstick[(phil + 1) % 5].acquire()
    eat(phil)
    time.sleep(1)
    print(f"Philosopher {phil} has finished eating")
    chopstick[(phil + 1) % 5].release()
    chopstick[phil].release()
    room.release()

def eat(phil):
    print(f"Philosopher {phil} is eating")

if __name__ == '__main__':
    threads = []
    for i in range(5):
        threads.append(threading.Thread(target=philosopher, args=(i,)))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
