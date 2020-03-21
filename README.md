# fzf-marks-advanced

A bookmarking plugin for zsh, inspired by [fzf-marks](https://github.com/urbainvaes/fzf-marks) and based on [fzf](https://github.com/junegunn/fzf).

## Functionality

This plugin for zsh allows access to different kinds of bookmarks, coming from three different sources.
1) Folders that you bookmark e.g. on Nautilus, usually found in `~/.config/gtk-3.0/bookmarks`
2) Folders that you also want to bookmark, but not to appear in Nautilus
3) Files that you want to bookmark

There are 4 commands.

* `CTRL-F`: Insert bookmarked files/directory, from sources 1., 2., 3., into current terminal line
* `CTRL-O`: Switch `$PWD` to a bookmarked directory, from sources 1., 2.
* `F1`: Insert/update bookmark pointing to `$PWD` to source 2.
* `F2`: Insert/update bookmark pointing to given file to source 3.

## Non-Functionality

Some functionality of [fzf-marks](https://github.com/urbainvaes/fzf-marks) is not included:

* Deletion and modification of bookmarks is not possible. Idea: Make a shortcut to edit these manually in your favorite editor.

Further things that would be nice to have in the future:

* Annotate the files with a default program, so one can launch a file on the fly from desktop

## How to use
Just copy the this folder to where you store your plugins for zsh. The plugin is then initialized by running `fzf-marks-advanced.plugin.zsh`. Don't forget to set your settings.

## Configuration
The following parameters **have to be** set.

```
FZFMA_DIRS_PRIMARY="$HOME/.config/gtk-3.0/bookmarks"
FZFMA_DIRS_SECONDARY="my/bookmarks/dirs"
FZFMA_FILES="my/bookmarks/files"
```

The following parameters **may be** set, in order to enable hotkeys.
```
FZFMA_KEY_INSERT="^f"      # CTRL-F
FZFMA_KEY_OPEN="^o"        # CTRL-O
FZFMA_KEY_ADD_DIR="^[OP"   # F1 key
FZFMA_KEY_ADD_FILE="^[OQ"  # F2 key
```

## License

MIT
