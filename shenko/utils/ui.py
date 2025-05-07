"""
UI utility module for Shenko.

This module provides utility functions and classes for creating consistent UI elements
and reducing code duplication in UI-related code.
"""

from panda3d.core import Vec3, TextNode
from direct.gui.DirectGui import DirectButton, OnscreenText, OnscreenImage

# Default UI colors
COLORS = {
    'text': (0, 1, 1, 1),  # Cyan text
    'bg': (0, 0, 0, 0.5),  # Semi-transparent black background
    'button': {
        'normal': (0.2, 0.2, 0.2, 1),    # Normal state: Dark grey
        'click': (0.5, 0.5, 0.5, 1),     # Clicked state: Light grey
        'rollover': (0.3, 0.3, 0.3, 1),  # Rollover state: Medium grey
        'disabled': (0.1, 0.1, 0.1, 1)   # Disabled state: Almost black
    }
}

# UI Elements tracking for easier cleanup
ui_elements = {}

def create_button(text, pos, command=None, extra_args=None, scale=0.1, 
                  rollover_sound=None, name=None, parent_group=None):
    """
    Create a standardized button with consistent styling.
    
    Args:
        text (str): The button text.
        pos (tuple or Vec3): The position (x, y, z).
        command (callable, optional): Function to call when button is clicked.
        extra_args (list, optional): Arguments to pass to the command.
        scale (float, optional): Button scale.
        rollover_sound (Sound, optional): Sound to play on rollover.
        name (str, optional): Unique name for tracking this button.
        parent_group (str, optional): Group name for batch cleanup.
        
    Returns:
        DirectButton: The created button.
    """
    # Convert tuple to Vec3 if needed
    if isinstance(pos, tuple):
        pos = Vec3(*pos)
    
    # Create the button with standard styling
    button = DirectButton(
        text=text,
        scale=scale,
        pos=pos,
        rolloverSound=rollover_sound,
        frameColor=(
            COLORS['button']['normal'],    # Normal state
            COLORS['button']['click'],     # Clicked state
            COLORS['button']['rollover'],  # Rollover state
            COLORS['button']['disabled']   # Disabled state
        ),
        frameSize=(-2.5, 2.5, -0.3, 0.7),  # Standard frame size
        text_fg=COLORS['text'],            # Text color
        text_bg=(0.2, 0.2, 0.2, 0),        # Text background
        text_scale=(0.8, 0.8),             # Text size
        command=command,
        extraArgs=extra_args if extra_args else []
    )
    
    # Track the button if a name is provided
    if name:
        ui_elements[name] = button
    elif parent_group:
        if parent_group not in ui_elements:
            ui_elements[parent_group] = []
        ui_elements[parent_group].append(button)
    
    return button

def create_version_text(version, pos=(0.95, -0.95), scale=0.05):
    """
    Create the version text display.
    
    Args:
        version (str): Version string.
        pos (tuple, optional): Position (x, y).
        scale (float, optional): Text scale.
        
    Returns:
        OnscreenText: The created text element.
    """
    version_text = OnscreenText(
        text=f"v{version}", 
        pos=pos, 
        scale=scale,
        fg=COLORS['text'], 
        bg=COLORS['bg'], 
        align=TextNode.ACenter, 
        mayChange=1
    )
    
    # Track the element
    ui_elements['version_text'] = version_text
    
    return version_text

def create_logo(image_path, pos=(0, 0, 0.4), height=0.15):
    """
    Create the logo image.
    
    Args:
        image_path (str): Path to the logo image.
        pos (tuple, optional): Position (x, y, z).
        height (float, optional): Desired height of the logo.
        
    Returns:
        OnscreenImage: The created image element.
    """
    # Standard aspect ratio for the logo
    aspect_ratio = 780 / 105
    
    # Calculate width based on height and aspect ratio
    width = height * aspect_ratio
    
    # Create the image
    logo = OnscreenImage(
        image=image_path, 
        pos=pos, 
        scale=(width, 1, height)
    )
    
    # Track the element
    ui_elements['logo'] = logo
    
    return logo

def create_menu_button(text, pos_z, command, extra_args=None, rollover_sound=None):
    """
    Create a standard menu button with vertical positioning.
    
    Args:
        text (str): Button text.
        pos_z (float): Vertical position (Z coordinate).
        command (callable): Function to call when clicked.
        extra_args (list, optional): Arguments to pass to the command.
        rollover_sound (Sound, optional): Sound to play on rollover.
        
    Returns:
        DirectButton: The created button.
    """
    return create_button(
        text=text,
        pos=(0, 0, pos_z),
        command=command,
        extra_args=extra_args,
        rollover_sound=rollover_sound,
        name=f"{text.lower()}_button"
    )

def cleanup_ui_elements(group_name=None):
    """
    Clean up UI elements to prevent memory leaks.
    
    Args:
        group_name (str, optional): If provided, only clean up elements in this group.
    """
    global ui_elements
    
    if group_name:
        # Clean up only the specified group
        if group_name in ui_elements:
            elements = ui_elements.pop(group_name)
            if isinstance(elements, list):
                for element in elements:
                    element.destroy()
            else:
                elements.destroy()
    else:
        # Clean up all elements
        for key, elements in list(ui_elements.items()):
            if isinstance(elements, list):
                for element in elements:
                    element.destroy()
            else:
                elements.destroy()
        ui_elements = {}
