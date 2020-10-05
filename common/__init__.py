import os

# banner
SKY_BLUE = "\033[36m"
END = "\033[0m"
WRITER = "R4U"
VERSION = "Ver0.0.0"
LUOYANG_SHOVEL_BANNER = f"""{SKY_BLUE}\
   __by {WRITER}                          ______               __
  / / __ _____ __ _____ ____ ___ _  / __/ / ___ _  _____ / /
 / /_/ // / _ / // / _ `/ _ / _ `/ _\ \/ _ / _ | |/ / -_/ / 
/____\_,_/\___\_, /\_,_/_//_\_, / /___/_//_\___|___/\__/_/  
             /___/         /___/                 {VERSION}    {END}
"""

#  common const
ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
