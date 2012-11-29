from dexy.template import Template

class Pander(Template):
    """
    Examples using pander (http://rapporter.github.com/pander) to generate markdown output from R and pandoc to render in multiple formats.
    """
    ALIASES = [ 'pander']

class Html5Website(Template):
    """
    Template for creating a website using dexy's WebsiteReporter. (based on http://html5templates.com/altitude/)
    """
    ALIASES = ['website-html5-altitude']

class CodeJournalHtmlPython(Template):
    """
    Template for a code journal about Python code, written in HTML.
    """
    ALIASES = ['code-journal-html-python']

class CodeJournalHtmlR(Template):
    """
    Template for a code journal about R code, written in HTML.
    """
    ALIASES = ['code-journal-html-r']

class CodeJournalMarkdownMatplotlib(Template):
    """
    Template for a code journal about matplotlib/numpy code, written in markdown and converted to HTML.
    """
    ALIASES = ['code-journal-markdown-matplotlib']
