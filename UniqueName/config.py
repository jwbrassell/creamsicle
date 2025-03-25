"""
Central configuration for the Django project.
This module serves as the single source of truth for all configuration settings.
"""

import os
import sys
import platform
import configparser
import importlib.util

class Config:
    _instance = None
    
    @classmethod
    def get_instance(cls):
        """Singleton pattern to ensure only one config instance exists"""
        if cls._instance is None:
            cls._instance = Config()
        return cls._instance
    
    def __init__(self):
        # Only initialize if this is the first instance
        if Config._instance is not None:
            return
            
        # Determine the app name from the directory structure
        self.app_dir = os.path.dirname(os.path.abspath(__file__))
        self.app_name = os.path.basename(self.app_dir)
        self.project_root = os.path.dirname(self.app_dir)
        
        # Add project root to Python path if not already there
        if self.project_root not in sys.path:
            sys.path.append(self.project_root)
            
        self._settings = {}
        self.reload()
        
    def _load(self):
        # Load local config from the default locations if exists.  If not, look at the "root" of the local
        # user profile folder (ex: /Users/<vzid>/{app_name}.conf or C:\Users\<vzid>\{app_name}.conf)
        path = os.path.join(os.path.expanduser('~'), f'{self.app_name}.conf')
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
    
    def get_settings_module(self):
        """Return the settings module string for Django"""
        return f"{self.app_name}.settings"
            
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

# Create the singleton instance
config = Config.get_instance()
