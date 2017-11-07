import sublime

if sublime.version() < '3':
    from googleclosurecall import GoogleClosureCall
    from uglifycall import UglifyCall
    from reducisauruscall import ReducisaurusCall
    from cssminifiercall import CssminifierCall
else:
    from Minifier.compilers.googleclosurecall import GoogleClosureCall
    from Minifier.compilers.uglifycall import UglifyCall
    from Minifier.compilers.reducisauruscall import ReducisaurusCall
    from Minifier.compilers.cssminifiercall import CssminifierCall