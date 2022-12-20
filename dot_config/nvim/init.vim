

" define the leader key
let mapleader="\<SPACE>"

set number relativenumber
" automatic toggling between line number modes when changing windows
augroup numbertoggle
  autocmd!
  autocmd BufEnter,FocusGained,InsertLeave,WinEnter * if &nu && mode() != "i" | set rnu   | endif
  autocmd BufLeave,FocusLost,InsertEnter,WinLeave   * if &nu                  | set nornu | endif
augroup END

" change the direction of new splits
set splitbelow
set splitright

" search highlighting colors
hi Search cterm=NONE ctermfg=white ctermbg=Brown

" reload the config file (Source Vimrc)
nnoremap <leader>sv :source $MYVIMRC<CR>
