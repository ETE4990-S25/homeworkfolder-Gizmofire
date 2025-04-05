import threading
from datetime import datetime, timedelta
from fibCalc import fibTest
from factorial import factorial_test

multiThread = 3582017

def testFib(num):
    # Start task 1 (fibTest) and record its start time
   
    task1_start_time = datetime.now()
    print(f"Task 1 (fibTest) started at: {task1_start_time.strftime('%Y-%m-%d %H:%M:%S.%f')}")
    fibTest(num)  # Call the fibTest function with the multiThread argument

    task1_end_time = datetime.now()
    task1_duration = task1_end_time - task1_start_time
    print(f"Task 1 (fibTest) finished at: {task1_end_time.strftime('%Y-%m-%d %H:%M:%S.%f')}")
    print(f"Task 1 (fibTest) duration: {task1_duration}")


def testFact(num):
    # Start task 2 (factorial_test) and record its start time
    task2_start_time = datetime.now()
    print(f"Task 2 (factorial_test) started at: {task2_start_time.strftime('%Y-%m-%d %H:%M:%S.%f')}")
    factorial_test(num)  # Call the factorial_test function with the multiThread argument

    task2_end_time = datetime.now()
    task2_duration = task2_end_time - task2_start_time
    print(f"Task 2 (factorial_test) finished at: {task2_end_time.strftime('%Y-%m-%d %H:%M:%S.%f')}")
    print(f"Task 2 (factorial_test) duration: {task2_duration}")



def main():
    start_time = datetime.now()
    print(f"Main program started at: {start_time.strftime('%Y-%m-%d %H:%M:%S.%f')}")

    print("Starting processes...")
    thread1 = threading.Thread(target=testFib, args=(multiThread,))
    thread2 = threading.Thread(target=testFact, args=(multiThread,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("Processes finished.")

    

    end_time = datetime.now()
    main_duration = end_time - start_time
    print(f"Main program finished at: {end_time.strftime('%Y-%m-%d %H:%M:%S.%f')}")
    print(f"Total main program duration: {main_duration}")

if __name__ == "__main__":
    main()