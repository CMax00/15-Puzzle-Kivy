[app]

android.accept_sdk_license = True

title = 15 Puzzle
package.name = puzzle15
package.domain = org.deinname

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,woff

version = 0.1

# Wichtig für aktuellen Build
requirements = python3,kivy==2.3.1,cython==0.29.37

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,VIBRATE
android.api = 33
android.minapi = 21
