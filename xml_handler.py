#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
class for decode the xml news date file

INPUT  xml date file form：
-----------------------------------------------------------------------------------------------------------------------
<html>
 <head></head>
 <body>
  <doc>
   <url>
    http://news.sohu.com/20120612/n345428229.shtml
   </url>
   <docno>
    c172394d49da2142-69713306c0bb3300
   </docno>
   <contenttitle>
    公安机关销毁１０余万非法枪支　跨国武器走私渐起
   </contenttitle>
   <content>
    中广网唐山６月１２日消息（记者汤一亮　庄胜春）据中国之声《新闻晚高峰》报道，今天（１２日）上午，公安机关２０１２年缉枪制爆专项行动“统一销毁非法枪爆物品活动”在河北唐山正式启动，１０万余只非法枪支、２５０余吨炸药在全国１５０个城市被统一销毁。黄明：现在我宣布，全国缉枪制爆统一销毁行动开始！随着公安部副部长黄明一声令下，大量仿制式枪以及猎枪、火药枪、气枪在河北唐山钢铁厂被投入炼钢炉。与此同时，在全国各省区市１５０个城市，破案追缴和群众主动上缴的１０万余支非法枪支被集中销毁，在全国各指定场所，２５０余吨炸药被分别销毁。公安部治安局局长刘绍武介绍，这次销毁的非法枪支来源于三个方面。刘绍武：打击破案包括涉黑、涉恶的团伙犯罪、毒品犯罪，还有从境外非法走私的枪支爆炸物。在销毁现场，记者看到了被追缴和上缴的各式各样的枪支。刘绍武：也包括制式枪，有的是军用枪、仿制的制式抢，还有猎枪、私制的火药枪等等。按照我国的枪支管理法，这些都是严厉禁止个人非法持有的。中国是世界上持枪犯罪的犯罪率最低的国家之一。中美联手破获特大跨国走私武器弹药案近日，中美执法部门联手成功破获特大跨国走私武器弹药案，在中国抓获犯罪嫌疑人２３名，缴获各类枪支９３支、子弹５万余发及大量枪支配件。在美国抓获犯罪嫌疑人３名，缴获各类枪支１２支。这是公安部与美国移民海关执法局通过联合调查方式侦破重大跨国案件的又一成功案例。２０１１年８月２５日，上海浦东国际机场海关在对美国纽约发往浙江台州，申报品名为扩音器（音箱）的快件进行查验时，发现货物内藏有手枪９支，枪支配件９件，长枪部件７件。经检验，这些都是具有杀伤力的制式枪支及其配件。这引起了公安部和海关总署的高度重视。公安部刑侦局局长刘安成：因为是从海关进口的货物中检查出来夹带，说明来源地是境外，或是说国外，这应该是一起特大跨国走私武器弹药的案件。上海市公安局和上海海关缉私局成立联合专案组，迅速开展案件侦查。专案组于８月２６日在浙江台州ＵＰＳ取件处将犯罪嫌疑人王挺（男，３２岁，台州市人）抓获。王挺交代，他通过一境外网站上认识了上家林志富，２００９年１１月以来，林志富长期居住美国，他通过互联网组建了一个走私、贩卖、私藏枪支弹药的群体，通过网络在国内寻找枪支弹药买家，并通过美国ＵＰＳ联邦速递公司将枪支弹药从纽约快递给多名类似王挺的中间人，再通过中间人发送给国内买家。此案中，犯罪分子依托虚拟网络进行犯罪交易，隐蔽性强，涉案人员使用的身份、地址、联系方式都是虚构的，侦查难度很大。刘安成说，此案体现了是新型犯罪，特别是现代犯罪的新特点。刘安成：他不受距离的限制、经常是跨国跨境，甚至是跨一个、数个、甚至数十个国家。这种犯罪手法的改变和新型犯罪的特点，要求我们各国警方充分合作。作者：汤一亮　庄胜春
   </content>
  </doc>
  <doc>
   <url>
    http://news.sohu.com/20120607/n344998325.shtml
   </url>
   <docno>
    dbb4554e49da2142-69713306c0bb3300
   </docno>
   <contenttitle>
    张绍刚发道歉信网友不认可：他的问题是俯视他人（图）
   </contenttitle>
   <content>
    天津卫视求职节目《非你莫属》“晕倒门”事件余波未了，主持人张绍刚前日通过《非你莫属》节目组发出道歉信，称自己错在对留学生缺乏了解。但他的道歉，没有得到网友的接受和原谅，有网友尖锐指出，张绍刚的问题就在俯视他人，连道歉都不会。张绍刚：我是一番好意之前哪怕被网友骂得再凶，张绍刚也表现彪悍，声称自己没错，绝不道歉。但这几天李开复领衔讨伐节目组，网上民意汹汹要他“下课”，张绍刚显然有点撑不住。前日他通过《非你莫属》节目组，发出一则语焉不详的道歉信。信中他将自己在节目中的表现，解释为一番好意，就像几年前程鹤麟先生说他的，“追在别人屁股后面，碎嘴叨叨地说＂你得这样，这是为了你好＂，而自己的错误，在于对求职者不够了解，没有站在别人的角度考虑问题，“当不了解一个群体的时候，就无法给出准确的判断和建议，今年以来的各种沸沸扬扬，大多源自于此。”他最后表示：“留学生的批评我很感谢，我会努力去了解这个群体的所思所想。有问题的，认识、纠正，这是咱们经常跟同学们说的，今天我对自己说！”网友：别再硬挺下去张绍刚的这番道歉，却没有得到网友的认可。有网友尖锐指出，张绍刚的问题在于俯视他人，连道歉都不会：“张绍刚要么在讲台，要么在舞台，对学生、对选手都掌握生杀大权，高高在上惯了，很难做到平视。他的问题不在于对哪个群体是否了解，而是他的态度。”更有网友认为，张绍刚存在自卑感，“在所有的海归学生访谈的时候，他对于相关外文的资料，先以＂我看不懂＂推脱；当学生提及在当地生活经验的时候，他就在对方的用字里面挑刺；然后吆喝批判学生数典忘祖，不爱祖国”。有网友劝张绍刚：“张先生，请先把自卑处理，再当主持人。”“别再硬挺了，再挺下去就真成棒槌了。”（余乐）作者：余乐　（来源：羊城晚报）
   </content>
  </doc>
 </body>
