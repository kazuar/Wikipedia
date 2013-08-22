# -*- coding: utf-8 -*-

mock_data = {
	"_wiki_request calls": {

		"{'inprop': 'url', 'titles': 'purpleberry', 'clcategories': 'Category:All disambiguation pages', 'prop': 'info|categories'}":
		{u'query': {u'normalized': [{u'to': u'Purpleberry', u'from': u'purpleberry'}], u'pages': {u'-1': {u'missing': u'', u'editurl': u'http://en.wikipedia.org/w/index.php?title=Purpleberry&action=edit', u'title': u'Purpleberry', u'contentmodel': u'wikitext', u'pagelanguage': u'en', u'ns': 0, u'fullurl': u'http://en.wikipedia.org/wiki/Purpleberry'}}}},

		"{'srinfo': 'suggestion', 'srlimit': 1, 'srsearch': 'Menlo Park, New Jersey', 'list': 'search', 'srprop': '', 'limit': 1}":
		{u'query-continue': {u'search': {u'sroffset': 1}}, u'query': {u'search': [{u'ns': 0, u'title': u'Edison, New Jersey'}]}, u'warnings': {u'main': {u'*': u"Unrecognized parameter: 'limit'"}}},
		
		"{'inprop': 'url', 'titles': 'Menlo Park, New Jersey', 'clcategories': 'Category:All disambiguation pages', 'prop': 'info|categories'}":
		{u'query': {u'pages': {u'342479': {u'redirect': u'', u'lastrevid': 463208951, u'pageid': 342479, u'title': u'Menlo Park, New Jersey', u'editurl': u'http://en.	wikipedia.org/w/index.php?title=Menlo_Park,_New_Jersey&action=edit', u'counter': u'', u'length': 74, u'contentmodel': u'wikitext', u'pagelanguage': u'en', u'	touched': u'2013-08-06T02:49:09Z', u'ns': 0, u'fullurl': u'http://en.wikipedia.org/wiki/Menlo_Park,_New_Jersey'}}}},
	
		"{'explaintext': '', 'titles': 'Menlo Park, New Jersey', 'prop': 'extracts'}":
		{u'query': {u'pages': {u'342479': {u'extract': u'REDIRECT Edison, New Jersey', u'ns': 0, u'pageid': 342479, u'title': u'Menlo Park, New Jersey'}}}},
	
		"{'inprop': 'url', 'titles': u'Edison, New Jersey', 'clcategories': 'Category:All disambiguation pages', 'prop': 'info|categories'}":
		{u'query': {u'pages': {u'125414': {u'lastrevid': 567347824, u'pageid': 125414, u'title': u'Edison, New Jersey', u'editurl': u'http://en.wikipedia.org/w/index.	php?title=Edison,_New_Jersey&action=edit', u'counter': u'', u'length': 78472, u'contentmodel': u'wikitext', u'pagelanguage': u'en', u'touched': u'2013-08-	08T22:21:48Z', u'ns': 0, u'fullurl': u'http://en.wikipedia.org/wiki/Edison,_New_Jersey'}}}},
	
		"{'inprop': 'url', 'titles': 'Dodge Ram (disambiguation)', 'clcategories': 'Category:All disambiguation pages', 'prop': 'info|categories'}":
		{u'query': {u'pages': {u'18803364': {u'lastrevid': 567152802, u'pageid': 18803364, u'title': u'Dodge Ram (disambiguation)', u'editurl': u'http://en.wikipedia.	org/w/index.php?title=Dodge_Ram_(disambiguation)&action=edit', u'counter': u'', u'length': 702, u'contentmodel': u'wikitext', u'pagelanguage': u'en', u'touched	': u'2013-08-08T15:12:27Z', u'ns': 0, u'fullurl': u'http://en.wikipedia.org/wiki/Dodge_Ram_(disambiguation)', u'categories': [{u'ns': 14, u'title': u'	Category:All disambiguation pages'}]}}}},
	
		"{'rvparse': '', 'titles': 'Dodge Ram (disambiguation)', 'rvprop': 'content', 'rvlimit': 1, 'prop': 'revisions'}":
		{u'query-continue': {u'revisions': {u'rvcontinue': 556603298}}, u'query': {u'pages': {u'18803364': {u'ns': 0, u'pageid': 18803364, u'revisions': [{u'*': u'<p><b><	a href="/wiki/Dodge_Ram" title="Dodge Ram">Dodge Ram</a></b> is a collective nameplate for light trucks made by <a href="/wiki/Dodge" title="Dodge">Dodge</a>\n	</p>\n<ul><li><a href="/wiki/Dodge_Ramcharger" title="Dodge Ramcharger">Dodge Ramcharger</a> - full-size SUV based on the Ram chassis (first vehicle to use 	the Ram name)\n</li><li><a href="/wiki/Dodge_Ram_Van" title="Dodge Ram Van">Dodge Ram Van</a> - full-size van\n</li><li><a href="/wiki/Dodge_Mini_Ram" 	title="Dodge Mini Ram" class="mw-redirect">Dodge Mini Ram</a> - cargo version of the Dodge Caravan\n<ul><li>See also:\n<ul><li><a 	href="/wiki/Dodge_Caravan_C/V" title="Dodge Caravan C/V" class="mw-redirect">Dodge Caravan C/V</a>\n</li><li><a href="/wiki/Ram_C/V" title="Ram C/V" class="mw-	redirect">Ram C/V</a> (modern day equivalent)\n</li></ul>\n</li></ul>\n</li><li><a href="/wiki/Dodge_Ram_50" title="Dodge Ram 50" class="mw-redirect">Dodge Ram 50</a> - Dodge version of the Mitsubishi Mighty Max, predecessor to the Dakota\n</li></ul>\n<p>See also:\n</p>\n<ul><li><a href="/wiki/Dodge_D-Series" 	title="Dodge D-Series" class="mw-redirect">Dodge D-Series</a> - Ram\'s predecessor, page includes first Ram body style\n</li><li><a href="/wiki/Dodge_Rampage" 	title="Dodge Rampage">Dodge Rampage</a> - car-based pickup truck\n</li><li><a href="/wiki/Ram_Trucks" title="Ram Trucks">Ram (brand)</a> - truck brand based 	on the Ram pickup truck\n</li></ul>\n<table id="disambigbox" class="metadata plainlinks dmbox dmbox-disambig" style="" role="presentation">\n<tr>\n<td 	class="mbox-image" style="padding: 2px 0 2px 0.4em;"> <a href="/wiki/File:Disambig_gray.svg" class="image"><img alt="Disambiguation icon" src="//upload.	wikimedia.org/wikipedia/en/thumb/5/5f/Disambig_gray.svg/30px-Disambig_gray.svg.png" width="30" height="23" srcset="//upload.wikimedia.	org/wikipedia/en/thumb/5/5f/Disambig_gray.svg/45px-Disambig_gray.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/5/5f/Disambig_gray.svg/60px-	Disambig_gray.svg.png 2x" /></a></td>\n<td class="mbox-text" style="padding: 0.25em 0.4em; font-style: italic;"> This <a href="/wiki/Help:Disambiguation" 	title="Help:Disambiguation">disambiguation</a> page lists articles associated with the same title. <br/> <small>If an <a class="external text" href="//en.	wikipedia.org/w/index.php?title=Special:WhatLinksHere/Dodge_Ram_(disambiguation)&amp;namespace=0">internal link</a> led you here, you may wish to change the 	link to point directly to the intended article.</small> </td>\n</tr>\n</table>\n'}], u'title': u'Dodge Ram (disambiguation)'}}}},
	
		"{'srinfo': 'suggestion', 'srlimit': 1, 'srsearch': 'butteryfly', 'list': 'search', 'srprop': '', 'limit': 1}":
		{u'query-continue': {u'search': {u'sroffset': 1}}, u'query': {u'searchinfo': {u'suggestion': u'butterfly'}, u'search': [{u'ns': 0, u'title': u"Butterfly's Tongue"}	]}, u'warnings': {u'main': {u'*': u"Unrecognized parameter: 'limit'"}}},
	
		"{'inprop': 'url', 'titles': u'butterfly', 'clcategories': 'Category:All disambiguation pages', 'prop': 'info|categories'}":
		{u'query': {u'normalized': [{u'to': u'Butterfly', u'from': u'butterfly'}], u'pages': {u'48338': {u'lastrevid': 566847704, u'pageid': 48338, u'title': u'Butterfly',	 u'editurl': u'http://en.wikipedia.org/w/index.php?title=Butterfly&action=edit', u'counter': u'', u'length': 60572, u'contentmodel': u'wikitext', u'	pagelanguage': u'en', u'touched': u'2013-08-07T11:15:37Z', u'ns': 0, u'fullurl': u'http://en.wikipedia.org/wiki/Butterfly'}}}},

		"{'srinfo': 'suggestion', 'srlimit': 1, 'srsearch': 'Celtuce', 'list': 'search', 'srprop': '', 'limit': 1}":
		{u'query-continue': {u'search': {u'sroffset': 1}}, u'query': {u'search': [{u'ns': 0, u'title': u'Celtuce'}]}, u'warnings': {u'main': {u'*': u"Unrecognized parameter: 'limit'"}}},

		"{'inprop': 'url', 'titles': u'Celtuce', 'clcategories': 'Category:All disambiguation pages', 'prop': 'info|categories'}":
		{u'query': {u'pages': {u'1868108': {u'lastrevid': 562756085, u'pageid': 1868108, u'title': u'Celtuce', u'editurl': u'http://en.wikipedia.org/w/index.php?title=Celtuce&action=edit', u'counter': u'', u'length': 1662, u'contentmodel': u'wikitext', u'pagelanguage': u'en', u'touched': u'2013-08-17T03:30:23Z', u'ns': 0, u'fullurl': u'http://en.wikipedia.org/wiki/Celtuce'}}}},

		"{'explaintext': '', 'titles': u'Celtuce', 'prop': 'extracts'}":
		{u'query': {u'pages': {u'1868108': {u'extract': u'Celtuce (Lactuca sativa var. asparagina, augustana, or angustata), also called stem lettuce, celery lettuce, asparagus lettuce, or Chinese lettuce, IPA (UK,US) /\u02c8s\u025blt.\u0259s/, is a cultivar of lettuce grown primarily for its thick stem, used as a vegetable. It is especially popular in China, and is called wosun (Chinese: \u83b4\u7b0b; pinyin: w\u014ds\u016dn) or woju (Chinese: \u83b4\u82e3; pinyin: w\u014dj\xf9) (although the latter name may also be used to mean lettuce in general).\n\nThe stem is usually harvested at a length of around 15\u201320 cm and a diameter of around 3\u20134 cm. It is crisp, moist, and mildly flavored, and typically prepared by slicing and then stir frying with more strongly flavored ingredients.', u'ns': 0, u'pageid': 1868108, u'title': u'Celtuce'}}}},

		"{'exintro': '', 'titles': u'Celtuce', 'explaintext': '', 'prop': 'extracts'}":
		{u'query': {u'pages': {u'1868108': {u'extract': u'Celtuce (Lactuca sativa var. asparagina, augustana, or angustata), also called stem lettuce, celery lettuce, asparagus lettuce, or Chinese lettuce, IPA (UK,US) /\u02c8s\u025blt.\u0259s/, is a cultivar of lettuce grown primarily for its thick stem, used as a vegetable. It is especially popular in China, and is called wosun (Chinese: \u83b4\u7b0b; pinyin: w\u014ds\u016dn) or woju (Chinese: \u83b4\u82e3; pinyin: w\u014dj\xf9) (although the latter name may also be used to mean lettuce in general).\n\nThe stem is usually harvested at a length of around 15\u201320 cm and a diameter of around 3\u20134 cm. It is crisp, moist, and mildly flavored, and typically prepared by slicing and then stir frying with more strongly flavored ingredients.', u'ns': 0, u'pageid': 1868108, u'title': u'Celtuce'}}}},

		"{'gimlimit': 'max', 'iiprop': 'url', 'titles': u'Celtuce', 'generator': 'images', 'prop': 'imageinfo'}":
		{u'query': {u'pages': {u'22263385': {u'imagerepository': u'local', u'ns': 6, u'pageid': 22263385, u'imageinfo': [{u'url': u'http://upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg', u'descriptionurl': u'http://en.wikipedia.org/wiki/File:Question_book-new.svg'}], u'title': u'File:Question book-new.svg'}, u'-1': {u'imagerepository': u'shared', u'ns': 6, u'imageinfo': [{u'url': u'http://upload.wikimedia.org/wikipedia/commons/8/87/Celtuce.jpg', u'descriptionurl': u'http://commons.wikimedia.org/wiki/File:Celtuce.jpg'}], u'missing': u'', u'title': u'File:Celtuce.jpg'}, u'-3': {u'imagerepository': u'shared', u'ns': 6, u'imageinfo': [{u'url': u'http://upload.wikimedia.org/wikipedia/commons/7/79/VegCorn.jpg', u'descriptionurl': u'http://commons.wikimedia.org/wiki/File:VegCorn.jpg'}], u'missing': u'', u'title': u'File:VegCorn.jpg'}, u'-2': {u'imagerepository': u'shared', u'ns': 6, u'imageinfo': [{u'url': u'http://upload.wikimedia.org/wikipedia/commons/d/dc/The_farmer%27s_market_near_the_Potala_in_Lhasa.jpg', u'descriptionurl': u'http://commons.wikimedia.org/wiki/File:The_farmer%27s_market_near_the_Potala_in_Lhasa.jpg'}], u'missing': u'', u'title': u"File:The farmer's market near the Potala in Lhasa.jpg"}}}, u'limits': {u'images': 500}},

		"{'titles': u'Celtuce', 'prop': 'extlinks', 'ellimit': 'max'}":
		{u'query': {u'pages': {u'1868108': {u'extlinks': [{u'*': u'http://ndb.nal.usda.gov/ndb/search/list'}, {u'*': u'http://ndb.nal.usda.gov/ndb/search/list?qlookup=11145&format=Full'}], u'ns': 0, u'pageid': 1868108, u'title': u'Celtuce'}}}, u'limits': {u'extlinks': 500}},

		"{'plnamespace': 0, 'titles': u'Celtuce', 'pllimit': 'max', 'prop': 'links'}":
		{u'query': {u'pages': {u'1868108': {u'ns': 0, u'pageid': 1868108, u'links': [{u'ns': 0, u'title': u'Calcium'}, {u'ns': 0, u'title': u'Carbohydrate'}, {u'ns': 0, u'title': u'Chinese language'}, {u'ns': 0, u'title': u'Dietary Reference Intake'}, {u'ns': 0, u'title': u'Dietary fiber'}, {u'ns': 0, u'title': u'Fat'}, {u'ns': 0, u'title': u'Folate'}, {u'ns': 0, u'title': u'Food energy'}, {u'ns': 0, u'title': u'Iron'}, {u'ns': 0, u'title': u'Lettuce'}, {u'ns': 0, u'title': u'Lhasa'}, {u'ns': 0, u'title': u'Magnesium in biology'}, {u'ns': 0, u'title': u'Manganese'}, {u'ns': 0, u'title': u'Niacin'}, {u'ns': 0, u'title': u'Pantothenic acid'}, {u'ns': 0, u'title': u'Phosphorus'}, {u'ns': 0, u'title': u'Pinyin'}, {u'ns': 0, u'title': u'Plant stem'}, {u'ns': 0, u'title': u'Potassium'}, {u'ns': 0, u'title': u'Protein (nutrient)'}, {u'ns': 0, u'title': u'Riboflavin'}, {u'ns': 0, u'title': u'Sodium'}, {u'ns': 0, u'title': u'Stir frying'}, {u'ns': 0, u'title': u'Thiamine'}, {u'ns': 0, u'title': u'Vegetable'}, {u'ns': 0, u'title': u'Vitamin A'}, {u'ns': 0, u'title': u'Vitamin B6'}, {u'ns': 0, u'title': u'Vitamin C'}, {u'ns': 0, u'title': u'Zinc'}], u'title': u'Celtuce'}}}, u'limits': {u'links': 500}},
	},

	"data": {
		"celtuce.content": u"Celtuce (Lactuca sativa var. asparagina, augustana, or angustata), also called stem lettuce, celery lettuce, asparagus lettuce, or Chinese lettuce, IPA (UK,US) /\u02c8s\u025blt.\u0259s/, is a cultivar of lettuce grown primarily for its thick stem, used as a vegetable. It is especially popular in China, and is called wosun (Chinese: \u83b4\u7b0b; pinyin: w\u014ds\u016dn) or woju (Chinese: \u83b4\u82e3; pinyin: w\u014dj\xf9) (although the latter name may also be used to mean lettuce in general).\n\nThe stem is usually harvested at a length of around 15\u201320 cm and a diameter of around 3\u20134 cm. It is crisp, moist, and mildly flavored, and typically prepared by slicing and then stir frying with more strongly flavored ingredients.",

		"celtuce.summary": u"Celtuce (Lactuca sativa var. asparagina, augustana, or angustata), also called stem lettuce, celery lettuce, asparagus lettuce, or Chinese lettuce, IPA (UK,US) /\u02c8s\u025blt.\u0259s/, is a cultivar of lettuce grown primarily for its thick stem, used as a vegetable. It is especially popular in China, and is called wosun (Chinese: \u83b4\u7b0b; pinyin: w\u014ds\u016dn) or woju (Chinese: \u83b4\u82e3; pinyin: w\u014dj\xf9) (although the latter name may also be used to mean lettuce in general).\n\nThe stem is usually harvested at a length of around 15\u201320 cm and a diameter of around 3\u20134 cm. It is crisp, moist, and mildly flavored, and typically prepared by slicing and then stir frying with more strongly flavored ingredients.",

		"celtuce.images": [u'http://upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg', u'http://upload.wikimedia.org/wikipedia/commons/8/87/Celtuce.jpg', u'http://upload.wikimedia.org/wikipedia/commons/7/79/VegCorn.jpg', u'http://upload.wikimedia.org/wikipedia/commons/d/dc/The_farmer%27s_market_near_the_Potala_in_Lhasa.jpg'],

		"celtuce.references": [u'http://ndb.nal.usda.gov/ndb/search/list', u'http://ndb.nal.usda.gov/ndb/search/list?qlookup=11145&format=Full'],

		"celtuce.links": [u'Calcium', u'Carbohydrate', u'Chinese language', u'Dietary Reference Intake', u'Dietary fiber', u'Fat', u'Folate', u'Food energy', u'Iron', u'Lettuce', u'Lhasa', u'Magnesium in biology', u'Manganese', u'Niacin', u'Pantothenic acid', u'Phosphorus', u'Pinyin', u'Plant stem', u'Potassium', u'Protein (nutrient)', u'Riboflavin', u'Sodium', u'Stir frying', u'Thiamine', u'Vegetable', u'Vitamin A', u'Vitamin B6', u'Vitamin C', u'Zinc'],
	}
}