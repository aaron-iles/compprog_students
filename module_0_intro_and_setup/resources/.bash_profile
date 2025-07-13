# Aliases
alias ll='ls -alF'
alias la='ls -A'
alias rm='rm -i'
alias testme='echo it worked!'

parse_git_branch() {
     git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}

# Prompt formatting
export PS1="\[\033[01;32m\]\u@\h:\[\033[01;33m\]\w\[\033[37m\]\$(parse_git_branch)\[\033[0m\] "
export PROMPT_DIRTRIM=1
