#!/usr/bin/env bash
set -e
source ${ROVER_SCRIPTS_ROOT}/utils/_base.sh

# SCRIPT CONTENT

### ------- Bash script example -------
warning "Colored bash command"
information "$(ls)"
# Далее опционально, нужно установить gum (описано в scripts/README.md)
#adasd


### ------- Python script example -----
python3 -c "
from utils import info
print(info('Python scripting!'))
"
greeting=$(gum choose "Hi" "Hello")
who=$(gum input --value "nobody :(" --placeholder "name")
gum confirm "Print?" && cecho -c 'magenta' "${greeting} from ${who}"

### ------- ZX script example ---------
# Опционально, нужно установить zx (описано в scripts/README.md)
# Но штука классная
zx <<'EOF'
let current_dir = await $`pwd`
await $`echo "We are in ${current_dir}"`
EOF
