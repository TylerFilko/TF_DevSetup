# MAC 2025
# Setup scrip updates

# Brew install ----------------------------------
yes | brew install asdf coreutils git delve docker terraform tflint
yes | brew install --cask visual-studio-code
yes | brew install --cask insomnia

# dev tooling install
yes | brew install kubectl derailed/k9s/k9s kind
kubectl version --client

# ASDF plugings ---------------------------------
asdf plugin add golang https://github.com/asdf-community/asdf-golang.git
asdf install golang latest

asdf plugin add golangci-lint
asdf install golangci-lint latest


asdf reshim golang # defur to finish fo asdf add calls

# Env setup for ZSH -----------------------------
cat zshprofile_template.txt >> ~/.zshprofile # once per login
cat zshrc_teamplate.txt >> ~/.zshrc           # once per interactive shell