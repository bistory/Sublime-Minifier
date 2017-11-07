# A Javascript and CSS Minifier for Sublime Text 2 & 3

The plugin supports [Google Closure Compiler](https://developers.google.com/closure/compiler/) for Javascript minification and [cssminifier](https://www.cssminifier.com/) or [Reducisaurus](http://code.google.com/p/reducisaurus/) for CSS minification.

This module was forked from [JsMinifier](https://github.com/cgutierrez/JsMinifier).

Usage
-----

__Windows__ / __Linux__ default key binding:    
`ctrl + alt + m` - attempts to minify the current buffer and replaces the buffers content    
`ctrl + alt + shift + m` - attempts to minify the current buffer and saves the output to a separate file.

__MacOSX__ default key binding:    
`⌘ + alt + m` - attempts to minify the current buffer and replaces the buffers content    
`⌘ + alt + shift + m` - attempts to minify the current buffer and saves the output to a separate file.


Installation
------------

**With the Package Control plugin:** The easiest way to install SublimeCodeIntel is through Package Control, which can be found at this site: https://packagecontrol.io/installation

Once you install Package Control, restart Sublime Text and bring up the Command Palette (``Command+Shift+P`` on OS X, ``Control+Shift+P`` on Linux/Windows). Select "Package Control: Install Package", wait while Package Control fetches the latest package list, then select Minifier when the list appears. The advantage of using this method is that Package Control will automatically keep Minifier up to date with the latest version.

**Without Git:** Download the latest source from [GitHub](https://github.com/bistory/Sublime-Minifier) and copy the whole directory into the Packages directory. Make sure folder name is "Minifier".

**With Git:** Clone the repository in your Sublime Text 2 or 3 Packages directory, located somewhere in user's "Home" directory:

    `git clone git://github.com/bistory/Sublime-Minifier.git`


The "Packages" packages directory is located at:

* OS X:

ST2 :
    `~/Library/Application Support/Sublime Text 2/Packages/`

ST3:
    `~/Library/Application Support/Sublime Text 3/Packages/`

* Linux:

ST2 :
    `~/.Sublime Text 2/Packages/`

ST3 :
    `~/.Sublime Text 3/Packages/`

* Windows:

ST2 :
    `%APPDATA%/Sublime Text 2/Packages/`

ST3 :
    `%APPDATA%/Sublime Text 3/Packages/`