'''
python utils/read_config.py
'''
import yaml

with open('config.yml', 'r') as file:
    #print(file.read())
    configuration = yaml.load(file, Loader=yaml.FullLoader)
    print(configuration)