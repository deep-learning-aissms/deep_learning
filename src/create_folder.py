import os
import shutil
import argparse
import yaml
import pandas as pd
import numpy as np
from get_data import get_data,read_params


##########CREATING FOLDER ##############

def create_folder(config,image=None):
    config = get_data(config)
    dir = config['load_data']['preprocessed_data']
    cla = config['load_data']['num_classes']
    if os.path.exists(dir+'/'+'train'+'/'+'class_0') and os.path.exists(dir+'/'+'test'+'/'+'class_0'):
        print("The train and test folder already exists.....")
        print("I am skipping it!")

    else:
        os.mkdir(dir+'/'+'train')
        os.mkdir(dir+'/'+'test')
        for i in range(cla):
            os.mkdir(dir+'/'+'train'+'/'+'class_'+str(i))
            os.mkdir(dir+'/'+'test'+'/'+'class_'+str(i))
        print("Folder created successfully!")


if __name__=='__main__':
   args = argparse.ArgumentParser()
   args.add_argument('--config',default='params.yml')
   passed_args = args.parse_args()
   a = create_folder(config=passed_args.config)