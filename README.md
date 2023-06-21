# 工具介绍
语雀导出的markdown格式的文档，无法利用hexo，或csdn对其渲染，因为语雀含有防盗链机制，导致图片无法加载。
该脚本将会收集语雀中markdown中的图片链接，自动下载到脚本的同级目录的images目录下，并生成新的test.md文档，替换掉原有的图片链接。

注意:替换图片链接的功能，需要自己将下载后的图片上传至指定图传，或者自己的WEB服务器上，并且文件名称不要改变。
注意:脚本使用时，需要将同目录的readme.md文件删除，否则readme.md会影响文档输出

# 工具效果
1.执行脚本文件，注意时python3版本，输入新的图片网络路径，注意后面要加/
[![pCGyPNF.png](https://s1.ax1x.com/2023/06/21/pCGyPNF.png)](https://imgse.com/i/pCGyPNF)<br>
2.如下所示，生成images目录，里面含有下载的图片
[![pCGyCAU.png](https://s1.ax1x.com/2023/06/21/pCGyCAU.png)](https://imgse.com/i/pCGyCAU)<br>
3.比较test.md文档和原始文档，可以发现图片链接已经自动改变
[![pCGyih4.png](https://s1.ax1x.com/2023/06/21/pCGyih4.png)](https://imgse.com/i/pCGyih4)<br>
