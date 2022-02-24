#!/usr/bin/env bash
set -e
source ${ROVER_SCRIPTS_ROOT}/_base.sh

# SCRIPT CONTENT

warning "Colored bash command"

python3 -c "
from pprint import pprint
pprint('Multiline python command')
"

cecho -c 'cyan' "`python3 -c \"print('Colored python command')\"`"
