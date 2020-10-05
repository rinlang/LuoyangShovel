import toml
import os


if __name__ == "__main__":
    config = toml.load('./config.toml')
    print(config)
else:
    config = toml.load(os.path.dirname(__file__)+'/config.toml')
