#!bin/bash

# uncomment color output in .bashrc
sed -i '/force_color_prompt/\s/^#\/\/' ~/.bashrc

# install fonts
fc-cache -fv