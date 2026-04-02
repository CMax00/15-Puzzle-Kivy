[app]

# App title (shown on phone)
title = 15 Puzzle

# Package name (must be unique, only lowercase letters and numbers, no underscores!)
package.name = puzzle15

# Package domain (you can change "deinname" to your name or company)
package.domain = org.deinname

# Directory where your source code is located
source.dir = .

# File types that should be included in the APK
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,woff

# Version of your app
version = 0.1

# Required dependencies
requirements = python3,kivy==2.3.1

# Screen orientation
orientation = portrait

# Fullscreen mode (0 = show status bar, 1 = real fullscreen)
fullscreen = 0

# Android permissions
android.permissions = INTERNET,VIBRATE

# Android API levels
android.api = 33
android.minapi = 21

# Optional: App icon and splash screen (uncomment when you add the files)
# icon.filename = icon.png
# presplash.filename = presplash.png

# Optional: Enable GPU (can improve performance on some devices)
# android.enable_gpu = True
