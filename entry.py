'''
python entry.py
30-Nov-23
'''
import os
import yaml

# Read config
with open('/home/gom/Workspace/MLTemplate/config.yml', 'r') as file:
    configuration = yaml.load(file, Loader=yaml.FullLoader)
    
# file repo fullpath
fullpath = configuration['repository']['fullpath']
python_path = configuration['environment']['python_path']

# Run
cmd =  python_path + ' ' + os.path.join(fullpath,'augment.py')
os.system(cmd)

cmd = python_path + ' ' + os.path.join(fullpath,'train.py')
os.system(cmd)

cmd = python_path + ' ' + os.path.join(fullpath,'test.py')
os.system(cmd)