import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from _version import __version__

from panda3d.core import *
from direct.fsm.FSM import FSM
from direct.gui.DirectGui import *
from pandac.PandaModules import WindowProperties

# Import utility modules
from shenko.utils.assets import get_audio_path, get_image_path
from shenko.utils.ui import create_menu_button, create_button, create_version_text, create_logo, cleanup_ui_elements
from shenko.utils.logger import get_logger

# Get logger instance
logger = get_logger()

class AppState(FSM):
    def enterMenu(self):
        logger.info("Entering main menu")
        
        # Load sound effect for button rollover
        self.rollSound = base.loader.loadSfx(get_audio_path("click.ogg"))
        
        # Create version text display
        self.version_text = create_version_text(__version__)
        
        # Create logo with proper path handling
        self.logo_image = create_logo(get_image_path("logo.png"))
        
        # Create main menu buttons
        self.startBtn = create_menu_button("Start", 0.0, self.request, ["StartGame"], self.rollSound)
        self.mapBtn = create_menu_button("View Map", -0.1, self.request, ["Map"], self.rollSound)
        self.optionsBtn = create_menu_button("Options", -0.2, self.request, ["Options"], self.rollSound)
        self.multiplayerBtn = create_menu_button("Multiplayer", -0.3, self.request, ["Multiplayer"], self.rollSound)
        self.helpBtn = create_menu_button("Help", -0.4, self.request, ["Help"], self.rollSound)
        self.exitBtn = create_menu_button("Quit", -0.5, quit, None, self.rollSound)

    def exitMenu(self):
        logger.info("Exiting main menu")
        # Use the cleanup utility instead of manually destroying each element
        cleanup_ui_elements()

    # Creating 'START' Screen
    def enterStartGame(self):
        logger.info("Entering Start Game screen")
        
        # Create menu button using utility
        self.menuBtn = create_button(
            text="Menu",
            pos=(0, 0, -0.8),
            command=self.request,
            extra_args=["Menu"],
            rollover_sound=self.rollSound,
            name="menu_button"
        )
        
        # Load 3D model
        self.panda = loader.loadModel("panda")
        self.panda.reparentTo(render)
        base.cam.setPos(0, -40, 5)

    def exitStartGame(self):
        logger.info("Exiting Start Game screen")
        # Clean up UI elements
        cleanup_ui_elements("menu_button")
        # Remove 3D model
        self.panda.removeNode()

    # Creating 'Map' Screen
    def enterMap(self):
        self.menuBtn = DirectButton(text="Menu",
                                    scale=0.1,
                                    pos=Vec3(0, 0, -0.8),
                                    rolloverSound=self.rollSound,
                                    frameColor=(
                                        (0.2, 0.2, 0.2, 1),  # Normal state: Dark grey
                                        (0.5, 0.5, 0.5, 1),  # Clicked state: Light grey
                                        (0.3, 0.3, 0.3, 1),  # Rollover state: Medium grey
                                        (0.1, 0.1, 0.1, 1)   # Disabled state: Almost black
                                    ),
                                    frameSize=(-2.5, 2.5, -0.3, 0.7),  # Adjusted frame size for larger hit box
                                    text_fg=(0, 1, 1, 1),  # Cyan text color
                                    text_bg=(0.2, 0.2, 0.2, 0),  # Transparent text background
                                    text_scale=(0.8, 0.8),  # Adjusted text size
                                    command=self.request,
                                    extraArgs=["Menu"])
        self.smiley = loader.loadModel("smiley")
        self.smiley.reparentTo(render)
        base.cam.setPos(0, -20, 0)

    def exitMap(self):
        self.menuBtn.destroy()
        self.smiley.removeNode()

    # Creating 'Options' Screen
    def enterOptions(self):
        self.menuBtn = DirectButton(text="Menu",
                                    scale=0.1,
                                    pos=Vec3(0, 0, -0.8),
                                    rolloverSound=self.rollSound,
                                    frameColor=(
                                        (0.2, 0.2, 0.2, 1),  # Normal state: Dark grey
                                        (0.5, 0.5, 0.5, 1),  # Clicked state: Light grey
                                        (0.3, 0.3, 0.3, 1),  # Rollover state: Medium grey
                                        (0.1, 0.1, 0.1, 1)   # Disabled state: Almost black
                                    ),
                                    frameSize=(-2.5, 2.5, -0.3, 0.7),  # Adjusted frame size for larger hit box
                                    text_fg=(0, 1, 1, 1),  # Cyan text color
                                    text_bg=(0.2, 0.2, 0.2, 0),  # Transparent text background
                                    text_scale=(0.8, 0.8),  # Adjusted text size
                                    command=self.request,
                                    extraArgs=["Menu"])
        self.smiley = loader.loadModel("smiley")
        self.smiley.reparentTo(render)
        base.cam.setPos(0, -20, 0)

    def exitOptions(self):
        self.menuBtn.destroy()
        self.smiley.removeNode()

    # Creating 'Multiplayer' Screen
    def enterMultiplayer(self):
        self.menuBtn = DirectButton(text="Menu",
                                    scale=0.1,
                                    pos=Vec3(0, 0, -0.8),
                                    rolloverSound=self.rollSound,
                                    frameColor=(
                                        (0.2, 0.2, 0.2, 1),  # Normal state: Dark grey
                                        (0.5, 0.5, 0.5, 1),  # Clicked state: Light grey
                                        (0.3, 0.3, 0.3, 1),  # Rollover state: Medium grey
                                        (0.1, 0.1, 0.1, 1)   # Disabled state: Almost black
                                    ),
                                    frameSize=(-2.5, 2.5, -0.3, 0.7),  # Adjusted frame size for larger hit box
                                    text_fg=(0, 1, 1, 1),  # Cyan text color
                                    text_bg=(0.2, 0.2, 0.2, 0),  # Transparent text background
                                    text_scale=(0.8, 0.8),  # Adjusted text size
                                    command=self.request,
                                    extraArgs=["Menu"])
        self.smiley = loader.loadModel("smiley")
        self.smiley.reparentTo(render)
        base.cam.setPos(0, -20, 0)

    def exitMultiplayer(self):
        self.menuBtn.destroy()
        self.smiley.removeNode()

    # Creating 'Help' Screen
    def enterHelp(self):
        self.menuBtn = DirectButton(text="Menu",
                                    scale=0.1,
                                    pos=Vec3(0, 0, -0.8),
                                    rolloverSound=self.rollSound,
                                    frameColor=(
                                        (0.2, 0.2, 0.2, 1),  # Normal state: Dark grey
                                        (0.5, 0.5, 0.5, 1),  # Clicked state: Light grey
                                        (0.3, 0.3, 0.3, 1),  # Rollover state: Medium grey
                                        (0.1, 0.1, 0.1, 1)   # Disabled state: Almost black
                                    ),
                                    frameSize=(-2.5, 2.5, -0.3, 0.7),  # Adjusted frame size for larger hit box
                                    text_fg=(0, 1, 1, 1),  # Cyan text color
                                    text_bg=(0.2, 0.2, 0.2, 0),  # Transparent text background
                                    text_scale=(0.8, 0.8),  # Adjusted text size
                                    command=self.request,
                                    extraArgs=["Menu"])
        self.smiley = loader.loadModel("smiley")
        self.smiley.reparentTo(render)
        base.cam.setPos(0, -20, 0)

    def exitHelp(self):
        self.menuBtn.destroy()
        self.smiley.removeNode()

