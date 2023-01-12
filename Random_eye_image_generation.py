import random
import shutil

import numpy as np
import pandas as pd
import os


if __name__ == '__main__':
    numbers = 150
    base_folder = 'D:\\Gaze_Uncertainty_11_10\\Dropout_ith_uncertainty\\MPII\\Leave_one_out\\Fold_7_full\\vis'
    df = pd.read_csv(os.path.join(base_folder, 'result.csv'))
    people = int(df['Sample_names'][0].split('/')[1][1:])
    saving_folder = os.path.join('Data', '{:03d}'.format(people))
    if os.path.exists(saving_folder):
        shutil.rmtree(saving_folder)
    os.makedirs(saving_folder)
    os.makedirs(os.path.join(saving_folder, 'Left'))
    os.makedirs(os.path.join(saving_folder, 'Right'))
    samples = len(os.listdir(os.path.join(base_folder, 'Left')))
    sample_list = list(np.arange(start=0, stop=samples))
    random.seed(0)
    random_samples = random.sample(sample_list, numbers)

    for i in random_samples:
        left_src = os.path.join(base_folder, 'Left', '{}.png'.format(i))
        right_src = os.path.join(base_folder, 'Right', '{}.png'.format(i))
        left_dst = os.path.join(saving_folder, 'Left')
        right_dst = os.path.join(saving_folder, 'Right')
        shutil.copy(src=left_src, dst=left_dst)
        shutil.copy(src=right_src, dst=right_dst)

    print()


