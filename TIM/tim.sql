
DROP TABLE IF EXISTS `text`;
CREATE TABLE `text` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `recvid` varchar(20) NOT NULL DEFAULT '',
  `text` text,
  `userid` varchar(20) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `userid` (`userid`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;



INSERT INTO `text` VALUES (1,'787503811','hello 11','787503810'),(2,'787503810','hello 10','787503811');




DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `userid` varchar(20) NOT NULL,
  `password` varchar(40) NOT NULL DEFAULT '',
  `username` varchar(20) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `state` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`userid`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;



INSERT INTO `user` VALUES ('787503810','123','fwx','787503810@qq..com',0),('787503811','123','fff','787503811@qq..com',0);