</html>
-----------------------------------------------------------------------------------------------------------------------
INPUT date file form：
-----------------------------------------------------------------------------------------------------------------------
<html>
 <head></head>
 <body>
  <doc>
   <url>
    http://news.sohu.com/20120612/n345428229.shtml
   </url>
   <docno>
    c172394d49da2142-69713306c0bb3300
   </docno>
   <contenttitle>
    公安机关销毁１０余万非法枪支　跨国武器走私渐起
   </contenttitle>
   <content>
    中广网唐山６月１２日消息（记者汤一亮　庄胜春）据中国之声《新闻晚高峰》报道，今天（１２日）上午，公安机关２０１２年缉枪制爆专项行动“统一销毁非法枪爆物品活动”在河北唐山正式启动，１０万余只非法枪支、２５０余吨炸药在全国１５０个城市被统一销毁。黄明：现在我宣布，全国缉枪制爆统一销毁行动开始！随着公安部副部长黄明一声令下，大量仿制式枪以及猎枪、火药枪、气枪在河北唐山钢铁厂被投入炼钢炉。与此同时，在全国各省区市１５０个城市，破案追缴和群众主动上缴的１０万余支非法枪支被集中销毁，在全国各指定场所，２５０余吨炸药被分别销毁。公安部治安局局长刘绍武介绍，这次销毁的非法枪支来源于三个方面。刘绍武：打击破案包括涉黑、涉恶的团伙犯罪、毒品犯罪，还有从境外非法走私的枪支爆炸物。在销毁现场，记者看到了被追缴和上缴的各式各样的枪支。刘绍武：也包括制式枪，有的是军用枪、仿制的制式抢，还有猎枪、私制的火药枪等等。按照我国的枪支管理法，这些都是严厉禁止个人非法持有的。中国是世界上持枪犯罪的犯罪率最低的国家之一。中美联手破获特大跨国走私武器弹药案近日，中美执法部门联手成功破获特大跨国走私武器弹药案，在中国抓获犯罪嫌疑人２３名，缴获各类枪支９３支、子弹５万余发及大量枪支配件。在美国抓获犯罪嫌疑人３名，缴获各类枪支１２支。这是公安部与美国移民海关执法局通过联合调查方式侦破重大跨国案件的又一成功案例。２０１１年８月２５日，上海浦东国际机场海关在对美国纽约发往浙江台州，申报品名为扩音器（音箱）的快件进行查验时，发现货物内藏有手枪９支，枪支配件９件，长枪部件７件。经检验，这些都是具有杀伤力的制式枪支及其配件。这引起了公安部和海关总署的高度重视。公安部刑侦局局长刘安成：因为是从海关进口的货物中检查出来夹带，说明来源地是境外，或是说国外，这应该是一起特大跨国走私武器弹药的案件。上海市公安局和上海海关缉私局成立联合专案组，迅速开展案件侦查。专案组于８月２６日在浙江台州ＵＰＳ取件处将犯罪嫌疑人王挺（男，３２岁，台州市人）抓获。王挺交代，他通过一境外网站上认识了上家林志富，２００９年１１月以来，林志富长期居住美国，他通过互联网组建了一个走私、贩卖、私藏枪支弹药的群体，通过网络在国内寻找枪支弹药买家，并通过美国ＵＰＳ联邦速递公司将枪支弹药从纽约快递给多名类似王挺的中间人，再通过中间人发送给国内买家。此案中，犯罪分子依托虚拟网络进行犯罪交易，隐蔽性强，涉案人员使用的身份、地址、联系方式都是虚构的，侦查难度很大。刘安成说，此案体现了是新型犯罪，特别是现代犯罪的新特点。刘安成：他不受距离的限制、经常是跨国跨境，甚至是跨一个、数个、甚至数十个国家。这种犯罪手法的改变和新型犯罪的特点，要求我们各国警方充分合作。作者：汤一亮　庄胜春
   </content>
  </doc>
  <doc>
   <url>
    http://news.sohu.com/20120607/n344998325.shtml
   </url>
   <docno>
    dbb4554e49da2142-69713306c0bb3300
   </docno>
   <contenttitle>
    张绍刚发道歉信网友不认可：他的问题是俯视他人（图）
   </contenttitle>
   <content>
    天津卫视求职节目《非你莫属》“晕倒门”事件余波未了，主持人张绍刚前日通过《非你莫属》节目组发出道歉信，称自己错在对留学生缺乏了解。但他的道歉，没有得到网友的接受和原谅，有网友尖锐指出，张绍刚的问题就在俯视他人，连道歉都不会。张绍刚：我是一番好意之前哪怕被网友骂得再凶，张绍刚也表现彪悍，声称自己没错，绝不道歉。但这几天李开复领衔讨伐节目组，网上民意汹汹要他“下课”，张绍刚显然有点撑不住。前日他通过《非你莫属》节目组，发出一则语焉不详的道歉信。信中他将自己在节目中的表现，解释为一番好意，就像几年前程鹤麟先生说他的，“追在别人屁股后面，碎嘴叨叨地说＂你得这样，这是为了你好＂，而自己的错误，在于对求职者不够了解，没有站在别人的角度考虑问题，“当不了解一个群体的时候，就无法给出准确的判断和建议，今年以来的各种沸沸扬扬，大多源自于此。”他最后表示：“留学生的批评我很感谢，我会努力去了解这个群体的所思所想。有问题的，认识、纠正，这是咱们经常跟同学们说的，今天我对自己说！”网友：别再硬挺下去张绍刚的这番道歉，却没有得到网友的认可。有网友尖锐指出，张绍刚的问题在于俯视他人，连道歉都不会：“张绍刚要么在讲台，要么在舞台，对学生、对选手都掌握生杀大权，高高在上惯了，很难做到平视。他的问题不在于对哪个群体是否了解，而是他的态度。”更有网友认为，张绍刚存在自卑感，“在所有的海归学生访谈的时候，他对于相关外文的资料，先以＂我看不懂＂推脱；当学生提及在当地生活经验的时候，他就在对方的用字里面挑刺；然后吆喝批判学生数典忘祖，不爱祖国”。有网友劝张绍刚：“张先生，请先把自卑处理，再当主持人。”“别再硬挺了，再挺下去就真成棒槌了。”（余乐）作者：余乐　（来源：羊城晚报）
   </content>
  </doc>
 </body>
