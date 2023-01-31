import random
import shutil

import numpy as np
import pandas as pd
import os


if __name__ == '__main__':
    numbers = 10
    base_folder = r'D:\Gaze_Uncertainty_11_10\With_uncertainty\MPII\Leave_one_out\Testing_results_ensemble\Fold_6\Base_1\vis_ensemble'
    df = pd.read_csv(os.path.join(base_folder, 'result.csv'))
    df = df.sort_values(by=['average_variance'], ascending=False)
    people = int(df['Sample_names'][0].split('/')[1][1:])
    saving_folder = os.path.join('Data', '{:03d}'.format(people))
    if os.path.exists(saving_folder):
        shutil.rmtree(saving_folder)
    os.makedirs(saving_folder)
    os.makedirs(os.path.join(saving_folder, 'Left'))
    os.makedirs(os.path.join(saving_folder, 'Right'))
    samples = len(os.listdir(os.path.join(base_folder, 'Left')))
    stop_1 = int(np.round(samples * 0.01))      # This is the bad stop
    stop_2 = int(np.round(samples * 0.1))       # This is the middle stop
    sample_list_1 = list(np.arange(start=0, stop=stop_1))
    sample_list_2 = list(np.arange(start=stop_1, stop=stop_2))
    sample_list_3 = list(np.arange(start=stop_2, stop=samples))
    random.seed(0)
    random_samples_1 = random.sample(sample_list_1, numbers)
    random_samples_2 = random.sample(sample_list_2, numbers)
    random_samples_3 = random.sample(sample_list_3, numbers)
    random_samples = [random_samples_1, random_samples_2, random_samples_3]

    for j in random_samples:
        for i in j:
            left_src = os.path.join(base_folder, 'Left', '{}.png'.format(i))
            right_src = os.path.join(base_folder, 'Right', '{}.png'.format(i))
            left_dst = os.path.join(saving_folder, 'Left', '{:03d}_{}.png'.format(people, i))
            right_dst = os.path.join(saving_folder, 'Right', '{:03d}_{}.png'.format(people, i))
            shutil.copy(src=left_src, dst=left_dst)
            shutil.copy(src=right_src, dst=right_dst)

    print()


