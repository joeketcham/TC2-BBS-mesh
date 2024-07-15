from command_handlers import (
    handle_help_command, handle_quick_help_command
)

class MainMenu(enumerate):
    q  = handle_quick_help_command
    b = lambda sender_id, interface: handle_help_command(sender_id, interface, 'bbs')
    u = lambda sender_id, interface: handle_help_command(sender_id, interface, 'utilities')
    x = handle_help_command

main_menu_handlers = {
    "q": handle_quick_help_command,
    "b": lambda sender_id, interface: handle_help_command(sender_id, interface, 'bbs'),
    "u": lambda sender_id, interface: handle_help_command(sender_id, interface, 'utilities'),
    "x": handle_help_command
}