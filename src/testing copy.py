import testing
import time 
import threading


def main():
    threading.Thread(target=testing.test_thread).start()
    while True:
        time.sleep(1.5)
        hhh = input("hello!")
        if hhh == str(1):
            print("done")
            testing.fucku = False
        elif hhh == str(2):
            testing.fucku = True

if __name__ == "__main__":
    main()

