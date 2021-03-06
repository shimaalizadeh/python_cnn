import numpy as np
import h5py
import math

def generate(DATA_FILENAME) :

    IMG_HEIGHT = 48
    IMG_WIDTH = 48

    x_training = np.empty([28709, 48, 48])
    x_test = np.empty([3589, 48 ,48])
    x_validation = np.empty([3589, 48 ,48])
    
    y_trainig = np.empty(28709)
    y_test = np.empty(3589)
    y_validation = np.empty(3589)

    train_idx = 0
    test_idx = 0
    val_idx = 0

    with open(DATA_FILENAME, 'r') as f:
        next(f) # ignore header
        for line in f:
            kaggle_label, data_str, category = line.split(',')[:3]
            print kaggle_label, kaggle_label.dtype
            data = data_str.split(' ')
            img = np.empty(shape=(IMG_HEIGHT, IMG_WIDTH), dtype = np.uint8)
            for idx, val in enumerate(data):
                img[math.floor(idx/IMG_WIDTH), idx % IMG_WIDTH] = float(val)

            category = category.strip() # to remove the potential spaces

            if category == "Training":
                print train_idx
                x_training[train_idx, :, :] = img
                y_trainig[train_idx] = kaggle_label.astype(np.int64)
                print type(y_trainig[train_idx])
                train_idx += 1
            elif category == "PublicTest":
                print val_idx
                x_validation[val_idx, :, :] = img
                y_validation[val_idx] = kaggle_label.astype(np.int64)
                val_idx += 1
            elif category == "PrivateTest":
                print test_idx
                x_test[test_idx, :, :] = img
                y_test[test_idx] = kaggle_label.astype(np.int64)
                
                test_idx += 1


    h5f_file= h5py.File('dataset/data.h5', 'w')
    h5f_file.create_dataset('X_train', data = x_training)
    h5f_file.create_dataset('X_val', data = x_validation)
    h5f_file.create_dataset('X_test', data = x_test)
    h5f_file.create_dataset('y_train', data = y_trainig)
    h5f_file.create_dataset('y_val', data = y_validation)
    h5f_file.create_dataset('y_test', data = y_test)
    h5f_file.close()

            
