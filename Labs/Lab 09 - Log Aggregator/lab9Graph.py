import matplotlib.pyplot as plt
import numpy as np
import time

# sample dict
dictionary = {
                'INFO': {'count': 8, 
                        'Database corruption': 3, 
                        'Disk failure detected': 2, 
                        'System failure': 3}, 
                'WARNING': {'count': 5, 
                            'Disk failure detected': 1, 
                            'Database corruption': 3, 
                            'System failure': 1}, 
                'ERROR': {'count': 11, 
                            'Database corruption': 6, 
                            'System failure': 3, 
                            'Disk failure detected': 2}, 
                'CRITICAL': {'count': 9, 
                                'Disk failure detected': 2, 
                                'System failure': 4, 
                                'Database corruption': 3}
                } 


def draw_graph(dictionary):
    # Prepare data for the graph
    log_levels = list(dictionary.keys())
    messages = set()
    for details in dictionary.values():
        messages.update(details.keys())
    messages.discard('count')  # Remove the 'count' key

 
    message_counts = {message: [] for message in messages}

    for log_level in log_levels:
        for message in messages:
            count = dictionary[log_level].get(message, 0)
            message_counts[message].append(count)

    


    # had to use np to stack dataframes
    # https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_stacked.html
    # Plot the data
    x = range(len(log_levels))
    # plt.figure(figsize=(12, 6))
    # Stack the bars for each message
    bottom = np.zeros(len(log_levels))
    for message, counts in message_counts.items():
        print(f"Counts for {message}: {counts}")
        plt.bar(x, counts, bottom=bottom, label=message)
        bottom += np.array(counts)  # Update the bottom for stacking
    plt.xlabel('Log Levels')
    plt.ylabel('Counts')
    plt.title('Log Messages by Level')
    plt.xticks(x, log_levels)
    plt.legend(title="Messages", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

def dict_listener(dictionary):
    # This function is a placeholder for any additional processing you want to do with the dictionary
    # For now, it just prints the dictionary
    print("Updated dictionary:", dictionary)
    temp  = {"INFO": {}, "WARNING": {}, "ERROR": {}, "CRITICAL": {}}
    
    start_time = time.time()
    while time.time() - start_time < 10:
        
        if temp != dictionary:
            # If the dictionary has changed, update the graph
            draw_graph(dictionary)
            # Update the temp variable to the current state of the dictionary
            temp = dictionary.copy()
        time.sleep(0.001)
        




if __name__ == "__main__":
    # Print the dictionary in a formatted way
    draw_graph(dictionary)
    print("Final dictionary:", dictionary)
   
