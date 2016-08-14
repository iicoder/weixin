#coding=utf-8
#2016.08.14

from jinja2 import Template
import yaml
import os

path_template = '_template'


def load_meta(article,home):
    fpath = os.path.join(home,article)

    with open(fpath,'r') as f:
        #load yaml meta
        content = f.read().strip()        
        if not content.startswith('---'):
            exce = 'this file format error {}'.format(article)
            raise Exception(exce)
        sk = content.find('---')
        ek = content.find('---',sk+3)
        meta = yaml.load(content[sk+3:ek].strip())

        #load names
        namelst = article.split('.')
        meta['id'] = namelst.pop(0)
        meta['title'] = namelst.pop(0)
        if article.endswith('.raw.md'):
            meta['tranraw'] =  True
            namelst.pop()
        meta['title'] = '.'.join(namelst)

        #rename
        meta['author'] = meta[u'原作者']
        meta['link'] = meta[u'来源']
        meta['file'] = article

        return meta


def render(fname,home,**kwargs):
    fin = os.path.join(home,path_template,fname)
    fout = os.path.join(home,fname)

    with open(fins,'r') as f:
        template = Template(f.read())    
        out = template.render(**kwargs)
    with open(fout,'w') as f:
        f.write(out)


def main(home):
    pass
    
    


if __name__ == '__main__':
    home = os.path.dirname(os.path.abspath(__file__))
    main(home)