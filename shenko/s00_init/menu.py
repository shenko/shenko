import sys

from panda3d.core import *
from direct.fsm.FSM import FSM
from direct.gui.DirectGui import *
from pandac.PandaModules import WindowProperties

class AppState(FSM):
    def enterMenu(self):
        # We will need to fix this so it automatically gets version!
        self.version_text = OnscreenText(text="v0.1.83", pos=(0.95, -0.95), scale=0.05,
                                    fg=(0, 1, 1, 1), bg=(0, 0, 0, .5), align=TextNode.ACenter, mayChange=1)

        self.rollSound = base.loader.loadSfx("assets/audio/click.ogg")

        # Creating the 'START' Button
        self.startBtn = DirectButton(text="Start",
                                     scale=0.10,
                                     pos=Vec3(0, 0, 0.0),
                                     rolloverSound=self.rollSound,
                                     #frameColor=(0.2, 0.2, 0.2, 1),  # Dark grey interior
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
                                     extraArgs=["StartGame"])
        # Creating the 'Map' Button
        self.mapBtn = DirectButton(text="View Map",
                                        scale=0.10,
                                        pos=Vec3(0, 0, -0.1),
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
                                        extraArgs=["Map"])
        # Creating the 'options' Button
        self.optionsBtn = DirectButton(text="Options",
                                        scale=0.10,
                                        pos=Vec3(0, 0, -0.2),
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
                                        extraArgs=["Options"])
        # Creating the 'Multiplayer' Button
        self.multiplayerBtn = DirectButton(text="Multiplayer",
                                        scale=0.10,
                                        pos=Vec3(0, 0, -0.3),
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
                                        extraArgs=["Multiplayer"])
        # Creating the 'Help' Button
        self.helpBtn = DirectButton(text="Help",
                                        scale=0.10,
                                        pos=Vec3(0, 0, -0.4),
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
                                        extraArgs=["Help"])
        # Creating the 'Exit' Button
        self.exitBtn = DirectButton(text="Quit",
                                        scale=0.10,
                                        pos=Vec3(0, 0, -0.5),
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
                                        command=quit)

        # Creating the Logo
        desired_height = .15  # Adjust this to your desired height
        aspect_ratio = 780 / 105

        # Calculate the corresponding width based on the desired height and aspect ratio
        desired_width = desired_height * aspect_ratio
        self.logo_image = OnscreenImage(image='assets/images/logo.png', pos=(0, 0, .4), scale=(desired_width, 1, desired_height))


    def exitMenu(self):
        # Destroy the OnscreenText element
        self.version_text.destroy()
        #self.version_text = None  # Optionally set the reference to None
        self.logo_image.destroy()
        self.startBtn.destroy()
        self.mapBtn.destroy()
        self.optionsBtn.destroy()
        self.multiplayerBtn.destroy()
        self.helpBtn.destroy()
        #self.exitBtn is not needed cause we are quiting.

    # Creating 'START' Screen
    def enterStartGame(self):
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
        self.panda = loader.loadModel("panda")
        self.panda.reparentTo(render)
        base.cam.setPos(0, -40, 5)

    def exitStartGame(self):
        self.menuBtn.destroy()
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
    win_props = WindowProperties()

    if base.win.getProperties().getFullscreen():
        win_props.setSize(800, 600)
        win_props.setFullscreen(False)
        #self.status.setText("Window Mode")
    else:
        win_props.setSize(1280, 800)   # we will need to fix this for 4k scaling
        win_props.setFullscreen(True)
        #self.status.setText("Fullscreen Mode")

    base.win.requestProperties(win_props)



def quit():
    print("quitting shenko")
    sys.exit()