import json

def preservColumn(cityToKeep):
    # Open the input json file
    with open('prix.json', 'r') as input_file:
        data = json.load(input_file)

    # Filter objets with "ville" equals to cityToKeep
    new_data = [item for item in data if item.get('ville') == cityToKeep]

    # Write the filtered data in the output 
    with open('output.json', 'w') as output_file:
        json.dump(new_data, output_file, indent=4)

    print("Filtering done. Data from", cityToKeep ,"are now in  'output.json'.")

preservColumn("Paris")
