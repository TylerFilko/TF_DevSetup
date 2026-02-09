# MAC 2025
# Setup scrip updates

# Brew install ----------------------------------
yes | brew install asdf coreutils git delve docker terraform tflint openshift-cli gh awscli kustomize
yes | brew install --cask visual-studio-code
yes | brew install --cask insomnia

# dev tooling install ---------------------------
yes | brew install kubectl derailed/k9s/k9s kind
kubectl version --client

# ASDF plugings ---------------------------------
asdf plugin add golang https://github.com/asdf-community/asdf-golang.git
asdf install golang latest

asdf plugin add golangci-lint
asdf install golangci-lint latest

asdf plugin add python
asdf python latest

asdf plugin add direnv
asdf install direnv

# defur to finish fo asdf add calls -------------
asdf reshim golang 
asdf reshim 

# ZSH plugings ----------------------------------
# oh my zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Env setup for ZSH -----------------------------
cat zshprofile.template.txt >> ~/.zshprofile # once per login
cat zshrc.template.txt >> ~/.zshrc           # once per interactive shell

# Optional Installs ----------------------------------

read -rp 'install Kind? (y/n) : ' kindInstallBool
if [[ $kindInstallBool == "y" ]]
    yes | brew install kind
else
    echo "Will not install Kind"
fi
