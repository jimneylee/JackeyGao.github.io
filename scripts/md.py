# -*- coding: utf-8 -*-
'''
File Name: markdown.py
Author: JackeyGao
mail: gaojunqi@outlook.com
Created Time: 五  8/12 09:59:17 2016
'''
import sys, re
import misaka as m
from hashlib import md5
from misaka import escape_html
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from pygments.util import ClassNotFound

import six

if six.PY2:
    reload(sys)
    sys.setdefaultencoding('utf-8')

cleanr =re.compile('<.*?>')


class HighlighterRenderer(m.HtmlRenderer):
    def link(self, content, link, title=''):
        if not hasattr(self, 'links'):
            self.links = []

        link_item = [content, link, title]
        
        if title:
            if link_item not in self.links:
                self.links.append(link_item) 
            index = self.links.index(link_item) + 1
            return '<a href="%s" title="%s">%s</a> <sup>[%s]</sup>' % (link, title, content.strip(), index)
        else:
            return '<a href="%s">%s</a>' % (link, content.strip())

    def header(self, content, level):
        return '<h{0} id="{1}">{1}</h{0}>'.format(level, content)

    def blockcode(self, text, lang):
        _id = md5(text.encode()).hexdigest()
        _id = "code%s" % str(_id)

        if ':' in lang:
            lang, title = lang.split(':')
        else:
            lang, title = lang, ''

        langDiv = '<figcaption><a href="#%s" class="lang-label"><\>text</a></figcaption>'% (_id)

        if title:
            titleDiv = '<span class="title-label">#%s</span>' % title
        else:
            titleDiv = ''

        if not lang:
            return '''<figcaption id="%s" class="code-wrapper">''' % (_id) + \
        '''\n<div class="highlight"><pre>''' +  text.strip() + '''</pre>''' + titleDiv + langDiv + '''</div></figcaption>\n''' 

        try:
            lexer = get_lexer_by_name(lang, stripall=True)
            language = lang
        except ClassNotFound:
            lexer = get_lexer_by_name('text', stripall=True)
            language = lang
            
        formatter = HtmlFormatter()
        text = text.encode('utf-8')
        content = highlight(text, lexer, formatter)
            
        langDiv = '<figcaption><a class="lang-label" href="#{0}"><\>'.format(_id) + language.title() + '</a></figcaption>'
        return '<figure id="%s" class="code-wrapper">' % (_id) + content + titleDiv + langDiv + '</figure>' 


    def blockquote(self, content):
        _real = re.sub(cleanr,'', content).strip()
        if _real.startswith('%center\n'):
            content = content.replace('%center', '')
            className = "blockquote-center song"
        elif _real.startswith('%valign\n'):
            content = content.replace('%valign', '')
            className = "blockquote-valign song"
        elif _real.startswith('%warning'):
            content = content.replace('%warning', '')
            className = "blockquote-warning"
        elif _real.startswith('%error'):
            content = content.replace('%error', '')
            className = "blockquote-error"
        else:
            content = content
            className = "blockquote-normal"
        
        content = content.strip()
        content = content.replace('\n', '<br/>')
        content = content.replace('</p><br/>', '</p>')
        content = content.replace('<p><br/>', '<p>')

        # content = content.strip('<br/>')

        return '''<blockquote class="%s">
                %s</blockquote>''' % (className, content)

    def image(self, link, title="", alt=''):
        #link = link.replace('/uploads', 'https://o8uou7r4o.qnssl.com')

        if 'cover' in title:
            self.cover = link

        if 'border' in title:
            css_class = "hassubimage border"
        else:
            css_class = "hassubimage"

        if 'radius' in title:
            css_class += ' radius'

        if 'padding' in title:
            css_class += ' padding'

        if 'overflow' in title:
            css_class += ' overflow'

        if alt == 'hidden':
            css_class += ' hidden'

        html = '<figure class="%s">' % css_class

        html += '<div class="image"><img src="%s"></div>' % (link)

        if alt:
            html +=  '''<figcaption class="img-title">#%s</figcaption>''' % (alt)

        html += '</figure>'
        print(html)
        return html

    def table(self, content):
        return '<div class="code table-wrapper"><table>'\
                + content + '</table></div>'


#toc = m.Markdown(m.HtmlTocRenderer())

def new_markdown():
    markdown = m.Markdown(
        HighlighterRenderer(),
        extensions=\
        m.EXT_FENCED_CODE |\
        m.EXT_TABLES |\
        m.EXT_QUOTE
    )
    return markdown
    

def markrender(content):
    markdown = new_markdown()
    md = markdown(content)
    print(dir(markdown))
    return md

if __name__ == '__main__':
    content = open('markdown/responder-chat-room.md').read()

    content = '---'.join(content.split('---')[1:]).strip().strip('\n')

    md = markrender(content)

    print(md)

    #print(markdown.renderer)

    #print(getattr(markdown.renderer, 'links', None))
    
