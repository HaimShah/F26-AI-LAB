previous_mode = None

def choose_mode(temperature, occupied):
    global previous_mode

    if not occupied:
        target_mode = "OFF"
    elif temperature < 18:
        target_mode = "HEAT"
    elif temperature > 26:
        target_mode = "COOL"
    else:
        target_mode = "OFF"

    send_command = target_mode != previous_mode
    previous_mode = target_mode

    return target_mode, send_command


tests = [
    (17, True),
    (17, True),
    (18, True),
    (26, True),
    (27, True),
    (27, True),
    (22, False)
]

for temperature, occupied in tests:
    old_mode = previous_mode
    target, send = choose_mode(temperature, occupied)

    result = "SEND COMMAND" if send else "NO COMMAND"

    print(
        "Previous:", old_mode,
        "| Temperature:", temperature,
        "| Occupied:", occupied,
        "| Target:", target,
        "|", result
    )