</html>
-----------------------------------------------------------------------------------------------------------------------


OUTPUT xml date file form：<date> elements added, and <doc> elements were sorted by date Ascending
-----------------------------------------------------------------------------------------------------------------------
<html>
 <head></head>
 <body>
   <doc>
   <url>
    http://news.sohu.com/20120607/n344998325.shtml
   </url>
   <docno>
    dbb4554e49da2142-69713306c0bb3300
   </docno>
   <contenttitle>
    张绍刚发道歉信网友不认可：他的问题是俯视他人（图）
   </contenttitle>
   <content>
    天津卫视求职节目《非你莫属》“晕倒门”事件余波未了，主持人张绍刚前日通过《非你莫属》节目组发出道歉信，称自己错在对留学生缺乏了解。但他的道歉，没有得到网友的接受和原谅，有网友尖锐指出，张绍刚的问题就在俯视他人，连道歉都不会。张绍刚：我是一番好意之前哪怕被网友骂得再凶，张绍刚也表现彪悍，声称自己没错，绝不道歉。但这几天李开复领衔讨伐节目组，网上民意汹汹要他“下课”，张绍刚显然有点撑不住。前日他通过《非你莫属》节目组，发出一则语焉不详的道歉信。信中他将自己在节目中的表现，解释为一番好意，就像几年前程鹤麟先生说他的，“追在别人屁股后面，碎嘴叨叨地说＂你得这样，这是为了你好＂，而自己的错误，在于对求职者不够了解，没有站在别人的角度考虑问题，“当不了解一个群体的时候，就无法给出准确的判断和建议，今年以来的各种沸沸扬扬，大多源自于此。”他最后表示：“留学生的批评我很感谢，我会努力去了解这个群体的所思所想。有问题的，认识、纠正，这是咱们经常跟同学们说的，今天我对自己说！”网友：别再硬挺下去张绍刚的这番道歉，却没有得到网友的认可。有网友尖锐指出，张绍刚的问题在于俯视他人，连道歉都不会：“张绍刚要么在讲台，要么在舞台，对学生、对选手都掌握生杀大权，高高在上惯了，很难做到平视。他的问题不在于对哪个群体是否了解，而是他的态度。”更有网友认为，张绍刚存在自卑感，“在所有的海归学生访谈的时候，他对于相关外文的资料，先以＂我看不懂＂推脱；当学生提及在当地生活经验的时候，他就在对方的用字里面挑刺；然后吆喝批判学生数典忘祖，不爱祖国”。有网友劝张绍刚：“张先生，请先把自卑处理，再当主持人。”“别再硬挺了，再挺下去就真成棒槌了。”（余乐）作者：余乐　（来源：羊城晚报）
   </content>
   <date>20120607</date>
  </doc>
  <doc>
   <url>
    http://news.sohu.com/20120612/n345428229.shtml
   </url>
   <docno>
    c172394d49da2142-69713306c0bb3300
   </docno>
   <contenttitle>
    公安机关销毁１０余万非法枪支　跨国武器走私渐起
   </contenttitle>
   <content>
    中广网唐山６月１２日消息（记者汤一亮　庄胜春）据中国之声《新闻晚高峰》报道，今天（１２日）上午，公安机关２０１２年缉枪制爆专项行动“统一销毁非法枪爆物品活动”在河北唐山正式启动，１０万余只非法枪支、２５０余吨炸药在全国１５０个城市被统一销毁。黄明：现在我宣布，全国缉枪制爆统一销毁行动开始！随着公安部副部长黄明一声令下，大量仿制式枪以及猎枪、火药枪、气枪在河北唐山钢铁厂被投入炼钢炉。与此同时，在全国各省区市１５０个城市，破案追缴和群众主动上缴的１０万余支非法枪支被集中销毁，在全国各指定场所，２５０余吨炸药被分别销毁。公安部治安局局长刘绍武介绍，这次销毁的非法枪支来源于三个方面。刘绍武：打击破案包括涉黑、涉恶的团伙犯罪、毒品犯罪，还有从境外非法走私的枪支爆炸物。在销毁现场，记者看到了被追缴和上缴的各式各样的枪支。刘绍武：也包括制式枪，有的是军用枪、仿制的制式抢，还有猎枪、私制的火药枪等等。按照我国的枪支管理法，这些都是严厉禁止个人非法持有的。中国是世界上持枪犯罪的犯罪率最低的国家之一。中美联手破获特大跨国走私武器弹药案近日，中美执法部门联手成功破获特大跨国走私武器弹药案，在中国抓获犯罪嫌疑人２３名，缴获各类枪支９３支、子弹５万余发及大量枪支配件。在美国抓获犯罪嫌疑人３名，缴获各类枪支１２支。这是公安部与美国移民海关执法局通过联合调查方式侦破重大跨国案件的又一成功案例。２０１１年８月２５日，上海浦东国际机场海关在对美国纽约发往浙江台州，申报品名为扩音器（音箱）的快件进行查验时，发现货物内藏有手枪９支，枪支配件９件，长枪部件７件。经检验，这些都是具有杀伤力的制式枪支及其配件。这引起了公安部和海关总署的高度重视。公安部刑侦局局长刘安成：因为是从海关进口的货物中检查出来夹带，说明来源地是境外，或是说国外，这应该是一起特大跨国走私武器弹药的案件。上海市公安局和上海海关缉私局成立联合专案组，迅速开展案件侦查。专案组于８月２６日在浙江台州ＵＰＳ取件处将犯罪嫌疑人王挺（男，３２岁，台州市人）抓获。王挺交代，他通过一境外网站上认识了上家林志富，２００９年１１月以来，林志富长期居住美国，他通过互联网组建了一个走私、贩卖、私藏枪支弹药的群体，通过网络在国内寻找枪支弹药买家，并通过美国ＵＰＳ联邦速递公司将枪支弹药从纽约快递给多名类似王挺的中间人，再通过中间人发送给国内买家。此案中，犯罪分子依托虚拟网络进行犯罪交易，隐蔽性强，涉案人员使用的身份、地址、联系方式都是虚构的，侦查难度很大。刘安成说，此案体现了是新型犯罪，特别是现代犯罪的新特点。刘安成：他不受距离的限制、经常是跨国跨境，甚至是跨一个、数个、甚至数十个国家。这种犯罪手法的改变和新型犯罪的特点，要求我们各国警方充分合作。作者：汤一亮　庄胜春
   </content>
  <date>20120612</date>
  </doc>
 </body>
