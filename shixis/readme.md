# 一、	项目背景
笔者在武汉上学，想找一份数据分析的实习，但武汉的数据分析实习岗位很少，学生很多，僧多肉少的情况下，必须准确把控招聘方的需求，看重的技能，着重去学习。在武汉实习岗位少的情况下，分析外地的数据分析实习时间要求，考虑去外地实习的可行性。
# 二、	项目简介
# 三、	数据来源和数据集
www.shixiseng.com
# 四、	技术和工具
Python、SPSS
# 五、	数据整理
数据清洗
原始数据

![image](https://github.com/chancechang/pythonProject/raw/master/shixis/image/crawldata.png)

1、	搜索数据分析得到的记录中有招聘助理这样的职位，被筛选出来的原因是类型中包含数据分析四个字，这样的记录是不符合要求的，我们要保证职位名称包含数据分析四个字，直接用Excel查找出岗位名称中包含数据和分析的，将不包含的删除掉。

2、	日薪中含有/天，我们要将薪水转化成int型，取出最大值，最小值，平均值。首先要将字符串拆分

3、	每周最少工作天数的单位都是天/周，我们提取出重要信息，也就是天数，转化成int型。

4、	最短工作月数的单位是个月，我们提取出重要信息，也就是月份数目，转化成int型。

5、	将职位描述提取出关键字，以便于分析需要的技能的重要程度。

6、	还存在地区名字为多个的，如下图所示，我们将地区分开，变成多条数据。

![image](https://github.com/chancechang/pythonProject/raw/master/shixis/image/2.png)

7、	去掉链接

8、	导入SPSS时，以逗号分隔，因此去掉文件中所有的逗号，以免对导入结果造成影响
数据清洗后得到的数据如下：
![image](https://github.com/chancechang/pythonProject/raw/master/shixis/image/3.png)
# 六、	数据分析
### 最短工作月数分布
![image](https://github.com/chancechang/pythonProject/raw/master/shixis/image/4.png)
### 不同地区的实习岗位数量
 ![image](https://github.com/chancechang/pythonProject/raw/master/shixis/image/5.png)
### 每周最少工作天数
 ![image](https://github.com/chancechang/pythonProject/raw/master/shixis/image/6.png)


### 日薪最小值
 ![image](https://github.com/chancechang/pythonProject/raw/master/shixis/image/7.png)
### 日薪均值
 ![image](https://github.com/chancechang/pythonProject/raw/master/shixis/image/8.png)
### 日薪最大值
 
![image](https://github.com/chancechang/pythonProject/raw/master/shixis/image/9.png)







### 要求
 ![image](https://github.com/chancechang/pythonProject/raw/master/shixis/image/10.png)
数据分析岗位大都要求excel、python、sql技能，掌握这三种工具是必要的
