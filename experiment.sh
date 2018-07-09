#!/bin/bash
# Script used to generate the initial scaffolding and necessary files to run the various experiments

if [[ $# -ne 6 ]]; then
    echo "Usage: $0 params_01.csv params_1.csv params_10.csv dataset_10k.csv dataset_100k.csv dataset_1m.csv"
    exit 1
fi

#For directory creation, the files must have the above naming convention

readonly THIS_DIR=$(dirname $0)
readonly EXPERIMENT_DIR=$THIS_DIR/experiment
readonly PARAMS=($1 $2 $3)
readonly DATASETS=($4 $5 $6)
readonly TMPDIR=tmpdir

echo '[*] Deleting $EXPERIMENT_DIR'
rm -rf $EXPERIMENT_DIR

echo '[*] Creating $EXPERIMENT_DIR'
mkdir $EXPERIMENT_DIR

for PARAM in ${PARAMS[@]}; do
    for DATASET in ${DATASETS[@]}; do
        DIRPARAM=$(echo $PARAM | cut -d '_' -f 2 | cut -d '.' -f 1)
        DIRDATASET=$(echo $DATASET | cut -d '_' -f 2 | cut -d '.' -f 1)
        DIR=$EXPERIMENT_DIR/$DIRPARAM/$DIRDATASET
        $THIS_DIR/pipeline.sh $PARAM $DATASET uniques.txt
        mkdir -p $DIR
        mv $TMPDIR/counts.csv $TMPDIR/map.csv $DIR/
    done
done

exit 0