</html>
-----------------------------------------------------------------------------------------------------------------------

"""
import xml.sax as sax

class xml_news_handler(sax.ContentHandler):
    """
    sax convert the xml file into list of doc
    """
    # result
    doc_list = []
    # tmp variable
    _doc=None
    _tag = ''

    def __init__(self):
        doc_list=[]

    def startElement(self, tag, attributes):
        self._tag = tag
        if tag == 'doc':
            # create a new element when start elemnt is doc
            self._doc = doc()

    def endElement(self, tag):
        if tag == 'doc':
            if not self._doc.date:
                self._doc.url2date(self._doc.url)
            if self._doc.date and self._doc.content and self._doc.docno and self._doc.url and self._doc.contenttitle:
                # add the date into list if the doc is not empty
                self.doc_list.append(self._doc)

    def characters(self, content):
        if not content.strip():
            return
        if self._tag == 'url':
            self._doc.url = content.strip()
        elif self._tag == 'docno':
            self._doc.docno = content.strip()
        elif self._tag == 'contenttitle':
            self._doc.contenttitle = content.strip()
        elif self._tag == 'content':
            self._doc.content = content.strip()
        elif self._tag == 'date':
            self._doc.date = content.strip()


class doc(object):
    """
    doc struct:
        url
        docno
        contenttitle
        content
        date
    """
    url = ''
    docno = ''
    contenttitle = ''
    content = ''
    date = ''

    def __init__(self, **kwargs):
        """
        init thre parameters from kwargs
        """
        self.init(kwargs)

    def init(self, kwargs):
        """
        :param kwargs: dict
        """
        if not kwargs:
            return
        if kwargs.get('url'):
            self.url = kwargs['url']
        if kwargs.get('docno'):
            self.docno = kwargs['docno']
        if kwargs.get('contenttitle'):
            self.contenttitle = kwargs['contenttitle']
        if kwargs.get('content'):
            self.content = kwargs['content']
        if kwargs.get('date'):
            self.date = kwargs['date']
        else:
            self.url2date(self.url)

    def url2date(self, url):
        """
        fetching the date info if the url contains
        """
        import re
        search = re.search("/20\d{6}/", self.url)
        if search:
            self.date = self.url[search.span()[0] + 1: search.span()[1] - 1]

from xml.dom import minidom

def generate_xml_from_doc_list(list,outputfile):
    """
    transfer the doc list into xml file
    :param list:doc list
    :param outputfile: output xml file path
    """
    impl = minidom.getDOMImplementation()

    # create a xml dom
    # three args ：namespaceURI, qualifiedName, doctype
    d = impl.createDocument(None, None, None)

    # create root element
    root = d.createElement('all')

    # add sub elments into root
    for e in list:
        # create sub elements
        doc = d.createElement('doc')
        url = d.createElement('url')
        docno = d.createElement('docno')
        contenttitle = d.createElement('contenttitle')
        content = d.createElement('content')
        date = d.createElement('date')

        # insert elements content
        url.appendChild(d.createTextNode(e.url))
        docno.appendChild(d.createTextNode(e.docno))
        contenttitle.appendChild(d.createTextNode(e.contenttitle))
        content.appendChild(d.createTextNode(e.content))
        date.appendChild(d.createTextNode(e.date))

        # build the doc elment
        doc.appendChild(url)
        doc.appendChild(docno)
        doc.appendChild(contenttitle)
        doc.appendChild(content)
        doc.appendChild(date)

        # insert doc into root
        root.appendChild(doc)

    # write into xml file
    f = open(outputfile, 'w',encoding='utf-8')
    root.writexml(f, addindent=' ', newl='\n')
    f.close()

def sample(list,begin_date,end_date):
    """
    keep the data in the list whose  begin_date<=date<=end_date
    :param list:
    :param begin_date:
    :param end_date:
    :return: sample(list)
    """
    b_d = int(begin_date)
    e_d = int(end_date)
    sample = []
    for doc in list:
        d = int(doc.date)
        if b_d <= d and d <= e_d:
            sample.append(doc)
    return sample

def load_data_from_xml(xml_file):
    """
    load xml data into meory and return the xml_news_handler instances
    :param xml_file: the source xml file
    :return: the xml_news_handler
    """
    # create a XMLReader
    parser = sax.make_parser()
    # turn off namepsaces
    parser.setFeature(sax.handler.feature_namespaces, 0)

    # Overwrite ContextHandler
    handler = xml_news_handler()
    parser.setContentHandler(handler)

    # parse xml file
    parser.parse(xml_file)

    return handler