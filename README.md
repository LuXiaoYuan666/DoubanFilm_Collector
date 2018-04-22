# DoubanFilm_Collector
* 支持版本: Python 3.6
* 支持数据库： MongoDB

* 使用：
	* 配置Config.ini  
	
	```
	[DB]
	;Configure the database information
	;type: mongodb
	type = mongodb
	host = 127.0.0.1
	port = 27017
	;Configure the database name to save films info
	DBName = dbFilm

	[FilmCollector]
	;choose the type of films in the following option:
	;请填写[剧情,喜剧,动作,爱情,科幻,悬疑,惊悚,恐怖,犯罪,同性,音乐,歌舞,传记,历史,战争,西部,奇幻,冒险,灾难,武侠,情色]
	type  = 同性
	;configure the number to collection.
	;if the number is greater than the number of the films, the result will return the maxium films.
	number of films = 300

	[Proxy]
	;configure the database name to save proxies
	DBName = proxiesName
	;configure the collection name to save proxies
	CollectionName = proxy
	;configure the interval to fetch the proxies
	interval = 5
	```  
	
	* 使用付费代理的可以直接修改GetProxy.py， 使用免费代理请参考https://github.com/jhao104/proxy_pool 
	* 按顺序启动MongoDB，ProxyApi.py以及ProxyManager.py
	* 最后开始run.py
	
	
	
	
