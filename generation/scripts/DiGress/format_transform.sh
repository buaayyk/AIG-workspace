#!/bin/bash

for graph_limit in "50" "100" "150" "200" 
do
    python scripts/DiGress/format_transform.py ${graph_limit}
done