def toggle_fullscreen():
    """
    Toggle between windowed and fullscreen modes.
    Also accounts for different screen resolutions including 4K displays.
    """
    win_props = WindowProperties()
    current_props = base.win.getProperties()
    
    logger.info("Toggling fullscreen mode")
    
    # Get the display resolution - if available
    try:
        # For modern systems with multi-monitors, try to get proper resolution
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.destroy()
    except:
        # Fallback to typical resolutions
        logger.warning("Could not determine screen resolution, using defaults")
        if current_props.getFullscreen():
            # Currently in fullscreen, going to windowed
            screen_width, screen_height = 1280, 720
        else:
            # Going to fullscreen, try to detect if it's a 4K display
            # If current window size is already large, assume 4K
            if current_props.getXSize() > 1920:
                screen_width, screen_height = 3840, 2160
            else:
                screen_width, screen_height = 1920, 1080
    
    if current_props.getFullscreen():
        # Switch to windowed mode
        win_props.setSize(min(1280, screen_width-100), min(720, screen_height-100))
        win_props.setFullscreen(False)
        logger.info(f"Switching to windowed mode: {win_props.getXSize()}x{win_props.getYSize()}")
    else:
        # Switch to fullscreen mode
        win_props.setSize(screen_width, screen_height)
        win_props.setFullscreen(True)
        logger.info(f"Switching to fullscreen mode: {screen_width}x{screen_height}")

    base.win.requestProperties(win_props)



def quit():
    """
    Properly exit the application with logging.
    """
    logger.info("Quitting Shenko application")
    
    try:
        # Attempt to clean up any remaining UI elements
        cleanup_ui_elements()
        
        # Log successful exit
        logger.info("Shenko exited successfully")
        print("Quitting Shenko...")
    except Exception as e:
        # Log any errors during shutdown
        logger.error(f"Error during shutdown: {e}")
    
    # Exit the application
    sys.exit(0)
