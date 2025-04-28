import lab9_generator
import lab9_parser
import lab9Graph
import threading
import sys
import json

# all the threads are to be ran from here

dictionary = {"INFO": {}, "WARNING": {}, "ERROR": {}, "CRITICAL": {}}

def main():
    t1 = threading.Thread(target=lab9_generator.logGenerator)
    t2 = threading.Thread(target=lab9_parser.logParser, args=("logGLfolder\\log.log",dictionary))
    t3 = threading.Thread(target=lab9Graph.dict_listener, args=(dictionary))
    
    t2.start()
    t3.start()
    t1.start()
    

    # timout added since program was being hung 
    t2.join(timeout=4)
    t3.join(timeout=10)
    t1.join()


    print("Done!")
    print("Final dictionary:", dictionary)

    with open("logGLfolder\\log_summary.json", "w") as json_file:
        json.dump(dictionary, json_file, indent=4)

    # this does not work at all, cry face
    lab9_parser.exitTimer()

   
    

if __name__ == "__main__":
    main()