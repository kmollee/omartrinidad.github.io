title: Vim Notes
date: 2013-04-25
category: Blog
tags: Vim

I used Vim since 2011. But only since 2013 I started using Vim in the right way.
When I write _in the right way_ I mean I started to think like a real _vimer_. In
this post I want to write a little bit of things I am learning each day:

# Changes in my `.vimrc`

## How to avoid use keyboard arrows

Use the keys `h`, `j`, `k`, and `l` is one of the more esoteric features of
`Vim`, but also is one of the most powerful. In order to avoid use the normal
arrow keys is possible lock them.

    nnoremap <up> <nop>
    nnoremap <down> <nop>
    nnoremap <left> <nop>
    nnoremap <right> <nop>
    inoremap <up> <nop>
    inoremap <down> <nop>
    inoremap <left> <nop>
    inoremap <right> <nop>

#Vim Text Objects.

#Vim System Clipboard

#mappings

## <Leader> key

-> I and A
-> zz, zt, zb
-> Ctrl N
-> Ctrl B and Ctrl F
-> ctags ?
-> Ctrl E and Ctrl Y
-> Ctrl A and Ctrl X
-> vim match
-> gq} and y}
-> Vim visual mode
-> (, ), { and }
-> ''
-> c$, c4w. r [normal mode]
-> ca" or ci" -> ci) or ca)
-> ya< or ya> or yi< or yi>

OpenOffice
:set tw=0 wrap linebreak

