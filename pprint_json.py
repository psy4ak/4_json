import json

def load_data(filepath):
    with open(filepath) as loads:
        my_data = json.load(loads)
        return my_data


def pretty_print_json(data):
    print (json.dumps(data,ensure_ascii=False, indent=4, sort_keys=True))


if __name__ == '__main__':

    path_file=input("File path (by default - Enter): ")
    
    if path_file == "":
        path_file= 'databars.json'
        
    my_data = load_data (path_file)
    pretty_print_json (my_data)
