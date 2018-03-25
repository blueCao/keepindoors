# [足不出户 知天下](https://github.com/blueCao/keepindoors)

## 前期准备

### 1.目标
- 对信息源进行分析（例如：分词、聚类分析、语义分析等等），选出符合条件信息（例如：热点信息）

### 2.工具
- hadoop存储（hive）
- spark大规模数据集测试
- python小规模数据训练测试

### 3.所用开源框架
- [HanLP中文分词（Java only）](https://github.com/hankcs/HanLP)
- [Jieba中文分词（Python only）](https://github.com/fxsjy/jieba)

### 4 hive（数据存储）
#### 4.1 数据源
- 抓取的本地文件利用[avro工具](http://avro.apache.org/)存储成avro格式
```
 avro格式的数据优势
- Rich data structures.
- A compact, fast, binary data format.
- A container file, to store persistent data.
- Remote procedure call (RPC).
- Simple integration with dynamic languages. Code generation is not required to read or write data files nor to use or implement RPC protocols. Code generation as an optional optimization, only worth implementing for statically typed languages.
```
#### 4.2 hdfs
- 将外部的avro文件导入到hdfs中，采用snappy压缩。  
[hive中使用snappy压缩avro参考链接](http://blog.itpub.net/31347383/viewspace-2123733/)
```
使用snappy压缩依据：（压缩比低、但是压缩和压缩的速度很快，是一种空间和速度tradeoff的方式）



Algorithm	% remaining	Encoding	Decoding
GZIP	13.4%	21 MB/s	118 MB/s
LZO	20.5%	135 MB/s	410 MB/s
Zippy/Snappy	22.2%	172 MB/s	409 MB/s
 

其中：

1）GZIP的压缩率最高，但是其实CPU密集型的，对CPU的消耗比其他算法要多，压缩和解压速度也慢；

2）LZO的压缩率居中，比GZIP要低一些，但是压缩和解压速度明显要比GZIP快很多，其中解压速度快的更多；

3）Zippy/Snappy的压缩率最低，而压缩和解压速度要稍微比LZO要快一些。
```

#### 4.4 hive中目录划分
- 托管表：hdfs://user/hive/warehouse/keepindoors/xxx_table

- 分区：按照日期格式 yyyy-mm-dd 作为划分的依据
```

```
- 桶：按照内容来源（如:tencent、zhihu、zhihu等等）进行划分
```
使用桶划分需要将 hive.enforce.bucketing 属性设置为true
```

### [5.pyspider的使用(实时新闻数据抓取)](https://github.com/blueCao/pyspider)
#### 5.1任务
- 任务id
- 任务状态
- 任务优先级
```
一个任务有唯一的任务ID叫taskid(默认是：md5(url),不过可以重写get_taskid(self,task)方法指定自己项目生成taskid方法。)
不同项目之间任务不冲突。
任务的四个状态:
active（运行）
failed（失败）
success（成功）
bad - （暂时没用着）
只有当任务状态为运行（active）时才会被调度。
根据优先级执行任务．
```

#### 5.2调度

- 调度优先级
```
@config(priority=2) 优先级越大越先执行（默认优先级为0，最小）
```
- 调度频率
```
@every(minutes=24*60, seconds=0) 这个设置是告诉scheduler（调度器）on_start方法每天执行一次。
```
- 有效期
```
@config(age=10 * 24 * 60 * 60) 这个设置告诉scheduler（调度器）这个request（请求）过期时间是10天，10天内再遇到这个请求直接忽略。这个参数也可以在self.crawl(url, age=10*24*60*60) 和 crawl_config中设置。
```


------

## 数据处理
### [9.搜狗实验室12年6月7月全完新闻数据集](http://www.sogou.com/labs/resource/ca.php)
#### 9.1 原始数据
```
格式说明：

数据格式为

<doc>

<url>页面URL</url>

<docno>页面ID</docno>

<contenttitle>页面标题</contenttitle>

<content>页面内容</content>

</doc>
注意：content字段去除了HTML标签，保存的是新闻正文文本



数据量：（150万条左右）
1,500,000
```
#### 9.2 数据预处理
> 根据原始数据解析成DOM根式，根据url中的日期信息，解析出对应的日期。例如：http://news.sohu.com/20120607/n344998325.shtml 需要解析出日期中日期信息，剔除不带日期的数据。并按照时间顺序排序。
```
格式说明：

数据格式为

<doc>

<url>页面URL</url>

<docno>页面ID</docno>

<contenttitle>页面标题</contenttitle>

<content>页面内容</content>

<date>20160612</date>

</doc>


```