# 汇聚的文章列表
 目前分两类

 一类转载，目前共有{{reposts|length}} 篇

 另一个就是翻译的啦，现在是{{tranlist|length}} 篇

## 翻译列表
{% for tran in tranlist %}
- [{{tran.title}}](./{{tran.file}}) - {{tran.author}} － [原文链接]({{tran.link}})
{% endfor %}

## 转载列表
{% for post in reposts %}
- [{{post.title}}](./{{post.file}}) - {{post.author}} － [原文链接]({{post.link}})
{% endfor %}
