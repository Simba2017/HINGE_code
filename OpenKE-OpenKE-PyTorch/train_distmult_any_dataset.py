import config
from  models import *
import json
import os
import argparse

parser = argparse.ArgumentParser(description="Data preprocessing path")
parser.add_argument('--indir', type=str, help='Input dir of train, test and valid data')
args = parser.parse_args()

os.environ['CUDA_VISIBLE_DEVICES']='1'
con = config.Config()
# con.set_in_path("./benchmarks/FB15K/")
# con.set_in_path("./benchmarks/wikipeople_testing_valid_25_pytorch_pg_triplets_keyValue_keyLiteral/")
con.set_in_path(args.indir)
# con.set_in_path("./benchmarks/JF17K_version1_test_25_percent_pg_triplets_keyValue_keyLiteral/")
con.set_work_threads(8)
con.set_train_times(1000)
con.set_nbatches(100)
con.set_alpha(0.1)
con.set_bern(0)
con.set_dimension(100)
con.set_margin(1.0)
con.set_ent_neg_rate(1)
con.set_rel_neg_rate(0)
con.set_opt_method("adagrad")
con.set_save_steps(10)
con.set_valid_steps(10)
con.set_early_stopping_patience(10)
con.set_checkpoint_dir("./checkpoint")
con.set_result_dir("./result")
con.set_test_link(True)
con.set_test_triple(False)
con.init()
con.set_train_model(DistMult)
con.train()
