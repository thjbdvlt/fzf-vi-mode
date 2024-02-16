# easy fzf vi-mode

automate bindings for [fzf](https://github.com/junegunn/fzf) with (vim-like) normal (and insert) mode.

__wonderful software fzf__ can be configured (with `--bind` option) to have something like a vim-like 'normal mode':

```bash
fzf --bind=j:down,k:up \
    --bind=start:unbind(i,j,k) \
    --bind=esc:disable-search+rebind(i,j,k) \
    --bind=i:enable-search+unbind(i,j,k)
```

but it can quickly become messy, and very unfun to write. as here:

```bash
    --bind=j:down,k:up,s:jump,p:toggle-preview \
    --bind=h:backward-char,l:forward-char,e:forward-word,b:backward-word \
    --bind=d:clear-query \
    --bind='y:execute(echo {} | xsel -b)' \
    --bind=E:preview-half-page-down,U:preview-half-page-up \
    --bind=c:cancel,x:forward-char+backward-delete-char \
    --bind=X:backward-delete-char \
    --bind=start:enable-search+unbind(e,j,s,p,h,l,é,b,d,y,E,U,c,x,X,i,a,A,I)  \
    --bind=i:enable-search+unbind(j,k,s,p,h,l,e,b,d,y,E,U,c,x,X,i,a,A,I) \
    --bind=a:enable-search+unbind(j,k,s,p,h,l,e,b,d,y,E,U,c,x,X,i,a,A,I)+forward-char \
    --bind=A:enable-search+unbind(j,k,s,p,h,l,e,b,d,y,E,U,c,x,X,i,a,A,I)+end-of-line \
    --bind=I:enable-search+unbind(j,k,s,p,h,l,e,b,d,y,E,U,c,x,X,i,a,A,I)+beginning-of-line \
    --bind=esc:disable-search+rebind(j,k,s,p,h,l,e,b,d,y,E,U,c,x,X,i,a,A,I) \
    --bind=®:backward-kill-word,change:top,backward-eof:abort
```

many things had to be reapeted, and it is required to be consistent: worth to script it.

the simple script provided here is based on a simple configuration file, which will export a single line option for fzf.

here is the one which will generate options above:

```toml
[mode]
escape = esc
insert_before = i
insert_after = a 
insert_end_line = A
insert_beginning_line = I

[normal]
j = down
k = up
s = jump
p = toggle-preview
h = backward-char
l = forward-char
e = forward-word
b = backward-word
d = clear-query
y = execute(echo {} | xsel -b)
E = preview-half-page-down
U = preview-half-page-up
c = cancel
x = forward-char+backward-delete-char
X = backward-delete-char

[insert]
® = backward-kill-word
change = top
backward-eof = abort
```
