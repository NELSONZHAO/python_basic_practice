# coding: utf-8
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
import urllib

# 获取文档对象
# fp = open("SMCM.pdf","rb")
fp = urllib.urlopen("http://www.tencent.com/zh-cn/content/ir/an/2016/attachments/20160321.pdf")

# 创建解释器
parser = PDFParser(fp)

# 创建pdf文档对象
doc = PDFDocument()

# 链接解释器和文档对象
parser.set_document(doc)
doc.set_parser(parser)

# 初始化文档
doc.initialize("")

# 创建pdf资源管理器
resource = PDFResourceManager()

# 参数分析器
laparam = LAParams()

# 创建pdf聚合器
device = PDFPageAggregator(resource, laparams=laparam)

# 创建页面解释器
interpreter = PDFPageInterpreter(resource, device)

# 使用文档对象从页面读取内容
for page in doc.get_pages():
	# 使用页面解释器来读取
	interpreter.process_page(page)

	# 使用聚合器来获得内容
	layout = device.get_result()

	for out in layout:
		if hasattr(out, "get_text"):
			print out.get_text()
