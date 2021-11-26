"""
setup.py
~~~~~~~~

This file helps us distribute the config_project application
"""
import os
from setuptools import setup
from distutils.cmd import Command
from shutil import copy2


class EnvironmentCommand(Command):
    """
    A custom setup.py command to dictate what environment config_app is built for

    Extends
        Command (Command) : A custom command for setup.py command line options
    """

    description = 'Build Config App for a specific environment'
    user_options = [
        # The format is (long option, short option, description).
        ('env=', None, 'Pick an Environment, prod, preprod or dev'),
    ]

    def initialize_options(self):
        """Set default values for options."""
        self.env = ''

    def finalize_options(self):
        """Post-process options."""
        if self.env == 'prod':
            print("you chose prod")
        elif self.env == 'preprod':
            print("you chose pre prod")
        elif self.env == 'dev':
            print("you chose dev")
        else:
            raise ValueError("Invalid Environment Selected " + self.env)

    def run(self):
        """
        Code that is run when the environment command is called from command line.
        Copy the chosen environment config to the application module.
        """

        dir_path = os.path.dirname(os.path.realpath(__file__))

        # Home of all configuration files
        config_project_configuration = dir_path + "/configuration/"

        # Target configuration destinations
        config_project_common_config_loc = dir_path + "/application/common_config.json"
        config_project_environment_config_loc = dir_path + "/application/environment_config.json"

        # Move common config to common config location
        print("Copying " + config_project_configuration + "common_config.json to " + config_project_common_config_loc)
        copy2(config_project_configuration + 'common_config.json', config_project_common_config_loc)

        # Move environment specific configuration to environment config location
        if self.env == 'prod':
            print("Copying " + config_project_configuration + "production_config.json to " + config_project_environment_config_loc)
            copy2(config_project_configuration + 'production_config.json', config_project_environment_config_loc)
        elif self.env == 'preprod':
            print("Copying " + config_project_configuration + "preprod_config.json to " + config_project_environment_config_loc)
            copy2(config_project_configuration + 'preprod_config.json', config_project_environment_config_loc)
        elif self.env == 'dev':
            print("Copying " + config_project_configuration + "proddev_configuction_config.json to " + config_project_environment_config_loc)
            copy2(config_project_configuration + 'dev_config.json', config_project_environment_config_loc)

setup(
    name='config_app',
    version='1.0.0',
    description='Simple code to move configuration files',
    author={'Ben Larking'},
    cmdclass={
        'environment': EnvironmentCommand,
    },
)
