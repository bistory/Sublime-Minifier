# A Javascript and CSS Minifier for Sublime Text 2

The plugin supports the [Google Closure Compiler](https://developers.google.com/closure/compiler/) and [UglifyJS](https://github.com/mishoo/UglifyJS) compilers for Javascript minification and [cssminifier](http://www.cssminifier.com/) and [Reducisaurus](http://code.google.com/p/reducisaurus/) for CSS minification.

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
<!---
**With the Package Control plugin:** The easiest way to install SublimeCodeIntel is through Package Control, which can be found at this site: http://wbond.net/sublime_packages/package_control

Once you install Package Control, restart Sublime Text 2 and bring up the Command Palette (``Command+Shift+P`` on OS X, ``Control+Shift+P`` on Linux/Windows). Select "Package Control: Install Package", wait while Package Control fetches the latest package list, then select SublimeCodeIntel when the list appears. The advantage of using this method is that Package Control will automatically keep SublimeCodeIntel up to date with the latest version.
-->

**Without Git:** Download the latest source from [GitHub](https://github.com/bistory/Sublime-Minifier) and copy the whole directory into the Packages directory. Make sure folder name is "Minifier".

**With Git:** Clone the repository in your Sublime Text 2 Packages directory, located somewhere in user's "Home" directory:

    `git clone git://github.com/bistory/Sublime-Minifier.git`


The "Packages" packages directory is located at:

* OS X:

    `~/Library/Application Support/Sublime Text 2/Packages/`

* Linux:

    `~/.Sublime Text 2/Packages/`

* Windows:

    `%APPDATA%/Sublime Text 2/Packages/`