"""
Simple config file for using configparser to get system settings
"""

import os
import sys
import platform
import configparser

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the app name from app_config.py
try:
    from app_config import APP_NAME
except ImportError:
    # If app_config.py doesn't exist, default to UniqueName
    APP_NAME = "UniqueName"

class Config(object):
    def __init__(self):
        self._settings = {}
        self.reload()
        
    def _load(self):
        # Load local config from the default locations if exists.  If not, look at the "root" of the local
        # user profile folder (ex: /Users/<vzid>/{APP_NAME}.conf or C:\Users\<vzid>\{APP_NAME}.conf)
        path = os.path.join(os.path.expanduser('~'), f'{APP_NAME}.conf')
        if os.path.exists(path):
            self._load_file(path)
            
    def _load_file(self, filename):
        source = configparser.ConfigParser()
        source.read(filename)
        for section in source.sections():
            if section not in self._settings:
                self._settings[section] = {}
            for option in source.options(section):
                value = source.get(section, option)
                self._settings[section][option] = value
                
    def get_config(self, section, setting, default=None):
        try:
            return self._settings[section][setting]
        except:
            return default
            
    def reload(self):
        self._settings = {}
        self._load()
        
    def dump(self):
        output = []
        for section in self._settings:
            output.append(f"[{section}]")
            for option in self._settings[section]:
                output.append(f"    {option}: {self._settings[section][option]}")
            output.append("")
        return "\n".join(output)
