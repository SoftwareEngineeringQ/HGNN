import scipy.io as scio
import numpy as np


def load_ft(data_dir, feature_name='GVCNN'):
    data = scio.loadmat(data_dir)  # [X, Y, indices, info, rates]
    lbls = data['Y'].astype(np.int64)
    if lbls.min() == 1:  # label从0开始
        lbls = lbls - 1
    idx = data['indices'].item()  # 数据索引

    if feature_name == 'MVCNN':
        fts = data['X'][0].item().astype(np.float32)  # 节点的特征
    elif feature_name == 'GVCNN':
        fts = data['X'][1].item().astype(np.float32)
    else:
        print(f'wrong feature name{feature_name}!')
        raise IOError

    idx_train = np.where(idx == 1)[0]  # 训练集索引
    idx_test = np.where(idx == 0)[0]
    return fts, lbls, idx_train, idx_test

