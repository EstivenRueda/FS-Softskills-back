def strtobool(val):
    """Convierte una representación en string de verdad a true (1) o false (0).

    Los valores verdadersos son 'y', 'yes', 't', 'true', 'on', y '1'; los valores falsos
    son 'n', 'no', 'f', 'false', 'off', y '0'. Genera ValueError si
    'val' es cualquier otra cosa.
    """
    val = val.lower()
    if val in ("y", "yes", "t", "true", "on", "1"):
        return 1
    if val in ("n", "no", "f", "false", "off", "0"):
        return 0
    raise ValueError(f"invalid truth value {val:!r}")
