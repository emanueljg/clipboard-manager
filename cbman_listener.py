import keyboard
from helpers import load_config, load_placeholders, start_cbman


def main():
    cfg = load_config()
    for k, v in load_placeholders().items():
        keyboard.add_abbreviation(
            source_text=cfg['prefix'].replace('Â', '') + k,
            replacement_text=v,
            match_suffix=True,
            timeout=cfg['placeholder_timeout']
        )

    keyboard.add_hotkey(
        cfg['cbman_hotkey'],
        callback=start_cbman,
        suppress=True,
        timeout=cfg['hotkey_timeout']
    )

    keyboard.wait()


if __name__ == '__main__':
    main()
