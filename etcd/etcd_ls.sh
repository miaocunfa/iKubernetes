#!/bin/bash
PREFIX=${1:-/}
ORIG_PREFIX=${PREFIX}

LAST_CHAR=${PREFIX:${#PREFIX}-1:1}
if [[ $LAST_CHAR != '/' ]];
then
    # Append  '/' at the end if not exist
    PREFIX="$PREFIX/"
fi

for ITEM in $(etcdctl get "$PREFIX" --prefix=true --keys-only | grep "$PREFIX");
do
    PREFIX_LEN=${#PREFIX}
    CONTENT=${ITEM:$PREFIX_LEN}
    POS=$(expr index "$CONTENT" '/')

    if [[ $POS -le 0 ]];
    then
        # No '/', it's not dir, get whole str
        POS=${#CONTENT}
    fi

    CONTENT=${CONTENT:0:$POS}
    LAST_CHAR=${CONTENT:${#CONTENT}-1:1}

    if [[ $LAST_CHAR == '/' ]];
    then
        CONTENT=${CONTENT:0:-1}
    fi

    echo ${PREFIX}${CONTENT}

done | sort | uniq

etcdctl get $ORIG_PREFIX
