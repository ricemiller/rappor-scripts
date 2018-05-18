#!/bin/bash

if [[ $# -ne 3 ]]; then
    echo "Usage: $0 path_to_params.csv path_to_dataset.csv path_to_uniques.txt"
    exit 1
fi

FILESOK=true

if [[ ! -f $1 ]]; then
    echo "File $1 does not exist"
    FILESOK=false
fi

if [[ ! -f $2 ]]; then
    echo "File $2 does not exist"
    FILESOK=false
fi

if [[ ! -f $3 ]]; then
    echo "File $3 does not exist"
    FILESOK=false
fi

if [[ $FILESOK = false ]]; then
    exit 1
fi


readonly THIS_DIR=$(dirname $0)
readonly TMPDIR=tmpdir
export PYTHONPATH=$THIS_DIR/client/python
readonly PARAMS=$1
readonly DATASET=$2
readonly UNIQUES=$3


echo '[*] Extracting values from params.csv'
k=$(awk 'BEGIN{FS=","}{print $1;}' $PARAMS | tail -1)
h=$(awk 'BEGIN{FS=","}{print $2;}' $PARAMS | tail -1)
m=$(awk 'BEGIN{FS=","}{print $3;}' $PARAMS | tail -1)
p=$(awk 'BEGIN{FS=","}{print $4;}' $PARAMS | tail -1)
q=$(awk 'BEGIN{FS=","}{print $5;}' $PARAMS | tail -1)
f=$(awk 'BEGIN{FS=","}{print $6;}' $PARAMS | tail -1)
echo "k = $k"
echo "h = $h"
echo "m = $m"
echo "p = $p"
echo "q = $q"
echo "f = $f"


echo '[*] Deleting tmpdir'
rm -rf $TMPDIR


echo '[*] Creating tmpdir'
mkdir $TMPDIR


echo '[*] Creating map.csv'
bin/hash_candidates.py \
    $PARAMS \
    < $UNIQUES \
    > $TMPDIR/map.csv


echo '[*] Creating true_values.csv'
bin/true_values_generator.py \
    $m \
    $DATASET \
    > $TMPDIR/true_values.csv

echo '[*] Creating reports.csv'
time tests/rappor_sim.py \
    --num-bits $k \
    --num-hashes $h \
    --num-cohorts $m \
    -p $p \
    -q $q \
    -f $f \
    < $TMPDIR/true_values.csv \
    > $TMPDIR/reports.csv


echo '[*] Creating counts.csv'
bin/sum_bits.py \
    $PARAMS \
    < $TMPDIR/reports.csv \
    > $TMPDIR/counts.csv
