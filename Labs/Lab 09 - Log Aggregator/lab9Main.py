import lab9_generator
import lab9_parser
import threading


def main():
    t1 = threading.Thread(target=lab9_generator.logGenerator)
    t2 = threading.Thread(target=lab9_parser.logParser, args=("logGLfolder\\log.log",))
    t2.start()
    t1.start()

    t1.join()
    t2.join()

    print("Done!")
    

if __name__ == "__main__":
    main()