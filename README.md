# noopy.dev

[![Blog Badge](http://img.shields.io/badge/DevBlog-blueviolet?style=flat-square&logo=gatsby&link=https://noopy.dev/)](https://noopy.dev/)

snoop2head writing about how to build things

## Guide for Installation

```shell
git clone https://github.com/snoop2head/noopy
cd noopy
npm install
gatsby build
npm start
```

## Guide for Customization

* [gatsby-meta-config.js](./gatsby-meta-config.js): blog meta data such as title, keywords etc.
* [contents](./contents)
  * [__about](./contents/about): writing about portfolio
  * [assets](./contents/assets): profile image and felog image above it
  * [blog](./contents/blog): blog writings in Markdown file format

## Moving Images After Writing

Placing image with Typora editor creates image on the corresponding directory. Use python3 to 1) move the img files into each categories' images folder and 2) rewrite their paths notated on the markdown document.

```python
python3 app.py
```

## Gatsby Template Reference

* [gatsby-starter-bee](https://github.com/JaeYeopHan/gatsby-starter-bee)
* [SOSO log](https://github.com/SoYoung210/SOSO)

