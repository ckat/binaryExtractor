import lxml.etree as etree;
import base64
import os


def extractPdf (type, dataBlocks, startIndex, runId):
	i = startIndex;
	for dataBlock in dataBlocks:
		i = i+1;
		fileName = "result_" + type + "_" + str(runId) + "_" + str(i) +".pdf";
		print("Decoding to: " + fileName);
		f = open(fileName, 'wb');
		decoded = base64.b64decode(dataBlock)
		f.write(decoded)
	return i - startIndex;

root = 	etree.parse("sample2.xml");
pid = os.getpid() # just a unique enough id 
NSMAP = {'ent': 'http://omsoe.crm.tmobile.net/datatypes/entity'}
orderImages = root.xpath("//ent:OrderImage/ent:data/text()", namespaces = NSMAP)
receipts = root.xpath("//ent:SalesPartnerOrderReceipt/ent:data/text()", namespaces = NSMAP)
count = 0;
count += extractPdf("OrderImage", orderImages, count, pid);
count += extractPdf("SalesPartnerOrderReceipt",receipts, count, pid);
print("Extracted " + str(count) + " data block(s)")