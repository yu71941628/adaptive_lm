import os
import random


def gen_sub_single_file(in_file, out_file, ratio):
        f = open(in_file, 'r')
        lines = f.readlines()
        f.close()

        flag_array = gen_flag_array(len(lines),ratio)

        f = open(out_file, 'w')

        for i in range(0,len(flag_array)):
                if flag_array[i]==1:
                        f.write(lines[i])

        f.close()

def gen_flag_array(l, r):
        ret = [0]*l
        sel_cnt = int(l*r)

        start = random.randint(0,l-sel_cnt)

        for i in range(0,l):
                ret[i] = 0

        for i in range(start,start+sel_cnt):
                ret[i] = 1

        return ret


if __name__ == "__main__":

        ori_path = './ptb'

        for i in range(5,101,5):
                os.mkdir(ori_path + '_' + str(i) + '/preprocess')
                os.mkdir (ori_path + '_' + str(i) + '/output')

#                in_train_file = ori_path + '/train.txt'
#                out_train_file = ori_path + '_' + str(i) + '/train.txt'
#                gen_sub_single_file(in_train_file, out_train_file, float(i)/100.0)

#                in_train_file = ori_path + '/test.txt'
#                out_train_file = ori_path + '_' + str(i) + '/test.txt'
#                gen_sub_single_file(in_train_file, out_train_file, float(i)/100.0)

#                in_train_file = ori_path + '/valid.txt'
#                out_train_file = ori_path + '_' + str(i) + '/valid.txt'
#                gen_sub_single_file(in_train_file, out_train_file, float(i)/100.0)
