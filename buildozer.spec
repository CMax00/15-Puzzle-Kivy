[app]

title = 15 Puzzle
package.name = puzzle15
package.domain = org.cmax

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,woff

version = 0.1

# Wichtig: cython explizit hinzufügen
requirements = python3,kivy==2.3.1,cython

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,VIBRATE
android.api = 33
android.minapi = 21
