#! /usr/bin/env bash
set -e

python generate_user_dict.py 
python jinmei-dict.py '../data/mecab-naist-jdic-0.6.3b-20111013/naist-jdic.csv' '../data/mecab-ipadic-neologd/mecab-user-dict-seed.20200130/mecab-user-dict-seed.20200130.csv' '../data/addon/addon.csv' '../data/addon/user_dict.csv' '../data/addon/user_dict_generated.csv' '../data/addon/tss_sei.csv' '../data/addon/tss_mei.csv'