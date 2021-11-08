import json
import logging
import os
import pickle


def write_pickle(file_path, filename, json_data):
    try:
        file = open(os.path.join(file_path, filename), "wb")
    except OSError as e:
        print("Error opening the file. Please ensure the file exists and has appropriate permissions.")
        logging.error(e)
    else:
        # pickle.dump()
        # pickle.dump()
        pickle.dump(json_data, file)
    finally:
        file.close() if file else logging.warning("No file resource available to close.")


def read_all_json_files(path_to_json_files):
    json_objects = []
    file_list = os.listdir(path_to_json_files)
    for file in file_list:
        if file.upper().endswith(".JSON"):
            json_object = json_helper(os.path.join(path_to_json_files, file))
            json_objects.append(json_object)
            # print(json_objects)
            # print(os.path.join(path_to_json_files, file))
    return json_objects


def json_helper(file_path):
    """
    opens a file, reads the json string and returns the json object
    :param file_path: path to file
    :return: json object
    """
    json_object = None
    file = None
    try:
        file = open(file_path)
    except OSError as e:
        print("Error opening the file. Please ensure the file exists and has appropriate permissions.")
        logging.error(e)
    else:
        json_object = json_read(file)
    finally:
        file.close() if file else logging.warning("No file resource available to close.")
        # print("asdasdasdasd")
        return json_object


def json_read(file):
    json_object = json.load(file)
    return json_object


def load_pickle(file_with_path):
    pickle_contents = None
    file = None
    try:
        file = open(file_with_path, "rb")
    except OSError as e:
        print("Error opening the file. Please ensure the file exists and has appropriate permissions.")
        logging.error(e)
    else:
        # print(file)
        # print(pickle.load(file))
        pickle_contents = pickle.load(file)
    finally:
        file.close() if file else logging.warning("No file resource available to close.")
        return pickle_contents


if __name__ == '__main__':
    object_list = read_all_json_files("./data/marvel")
    # print(object_list)
    write_pickle("./data/marvel", "marvel.pickle", object_list)
    print(load_pickle("./data/marvel/marvel.pickle"))
