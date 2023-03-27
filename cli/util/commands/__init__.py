from .command_build import CommandBuild
from .command_push import CommandPush
from .command_wipe import CommandWipe

available_commands = {
    'build': CommandBuild,
    'push': CommandPush,
    'wipe': CommandWipe,
}
