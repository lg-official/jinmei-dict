#! /usr/bin/env bash

script_dir=$(dirname $(realpath "$0"))

cp $script_dir/sei.json $script_dir/../../mail_helper/settings/
cp $script_dir/mei.json $script_dir/../../mail_helper/settings/