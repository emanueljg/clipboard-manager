import os
import pickle

import psutil
import yaml


def load_config(path='config.yaml'):
    """Load the YAML config file."""
    with open(path, 'r') as f:
        return yaml.safe_load(f)


cfg = load_config()


def save_placeholders(placeholders):
    """Save placeholders to `cfg['placeholders_path']` as specified in `config.yaml`."""
    with open(cfg['placeholders_path'], 'wb') as f:
        pickle.dump(placeholders, f)


def load_placeholders():
    """Return either loaded placeholders from `cfg['placeholders_path']` or an empty dict."""
    if os.path.exists(cfg['placeholders_path']):
        with open(cfg['placeholders_path'], 'rb') as f:
            return pickle.load(f)
    else:
        return {}


def start_cbman():
    if "cbman.exe" not in {p.name() for p in psutil.process_iter()}:
        os.startfile(cfg['cbman_path'])
