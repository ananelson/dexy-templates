from dexy.template import Template

class CodeJournalHtmlPython(Template):
    """
    Template for a code journal about Python code, written in HTML.
    """
    ALIASES = ['code-journal-html-python']
    FILTERS_USED = ['jinja', 'pyg', 'pycon', 'idio']

class CodeJournalHtmlR(Template):
    """
    Template for a code journal about R code, written in HTML.
    """
    ALIASES = ['code-journal-html-r']
    FILTERS_USED = ['jinja', 'idio', 'rint', 'pyg']

class CodeJournalMarkdownMatplotlib(Template):
    """
    Template for a code journal about matplotlib/numpy code, written in markdown and converted to HTML.
    """
    ALIASES = ['code-journal-markdown-matplotlib']
    FILTERS_USED = ['markdown', 'idio', 'jinja', 'pycon', 'pyg']

class CodeJournalMarkdownR(Template):
    """
    Template for a code journal about R code, written in markdown and converted to HTML.
    """
    ALIASES = ['code-journal-markdown-r']
    FILTERS_USED = ['rint', 'markdown', 'idio', 'jinja', 'pyg']

class CodeJournalTextileRuby(Template):
    """
    Template for a code journal about Ruby code, written in textile and converted to HTML.
    """
    ALIASES = ['code-journal-textile-ruby']
    FILTERS_USED = ['textile', 'pyg']

class LatexArticlePython(Template):
    """
    Template for an article about Python code written in LaTeX and rendered as PDF.
    """
    ALIASES = ['latex-article-python']
    FILTERS_USED = ['latex', 'ft', 'jinja', 'l', 'pycon', 'idio', 'hd', 'pyg']

class LatexArticleR(Template):
    """
    Template for an article about R code written in LaTeX and rendered as PDF.
    """
    ALIASES = ['latex-article-r']
    FILTERS_USED = ['latex', 'r', 'jinja', 'idio', 'l', 'pyg']

class LatexBeamerR(Template):
    """
    Template for an article about R code written in LaTeX Beamer and rendered as PDF.
    """
    ALIASES = ['latex-beamer-r']
    FILTERS_USED = ['latex', 'r', 'jinja', 'idio', 'l', 'pyg']

class LatexBookR(Template):
    """
    Template for a book about R code written in LaTeX Beamer and rendered as PDF.
    """
    ALIASES = ['latex-book-r']
    FILTERS_USED = ['latex', 'jinja', 'l', 'r', 'idio', 'pyg']

class LatexChaptersInclude(Template):
    """
    Template for a book where chapters are included using jinja.
    """
    ALIASES = ['latex-chapters-include']
    FILTERS_USED = ['latex', 'rst2html', 'rst2latex', 'jinja']

class LatexTufteArticleR(Template):
    """
    Article using Tufte LaTeX template.
    """
    ALIASES = ['latex-tufte-article-r']
    FILTERS_USED = ['latex', 'ft', 'jinja', 'l', 'r', 'idio', 'hd', 'pyg']

class Pander(Template):
    """
    Examples using pander (http://rapporter.github.com/pander) to generate markdown output from R and pandoc to render in multiple formats.
    """
    ALIASES = [ 'pander']
    FILTERS_USED = ['pandoc', 'jinja', 'rout', 'calibre']

class Html5Website(Template):
    """
    Template for creating a website using dexy's WebsiteReporter. (based on http://html5templates.com/altitude/)
    """
    ALIASES = ['website-html5-altitude']
    FILTERS_USED = ['jinja', 'markdown', 'shint', 'idio', 'pyg', 'htmlsections']
