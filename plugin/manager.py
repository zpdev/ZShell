from zshell.plugin.session_manager import SessionManagerPlugin
from zshell.plugin.tab_manager import TabManagerPlugin
from zshell.plugin.quick_connect import QuickConnectPlugin
from zshell.plugin.putty_tab import PuttyTabPlugin
from zshell.plugin.upload import UploadPlugin

enable_plugins = [
    SessionManagerPlugin,
    QuickConnectPlugin,
    TabManagerPlugin,
    PuttyTabPlugin,
    UploadPlugin
]
