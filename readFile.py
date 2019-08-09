from json.decoder import JSONDecodeError
import json



def readFile():
    with open('E:\py\DLP_MUTI_REPLICA\config.json') as config_file:
        try:
            config_data = json.load(config_file)
            # print(config_data)
        except JSONDecodeError:
            print("[ERROR] Invalid json format in config file!")
            exit(1)

    return config_data