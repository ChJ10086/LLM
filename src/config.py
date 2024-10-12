# config.py

import yaml
import os

class ClassPropertyDescriptor:
    def __init__(self, fget):
        self.fget = fget

    def __get__(self, instance, owner):
        return self.fget(owner)

def classproperty(func):
    return ClassPropertyDescriptor(func)

class Config:
    _tokens_config = None
    _property_config = None

    DATA_DIR = os.path.join(os.path.dirname(__file__), '../data')

    @classproperty
    def key(cls):
        """Access the API key."""
        if cls._tokens_config is None:
            tokens_path = os.path.join(cls.DATA_DIR, 'tokens.yaml')
            try:
                with open(tokens_path, 'r') as file:
                    cls._tokens_config = yaml.safe_load(file)
            except FileNotFoundError:
                cls._tokens_config = {}
        return cls._tokens_config.get('api_key', '')

    @classproperty
    def api(cls):
        """Access the API URL from the configuration."""
        if cls._property_config is None:
            property_path = os.path.join(cls.DATA_DIR, 'property.yaml')
            try:
                with open(property_path, 'r') as file:
                    cls._property_config = yaml.safe_load(file)
            except FileNotFoundError:
                cls._property_config = {}
        return cls._property_config.get('api_url', '')

    @classproperty
    def model_mappings(cls):
        """Access the model mappings from the configuration."""
        if cls._property_config is None:
            cls.api  # Ensure _property_config is loaded
        return cls._property_config.get('model_mappings', {})
