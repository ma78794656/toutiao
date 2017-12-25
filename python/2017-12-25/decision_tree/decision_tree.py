# -*- coding:utf-8 -*-
import numpy as np
import operator
import matplotlib.pyplot as plt
import treePlotter


def calc_shannon_entropy(dataset):
    '''
    :param dataset: n行数组，最后一列为label
    :return: shannon_entropy
    '''
    label_count = {}
    for entry in dataset:
        label = entry[-1]
        label_count[label] = label_count.get(label, 0) + 1  # 计算所有label出现的次数
    entry_num = len(dataset)
    shannon_entropy = 0.0
    for key,val in label_count.items():
        prob = float(val) / entry_num  # 每一个label在dataset中出现的概率
        shannon_entropy -= prob * np.log2(prob)  # 每一个label在dataset中的熵
    return shannon_entropy


def split_dataset(dataset, axis, value):
    sub_dataset = []
    for entry in dataset:
        if entry[axis] == value:
            sub_entry = entry[:axis] + entry[axis + 1:]
            sub_dataset.append(sub_entry)
    return sub_dataset


def get_best_feature_index(dataset):
    dataset_len = len(dataset)
    feature_num = len(dataset[0]) - 1  # 组后一列为标签
    shannon_base = calc_shannon_entropy(dataset)
    shannon_list = []
    for idx in range(0, feature_num, 1):
        value_list = [entry[idx] for entry in dataset]
        unique_values = set(value_list)
        sub_shannon = 0.0
        for val in unique_values:
            sub_dataset = split_dataset(dataset, idx, val)
            prob = calc_shannon_entropy(sub_dataset)
            sub_shannon += prob * len(sub_dataset) / dataset_len
        shannon_list.append(sub_shannon)
    shannon_arr = np.array(shannon_list)
    #print('all features shannon values:')
    #print(shannon_arr)
    #print('gain shannon values:')
    #print(shannon_arr - shannon_base)
    #print('best feature is %d and shannon is %f and gain is %f' % (np.argsort(shannon_arr)[0], shannon_arr[np.argsort(shannon_arr)[0]], shannon_base - shannon_arr[np.argsort(-shannon_arr)[0]]))
    return np.argsort(shannon_arr)[0]


def create_dataset():
    dataset = [
        ['是', '是', '是', '是鱼类'],
        ['是', '是', '否', '是鱼类'],
        ['是', '否', '否', '非鱼类'],
        ['否', '是', '否', '非鱼类'],
        ['否', '否', '否', '非鱼类'],
        ['否', '是', '是', '是鱼类'],
    ]
    labels = ['不出水面能否生存', '是否有脚蹼', '是否有腮']
    return dataset,labels


def vote_labels(label_list):
    label_count = {}
    for label in label_list:
        label_count[label] = label_count.get(label, 0) + 1
    sorted_label_count = sorted(label_count.iteritems(), key = operator.getitem(1), reverse=True)
    return sorted_label_count[0][0]


def create_tree(dataset, features_name):
    label_list = [entry[-1] for entry in dataset]
    if label_list.count(label_list[0]) == len(label_list):  # 剩余的所有数据的label都相同
        return label_list[0]
    if len(dataset[0]) == 1:  # 剩余的所有的label不完全相同，并且所有特征都已用完，则投票选出剩余数据的标签
        return vote_labels(label_list)
    best_feature = get_best_feature_index(dataset)
    best_feature_name = features_name[best_feature]
    del(features_name[best_feature])
    tree = {best_feature_name:{}}
    feature_values = [entry[best_feature] for entry in dataset]
    feature_set = set(feature_values)
    for val in feature_set:
        tree[best_feature_name][val] = create_tree(split_dataset(dataset, best_feature, val), features_name)
    return tree


def classify(input_tree, feat_labels, test_vec):
    first_str = list(input_tree.keys())[0]
    second_dict = input_tree[first_str]
    feat_index = feat_labels.index(first_str)
    key = test_vec[feat_index]
    value_of_feat = second_dict[key]
    if isinstance(value_of_feat, dict):
        class_label = classify(value_of_feat, feat_labels, test_vec)
    else:
        class_label = value_of_feat
    return class_label


dataset, labels = create_dataset()
labels_bak = [l for l in labels]
mytree = create_tree(dataset, labels)
treePlotter.createPlot(mytree)
print('#'*15 + classify(mytree, labels_bak, ['是', '是', '否']) + '#'*15)
print('#'*15 + classify(mytree, labels_bak, ['否', '否', '否']) + '#'*15)
