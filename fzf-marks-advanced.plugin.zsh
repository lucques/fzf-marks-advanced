FZFMA_BASE=$(dirname $0)

# Core functions

function fzma-select-multi-files {
    (paste -sd '\n' $FZFMA_FILES $FZFMA_DIRS_PRIMARY $FZFMA_DIRS_SECONDARY) |
    awk NF |   # Remove empty lines
    ${FZFMA_BASE}/raw-to-formatted.py |
    fzf --ansi \
    --select-1 \
    --multi |
    ${FZFMA_BASE}/formatted-to-paths.py
}

function fzma-select-single-dir {
    (paste -sd '\n' $FZFMA_DIRS_PRIMARY $FZFMA_DIRS_SECONDARY) |
    awk NF |   # Remove empty lines
    ${FZFMA_BASE}/raw-to-formatted.py |
    fzf --ansi \
    --select-1 |
    ${FZFMA_BASE}/formatted-to-paths.py
}

# Define widgets

function fzma-insert-widget() {
    LBUFFER="${LBUFFER}$(fzma-select-multi-files)"
    local ret=$?
    zle reset-prompt
    return $ret
}
zle -N fzma-insert-widget

function fzma-open-widget() {
    local target="$(fzma-select-single-dir)" || return
    if [[ -d ${target} ]]; then
        cd "${target}"
    fi
    zle && zle reset-prompt
}
zle -N fzma-open-widget

# Define plain functions

function bookmark-dir() {
    local name
    echo "Save current directory as bookmark."
    vared -p 'Name: ' name
    ${FZFMA_BASE}/save-bookmark.py "$FZFMA_DIRS_SECONDARY" "$name" "$PWD"
}

function bookmark-file() {
    local file_path name
    echo "Save file as bookmark."
    vared -p 'Path: ' file_path
    vared -p 'Name: ' name
    ${FZFMA_BASE}/save-bookmark.py "$FZFMA_FILES" "$name" "$file_path"
}

# Bind hotkeys

if [ "${FZFMA_KEY_INSERT}" ]; then
    bindkey ${FZFMA_KEY_INSERT} fzma-insert-widget
fi

if [ "${FZFMA_KEY_OPEN}" ]; then
    bindkey ${FZFMA_KEY_OPEN} fzma-open-widget
fi

if [ "${FZFMA_KEY_ADD_DIR}" ]; then
    bindkey -s ${FZFMA_KEY_ADD_DIR} 'bookmark-dir\n'
fi

if [ "${FZFMA_KEY_ADD_FILE}" ]; then
    bindkey -s ${FZFMA_KEY_ADD_FILE} 'bookmark-file\n'
fi