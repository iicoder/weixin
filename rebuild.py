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
        content = f.read().decode('utf-8').strip()
        if not content.startswith('---'):
            exce = 'this file format error {}'.format(article)
            raise Exception(exce)

        sk = content.find('---')
        ek = content.find('---',sk+3)
        info = yaml.load(content[sk+3:ek].strip())

        #load names
        article = article.decode('utf-8')
        namelst = article.split('.')

        meta = {}

        meta['id'] = namelst.pop(0)
        meta['type'] = namelst.pop(0)
        if article.endswith('.raw.md'):
            meta['tranraw'] =  True
            namelst.pop()
        meta['title'] = '.'.join(namelst)

        #rename
        meta['author'] = info[u'原作者']
        meta['link'] = info[u'来源']
        meta['file'] = article

        return meta


def render(fname,home,**kwargs):
    fin = os.path.join(home,path_template,fname)
    fout = os.path.join(home,fname)

    with open(fin,'r') as f:
        content = f.read().decode('utf-8')
        template = Template(content)
        out = template.render(**kwargs)
    with open(fout,'w') as f:
        f.write(out.encode('utf-8'))


def main(home):
    #load metas
    reposts = []
    tranlist = []
    for fname in os.listdir(home):
        fid = fname.split('.',1)[0]
        if not fid.isdigit():
            continue
        meta = load_meta(fname,home)
        if meta['type'] == 'tran':
            if not meta.get('tranraw'):
                tranlist.append(meta)
        elif meta['type'] == 'repost':
            reposts.append(meta)

    renderfile = 'LIST.md'
    render(renderfile,home,reposts=reposts,tranlist=tranlist)


if __name__ == '__main__':
    home = os.path.dirname(os.path.abspath(__file__))
    main(home)