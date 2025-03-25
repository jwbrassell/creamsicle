import os
from django.core.management.templates import TemplateCommand
from UniqueName.config import config
from pathlib import Path

# Get BASE_DIR from config
BASE_DIR = Path(config.project_root)

class Command(TemplateCommand):
    help = (
        "Creates a Django app directory structure for the given app name in "
        "the 'apps' directory. Uses custom templates. Use this instead of 'startapp'"
    )
    
    missing_args_message = "You must provide an application name."
    
    def add_arguments(self, parser):
        parser.add_argument("app_name", nargs="+", type=str)
    
    def handle(self, **options):
        new_app_name = options["app_name"][0].lower().strip()
        if not new_app_name:
            print("Please provide a valid app name.")
            return
        
        new_folder = os.path.join(BASE_DIR, 'apps', f'{new_app_name}')
        
        # Create a folder in the apps directory
        if not os.path.exists(new_folder) and new_app_name:
            os.mkdir(new_folder)
        
        options = {'verbosity': 1, 'settings': None, 'pythonpath': None, 'traceback': False, 'no_color': False,
                  'force_color': False, 'name': new_app_name, 'directory': new_folder,
                  'template': f'{config.app_name}/creation_templates/app_template', 'extensions': ['.py'], 'files': []}
        app_name = options.pop("name")
        target = options.pop("directory")
        try:
            super().handle("app", app_name, target, **options)
        except Exception as e:
            print(f"__________(e)")
            if os.path.exists(new_folder) and new_app_name and "already exists" not in str(e):
                os.rmdir(new_folder)
