#!/usr/bin/env python3
"""
Shenko Release Manager - Automated Multi-Platform Release Script
Releases to: GitHub, PyPI, Docker Hub, and Snapcraft

Usage: python3 release_shenko.py [patch|minor|major]
"""

import os
import sys
import subprocess
import time
import logging
from datetime import datetime
from pathlib import Path
import getpass

# Configuration
SHENKO_PATH = Path(__file__).parent.absolute()
LOG_FILE = SHENKO_PATH / "release.log"
VERSION_FILES = [
    "_version.py",
    "shenko/__init__.py", 
    "pyproject.toml",
    "Dockerfile",
    "snap/snapcraft.yaml",
    "setup.cfg"
]

class ShenkoReleaseManager:
    """Automated release manager for all platforms."""
    
    def __init__(self, bump_type="patch"):
        self.bump_type = bump_type
        self.setup_logging()
        self.start_time = time.time()
        self.docker_username = None
        self.docker_password = None
        self.current_version = None
        self.new_version = None
        
    def setup_logging(self):
        """Setup logging system."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(LOG_FILE, encoding='utf-8'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
        
    def run_command(self, cmd, capture=True, check=True, timeout=1800):
        """Run shell command with error handling."""
        self.logger.info(f"Running: {' '.join(cmd) if isinstance(cmd, list) else cmd}")
        try:
            if isinstance(cmd, str):
                result = subprocess.run(
                    cmd, shell=True, capture_output=capture,
                    text=True, check=check, timeout=timeout, cwd=SHENKO_PATH
                )
            else:
                result = subprocess.run(
                    cmd, capture_output=capture, text=True,
                    check=check, timeout=timeout, cwd=SHENKO_PATH
                )
            
            if capture and result.stdout:
                self.logger.info(f"Output: {result.stdout.strip()}")
            if result.stderr:
                self.logger.warning(f"Stderr: {result.stderr.strip()}")
                
            return result
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Command failed: {e}")
            if e.stdout:
                self.logger.error(f"Stdout: {e.stdout}")
            if e.stderr:
                self.logger.error(f"Stderr: {e.stderr}")
            raise
        except subprocess.TimeoutExpired:
            self.logger.error(f"Command timed out after {timeout} seconds")
            raise
            
    def get_current_version(self):
        """Read current version from _version.py."""
        version_file = SHENKO_PATH / "_version.py"
        with open(version_file, 'r') as f:
            for line in f:
                if '__version__' in line:
                    version = line.split('=')[1].strip().strip('"').strip("'")
                    self.logger.info(f"Current version: {version}")
                    return version
        raise Exception("Could not find version in _version.py")
        
    def bump_version(self, version, bump_type):
        """Bump version number."""
        parts = version.split('.')
        major, minor, patch = int(parts[0]), int(parts[1]), int(parts[2])
        
        if bump_type == "major":
            major += 1
            minor = 0
            patch = 0
        elif bump_type == "minor":
            minor += 1
            patch = 0
        else:  # patch
            patch += 1
            
        new_version = f"{major}.{minor}.{patch}"
        self.logger.info(f"Bumped version: {version} → {new_version}")
        return new_version
        
    def update_version_files(self, old_version, new_version):
        """Update all version files manually."""
        self.logger.info(f"Updating version files: {old_version} → {new_version}")
        
        updates = {
            "_version.py": [
                (f'__version__ = "{old_version}"', f'__version__ = "{new_version}"')
            ],
            "shenko/__init__.py": [
                (f"__version__ = '{old_version}'", f"__version__ = '{new_version}'")
            ],
            "pyproject.toml": [
                (f'version = "{old_version}"', f'version = "{new_version}"')
            ],
            "Dockerfile": [
                (f"# version='{old_version}'", f"# version='{new_version}'")
            ],
            "snap/snapcraft.yaml": [
                (f"version: '{old_version}'", f"version: '{new_version}'")
            ],
            "setup.cfg": [
                (f"current_version = {old_version}", f"current_version = {new_version}")
            ]
        }
        
        for file_path, replacements in updates.items():
            full_path = SHENKO_PATH / file_path
            if not full_path.exists():
                self.logger.warning(f"File not found: {file_path}")
                continue
                
            with open(full_path, 'r') as f:
                content = f.read()
                
            for old, new in replacements:
                if old in content:
                    content = content.replace(old, new)
                    self.logger.info(f"Updated {file_path}")
                else:
                    self.logger.warning(f"Pattern not found in {file_path}: {old}")
                    
            with open(full_path, 'w') as f:
                f.write(content)
                
    def step_version_bump(self):
        """Step 1: Bump version."""
        print("\n" + "="*60)
        print("STEP 1: Version Bump")
        print("="*60)
        
        self.current_version = self.get_current_version()
        self.new_version = self.bump_version(self.current_version, self.bump_type)
        
        print(f"Version: {self.current_version} → {self.new_version}")
        
        # Try bumpversion first, fall back to manual if it fails
        try:
            self.run_command(["bumpversion", self.bump_type], check=False)
            self.logger.info("Bumpversion command completed")
        except:
            self.logger.warning("Bumpversion failed, updating manually")
            self.update_version_files(self.current_version, self.new_version)
            
        print("✅ Version bumped successfully")
        return True
        
    def step_commit_and_tag(self):
        """Step 2: Git commit and tag."""
        print("\n" + "="*60)
        print("STEP 2: Git Commit & Tag")
        print("="*60)
        
        self.run_command(["git", "add", "-A"])
        self.run_command([
            "git", "commit", "-m",
            f"Bump version: {self.current_version} → {self.new_version}"
        ])
        self.run_command(["git", "tag", f"v{self.new_version}"])
        
        print(f"✅ Committed and tagged v{self.new_version}")
        return True
        
    def step_build_python_packages(self):
        """Step 3: Build Python packages."""
        print("\n" + "="*60)
        print("STEP 3: Build Python Packages")
        print("="*60)
        
        # Clean old builds
        for dir in ['dist', 'build', '*.egg-info']:
            self.run_command(f"rm -rf {dir}")
            
        # Build packages
        self.run_command([sys.executable, "-m", "build"])
        
        # Verify with twine
        self.run_command(["twine", "check", "dist/*"])
        
        print("✅ Python packages built and verified")
        return True
        
    def step_push_to_github(self):
        """Step 4: Push to GitHub."""
        print("\n" + "="*60)
        print("STEP 4: Push to GitHub")
        print("="*60)
        
        self.run_command(["git", "push", "origin", "master", "--tags"])
        
        print("✅ Pushed to GitHub with tags")
        return True
        
    def step_upload_to_pypi(self):
        """Step 5: Upload to PyPI."""
        print("\n" + "="*60)
        print("STEP 5: Upload to PyPI")
        print("="*60)
        
        self.run_command(["twine", "upload", "dist/*"])
        
        print(f"✅ Uploaded to PyPI: https://pypi.org/project/shenko/{self.new_version}/")
        return True
        
    def step_docker_build_and_push(self):
        """Step 6: Build and push Docker images."""
        print("\n" + "="*60)
        print("STEP 6: Docker Build & Push")
        print("="*60)
        
        if not self.docker_username or not self.docker_password:
            print("Docker credentials not provided. Skipping Docker deployment.")
            print("(Provide credentials when running script to enable Docker deployment)")
            return True
            
        # Login to Docker Hub
        login_cmd = f"echo '{self.docker_password}' | sudo docker login -u {self.docker_username} --password-stdin"
        self.run_command(login_cmd)
        
        # Build images
        self.run_command([
            "sudo", "docker", "build",
            "-t", f"shenko/shenko.docker:{self.new_version}",
            "-t", "shenko/shenko.docker:latest",
            "."
        ])
        
        # Push images
        self.run_command(["sudo", "docker", "push", f"shenko/shenko.docker:{self.new_version}"])
        self.run_command(["sudo", "docker", "push", "shenko/shenko.docker:latest"])
        
        print(f"✅ Pushed to Docker Hub: hub.docker.com/r/shenko/shenko.docker")
        return True
        
    def step_snapcraft_build_and_push(self):
        """Step 7: Build and push Snap package."""
        print("\n" + "="*60)
        print("STEP 7: Snapcraft Build & Upload")
        print("="*60)
        
        # Check if logged in
        try:
            result = self.run_command(["snapcraft", "whoami"], check=False)
            if result.returncode != 0:
                print("⚠️  Not logged in to Snapcraft")
                print("Please run: snapcraft login")
                print("Then run this script again")
                return False
        except:
            print("⚠️  Snapcraft not available or not logged in")
            return False
            
        # Clean previous builds
        self.run_command(["snapcraft", "clean"])
        
        # Build snap
        self.run_command(["snapcraft"])
        
        # Upload to store
        snap_file = f"shenko_{self.new_version}_amd64.snap"
        self.run_command([
            "snapcraft", "upload", snap_file,
            "--release=stable"
        ])
        
        print(f"✅ Uploaded to Snapcraft Store: snapcraft.io/shenko")
        return True
        
    def generate_report(self):
        """Generate release report."""
        duration = time.time() - self.start_time
        print("\n" + "="*60)
        print("RELEASE COMPLETE!")
        print("="*60)
        print(f"Version: {self.new_version}")
        print(f"Duration: {duration:.1f} seconds")
        print()
        print("📦 Deployment Status:")
        print(f"  ✅ GitHub: https://github.com/shenko/shenko")
        print(f"  ✅ PyPI: https://pypi.org/project/shenko/{self.new_version}/")
        if self.docker_username:
            print(f"  ✅ Docker: https://hub.docker.com/r/shenko/shenko.docker")
        else:
            print(f"  ⚠️  Docker: Skipped (no credentials)")
        print(f"  📝 Snapcraft: Check status with 'snapcraft status shenko'")
        print("="*60)
        
    def run_release(self):
        """Run complete release process."""
        try:
            print("="*60)
            print("🚀 SHENKO RELEASE MANAGER")
            print("="*60)
            print(f"Bump type: {self.bump_type}")
            print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print("="*60)
            
            self.step_version_bump()
            self.step_commit_and_tag()
            self.step_build_python_packages()
            self.step_push_to_github()
            self.step_upload_to_pypi()
            self.step_docker_build_and_push()
            self.step_snapcraft_build_and_push()
            
            self.generate_report()
            return True
            
        except Exception as e:
            print(f"\n❌ Release failed: {e}")
            self.logger.error(f"Release failed: {e}")
            print(f"Check log file: {LOG_FILE}")
            return False

def main():
    """Main entry point."""
    bump_type = sys.argv[1] if len(sys.argv) > 1 else "patch"
    
    if bump_type not in ["patch", "minor", "major"]:
        print("Usage: python3 release_shenko.py [patch|minor|major]")
        sys.exit(1)
        
    manager = ShenkoReleaseManager(bump_type)
    
    # Optionally get Docker credentials
    print("\n🐳 Docker Hub Credentials (optional, press Enter to skip):")
    try:
        username = input("Username: ").strip()
        if username:
            password = getpass.getpass("Password: ")
            manager.docker_username = username
            manager.docker_password = password
    except (KeyboardInterrupt, EOFError):
        print("\nSkipping Docker credentials")
        
    success = manager.run_release()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
