/*
SQLyog Ultimate v9.60 
MySQL - 5.6.17 : Database - intelligent_event
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`intelligent_event` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `intelligent_event`;

/*Table structure for table `alert_2015` */

DROP TABLE IF EXISTS `alert_2015`;

CREATE TABLE `alert_2015` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(255) NOT NULL DEFAULT '',
  `site_id` int(11) NOT NULL DEFAULT '0',
  `pool_id` int(11) NOT NULL DEFAULT '0',
  `host_name` varchar(255) NOT NULL DEFAULT '',
  `description` text NOT NULL,
  `clock` int(11) NOT NULL DEFAULT '0',
  `kind_id` int(11) NOT NULL DEFAULT '0',
  `type_id` int(11) NOT NULL DEFAULT '0',
  `level_id` int(11) NOT NULL DEFAULT '0',
  `source_id` int(11) NOT NULL DEFAULT '0',
  `status` varchar(255) NOT NULL DEFAULT '',
  `remark` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `clock` (`clock`) USING BTREE,
  KEY `ip` (`ip`) USING BTREE,
  KEY `pool_id` (`pool_id`) USING BTREE,
  KEY `site_id` (`site_id`,`pool_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `alert_2015` */

/*Table structure for table `alert_2016` */

DROP TABLE IF EXISTS `alert_2016`;

CREATE TABLE `alert_2016` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(255) NOT NULL DEFAULT '',
  `site_id` int(11) NOT NULL DEFAULT '0',
  `pool_id` int(11) NOT NULL DEFAULT '0',
  `host_name` varchar(255) NOT NULL DEFAULT '',
  `description` text NOT NULL,
  `clock` int(11) NOT NULL DEFAULT '0',
  `type` int(11) NOT NULL DEFAULT '0',
  `source` int(11) NOT NULL DEFAULT '0',
  `status` varchar(255) NOT NULL DEFAULT '',
  `remark` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `alert_2016` */

/*Table structure for table `alert_2017` */

DROP TABLE IF EXISTS `alert_2017`;

CREATE TABLE `alert_2017` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(255) NOT NULL DEFAULT '',
  `site_id` int(11) NOT NULL DEFAULT '0',
  `pool_id` int(11) NOT NULL DEFAULT '0',
  `host_name` varchar(255) NOT NULL DEFAULT '',
  `description` text NOT NULL,
  `clock` int(11) NOT NULL DEFAULT '0',
  `type` int(11) NOT NULL DEFAULT '0',
  `source` int(11) NOT NULL DEFAULT '0',
  `status` varchar(255) NOT NULL DEFAULT '',
  `remark` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `alert_2017` */

/*Table structure for table `important_event` */

DROP TABLE IF EXISTS `important_event`;

CREATE TABLE `important_event` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(255) NOT NULL DEFAULT '' COMMENT '计算or直接得到',
  `site_id` int(11) NOT NULL DEFAULT '0' COMMENT '计算or直接得到',
  `pool_id` int(11) NOT NULL DEFAULT '0' COMMENT '计算or直接得到',
  `host_name` varchar(255) NOT NULL DEFAULT '' COMMENT '直接得到',
  `description` text NOT NULL COMMENT '直接得到',
  `clock` int(11) NOT NULL DEFAULT '0' COMMENT '默认or直接得到',
  `kind_id` int(11) NOT NULL DEFAULT '0',
  `type_id` int(11) NOT NULL DEFAULT '0' COMMENT '计算',
  `source_id` int(11) NOT NULL DEFAULT '0' COMMENT '直接得到',
  `status` varchar(255) NOT NULL DEFAULT '' COMMENT '计算',
  `remark` varchar(255) NOT NULL DEFAULT '' COMMENT '计算or直接得到',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `important_event` */

/*Table structure for table `kind_map` */

DROP TABLE IF EXISTS `kind_map`;

CREATE TABLE `kind_map` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

/*Data for the table `kind_map` */

insert  into `kind_map`(`id`,`name`) values (1,'可用性'),(2,'稳定性');

/*Table structure for table `level_map` */

DROP TABLE IF EXISTS `level_map`;

CREATE TABLE `level_map` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

/*Data for the table `level_map` */

insert  into `level_map`(`id`,`name`) values (1,'网络层'),(2,'系统层'),(3,'中间件层'),(4,'应用层'),(5,'业务层');

/*Table structure for table `shield` */

DROP TABLE IF EXISTS `shield`;

CREATE TABLE `shield` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pool_id` int(11) NOT NULL DEFAULT '0',
  `ip` varchar(255) NOT NULL DEFAULT '',
  `key` varchar(255) NOT NULL DEFAULT '',
  `level_id` int(11) NOT NULL DEFAULT '0',
  `source_id` int(11) NOT NULL DEFAULT '0',
  `start_time` int(11) NOT NULL DEFAULT '0',
  `end_time` int(11) NOT NULL DEFAULT '0',
  `expire_time` int(11) NOT NULL DEFAULT '0',
  `status` int(11) NOT NULL DEFAULT '0' COMMENT '0-屏蔽中 1-已取消屏蔽',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Data for the table `shield` */

insert  into `shield`(`id`,`pool_id`,`ip`,`key`,`level_id`,`source_id`,`start_time`,`end_time`,`expire_time`,`status`) values (1,486,'1','',0,0,12345670,12345679,12345699,0);

/*Table structure for table `source_map` */

DROP TABLE IF EXISTS `source_map`;

CREATE TABLE `source_map` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

/*Data for the table `source_map` */

insert  into `source_map`(`id`,`name`) values (1,'zabbix'),(2,'healthcheck');

/*Table structure for table `type_map` */

DROP TABLE IF EXISTS `type_map`;

CREATE TABLE `type_map` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `level_id` int(11) NOT NULL DEFAULT '0',
  `kind_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8;

/*Data for the table `type_map` */

insert  into `type_map`(`id`,`name`,`level_id`,`kind_id`) values (1,'traffic utilization',1,2),(2,'netstat established',1,2),(3,'cpu utilization',2,2),(4,'tomcat port 8080',4,1),(5,'disk space',2,1),(6,'load',2,2),(9,'zabbix agent',3,1),(10,'order number',5,1),(11,'squid',3,1),(12,'mysql port',4,1),(13,'cms',4,1),(14,'cdn',1,2),(15,'memcache',3,1),(16,'swap',2,2),(17,'oracle',4,1),(18,'zk',4,1),(19,'network established',1,2),(20,'webserver port',4,1),(21,'disk I/O',2,2),(22,'network time wait',1,2),(23,'dts java',4,1),(24,'tomcat full gc',4,1),(25,'redis',3,1),(26,'netstat timewait',1,2),(27,'mem',3,1),(28,'mongo',3,1),(29,'JMX',4,1),(30,'free inodes',2,2),(31,'SSLVPN',1,1),(32,'python',4,1),(33,'ping',1,1),(34,'jumper full gc',4,1),(35,'traffic changed a lot',1,1),(36,'zookeeper',4,1),(37,'service sequence',2,1),(38,'kafka',3,1);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
