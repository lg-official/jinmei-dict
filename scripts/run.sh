#! /usr/bin/env bash
set -e

script_dir=$(dirname $(realpath "$0"))

python $script_dir/generate_user_dict.py 
python $script_dir/jinmei-dict.py $script_dir/../data/mecab-naist-jdic-0.6.3b-20111013/naist-jdic.csv $script_dir/../data/mecab-ipadic-neologd/mecab-user-dict-seed.20200130/mecab-user-dict-seed.20200130.csv $script_dir/../data/addon/addon.csv $script_dir/../data/addon/user_dict.csv $script_dir/../data/addon/user_dict_generated.csv $script_dir/../data/addon/tss_sei.csv $script_dir/../data/addon/tss_mei.csv

$script_dir/copy.sh