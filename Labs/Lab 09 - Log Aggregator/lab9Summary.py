


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


def generate_summary(dictionary):
    summary = {}
    for log_level, details in dictionary.items():
        summary[log_level] = {
            'total_count': details['count'],
            'unique_messages': len(details) - 1,  # Exclude the 'count' key
            'messages': details
        }
    return summary



if __name__ == "__main__":
    # Print the dictionary in a formatted way
    print("Final dictionary:")
    for log_level, details in dictionary.items():
        print(f"{log_level}:")
        for key, value in details.items():
            print(f"  {key}: {value}")