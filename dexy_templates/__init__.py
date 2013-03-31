from dexy.template import Template

class WebpyWebapp(Template):
    """
    An example web app written using web.py, documented using dexy.
    """
    aliases = ['webpy-webapp']
    filters_used = []
    def is_active(self):
        return False

class CodeJournalHtmlPython(Template):
    """
    Template for a code journal about Python code, written in HTML.
    """
    aliases = ['code-journal-html-python']
    filters_used = ['jinja', 'pyg', 'pycon', 'idio']

class CodeJournalHtmlR(Template):
    """
    Template for a code journal about R code, written in HTML.
    """
    aliases = ['code-journal-html-r']
    filters_used = ['jinja', 'idio', 'rint', 'pyg']

class CodeJournalMarkdownMatplotlib(Template):
    """
    Template for a code journal about matplotlib/numpy code, written in markdown and converted to HTML.
    """
    aliases = ['code-journal-markdown-matplotlib']
    filters_used = ['markdown', 'idio', 'jinja', 'pycon', 'pyg']

class CodeJournalMarkdownR(Template):
    """
    Template for a code journal about R code, written in markdown and converted to HTML.
    """
    aliases = ['code-journal-markdown-r']
    filters_used = ['rint', 'markdown', 'idio', 'jinja', 'pyg']

class CodeJournalTextileRuby(Template):
    """
    Template for a code journal about Ruby code, written in textile and converted to HTML.
    """
    aliases = ['code-journal-textile-ruby']
    filters_used = ['textile', 'pyg', 'rb', 'jinja', 'easyhtml']

class LatexArticlePython(Template):
    """
    Template for an article about Python code written in LaTeX and rendered as PDF.
    """
    aliases = ['latex-article-python']
    filters_used = ['latex', 'ft', 'jinja', 'l', 'pycon', 'idio', 'hd', 'pyg']

class LatexArticleR(Template):
    """
    Template for an article about R code written in LaTeX and rendered as PDF.
    """
    aliases = ['latex-article-r']
    filters_used = ['latex', 'r', 'jinja', 'idio', 'l', 'pyg', 'hd', 'ft']

class LatexBeamerR(Template):
    """
    Template for an article about R code written in LaTeX Beamer and rendered as PDF.
    """
    aliases = ['latex-beamer-r']
    filters_used = ['latex', 'r', 'jinja', 'idio', 'l', 'pyg']

class LatexBookR(Template):
    """
    Template for a book about R code written in LaTeX Beamer and rendered as PDF.
    """
    aliases = ['latex-book-r']
    filters_used = ['latex', 'jinja', 'l', 'r', 'idio', 'pyg']

class LatexChaptersInclude(Template):
    """
    Template for a book where chapters are included using jinja.
    """
    aliases = ['latex-chapters-include']
    filters_used = ['latex', 'rst2html', 'rst2latex', 'jinja']

class LatexTufteArticleR(Template):
    """
    Article using Tufte LaTeX template.
    """
    aliases = ['latex-tufte-article-r']
    filters_used = ['latex', 'ft', 'jinja', 'l', 'r', 'idio', 'hd', 'pyg']

class Pander(Template):
    """
    Examples using pander (http://rapporter.github.com/pander) to generate markdown output from R and pandoc to render in multiple formats.
    """
    aliases = [ 'pander']
    filters_used = ['pandoc', 'jinja', 'rout', 'calibre']

class Html5Website(Template):
    """
    Template for creating a website using dexy's WebsiteReporter. (based on http://html5templates.com/altitude/)
    """
    aliases = ['website-html5-altitude']
    filters_used = ['jinja', 'markdown', 'shint', 'idio', 'pyg', 'htmlsections']

class SimpleWebsite(Template):
    """
    Template for creating a very simple website using dexy's WebsiteReporter.
    """
    aliases = ['website-simple']
    filters_used = ['jinja', 'rstbody']
