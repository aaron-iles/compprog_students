# Aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'
alias ..='cd ..; ll'
alias ....='cd ../..; ll'
alias rm='rm -i'
alias g='gvim -p --remote-tab-silent'

# Functions
function d {
    cd $1; ll
}

parse_git_branch() {
     git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}

# Prompt formatting
export PS1="\[\033[01;32m\]\u@\h:\[\033[01;33m\]\w\[\033[37m\]\$(parse_git_branch)\[\033[0m\] "
export PROMPT_DIRTRIM=1
