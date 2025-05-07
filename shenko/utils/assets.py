"""
Assets utility module for Shenko.

This module provides functions for resolving paths to assets regardless of 
the current working directory, making the code more robust across platforms
and deployment methods.
"""

import os
import sys

# Base paths
_ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets')

def get_asset_path(relative_path):
    """
    Resolve the absolute path to an asset.
    
    Args:
        relative_path (str): Path relative to the assets directory.
                            Example: 'audio/click.ogg'
    
    Returns:
        str: The absolute path to the asset.
    """
    # First try the ideal location (package assets directory)
    path = os.path.join(_ASSETS_DIR, relative_path)
    
    # If it exists, return it
    if os.path.exists(path):
        return path
    
    # If not found, try the root directory location
    path = os.path.join(_ROOT_DIR, 'assets', relative_path)
    
    # If it exists, return it
    if os.path.exists(path):
        return path
    
    # If still not found, try a relative path from the current working directory
    # This is a fallback for development/testing scenarios
    path = os.path.join('assets', relative_path)
    
    return path

def get_audio_path(filename):
    """
    Get the path to an audio file.
    
    Args:
        filename (str): Audio filename, e.g., 'click.ogg'
    
    Returns:
        str: The path to the audio file.
    """
    return get_asset_path(os.path.join('audio', filename))

def get_image_path(filename):
    """
    Get the path to an image file.
    
    Args:
        filename (str): Image filename, e.g., 'logo.png'
    
    Returns:
        str: The path to the image file.
    """
    return get_asset_path(os.path.join('images', filename))
