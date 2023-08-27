# some more aliases
alias xclip='xclip -selection c'
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'
alias .='echo $PWD; echo $PWD | tr -d "\n" | xclip'
alias ..='cd ..; ll'
alias ....='cd ../..; ll'
alias ......='cd ../../..; ll'
alias myip="curl http://ipecho.net/plain; echo"
alias reload='source ~/.bashrc'
alias ssd='cd /media/aaron/SanDisk_SSD'
alias rm='rm -i'
alias lib='cd /home/aaron/lib'
alias g='gvim -p --remote-tab-silent'

### functions
function d {
    cd $1; ll
}

parse_git_branch() {
     git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}

export PS1="\[\033[01;32m\]\u@\h:\[\033[01;33m\]\w\[\033[37m\]\$(parse_git_branch)\[\033[0m\] "
export PROMPT_DIRTRIM=1
