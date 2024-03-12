# easy fzf vi-mode

automates configuration for a pseudo-modal __vim__-like [fzf](https://github.com/junegunn/fzf) (insert and normal modes).

__wonderful software fzf__ can be configured (with `--bind` option) to have something like a vim-like 'normal mode':

```bash
fzf --bind=j:down,k:up \
    --bind=start:unbind(i,j,k) \
    --bind=esc:disable-search+rebind(i,j,k) \
    --bind=i:enable-search+unbind(i,j,k)
```

 with the options above, pressing `esc` will rebind `j` to `up` and `k` to `down`, just like in vim: it's a pseudo-normal-mode. then, pressing `i` will unbind them so they will just be put in query, as they should (pseudo-insert-mode).

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

same patterns again and again, plus it is required to be consistent: worth to script it. the simple python script provided here is based on a simple configuration file, which will export a single line option for fzf (that i personally just copy-paste and append it to `FZF_DEFAULT_OPTS` in my `.bashrc`). here is the configuration which will generate options above:

```conf
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

dependancies
------------

no dependancies, it uses the [configparser](https://docs.python.org/3/library/configparser.html) standard library.
