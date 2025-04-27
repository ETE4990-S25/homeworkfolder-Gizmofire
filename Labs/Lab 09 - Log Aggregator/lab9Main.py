import lab9_generator
import lab9_parser
import threading
import sys



dictionary = {"INFO": 0, "WARNING": 0, "ERROR": 0, "CRITICAL": 0}

def main():
    t1 = threading.Thread(target=lab9_generator.logGenerator)
    t2 = threading.Thread(target=lab9_parser.logParser, args=("logGLfolder\\log.log",dictionary))
    
    
    t2.start()
    t1.start()

    # timout added since program was being hung 
    t2.join(timeout=10)
    
   
    t1.join()

    

    print("Done!")
    print("Final dictionary:", dictionary)
    print("Exiting in 10 seconds...")

    lab9_parser.exitTimer()

   
    

if __name__ == "__main__":
    main()