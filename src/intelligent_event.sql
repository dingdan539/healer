/*
SQLyog Ultimate v9.60 
MySQL - 5.6.12-log : Database - intelligent_event
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
  `kind_id` int(11) NOT NULL DEFAULT '0',
  `type_id` int(11) NOT NULL DEFAULT '0',
  `level_id` int(11) NOT NULL DEFAULT '0',
  `source_id` int(11) NOT NULL DEFAULT '0',
  `status` varchar(255) NOT NULL DEFAULT '',
  `remark` varchar(255) NOT NULL DEFAULT '',
  `server_type_id` int(11) NOT NULL DEFAULT '0',
  `rack_id` int(11) NOT NULL DEFAULT '0',
  `switch_ip` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `clock` (`clock`) USING BTREE,
  KEY `ip` (`ip`) USING BTREE,
  KEY `pool_id` (`pool_id`) USING BTREE,
  KEY `site_id` (`site_id`,`pool_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=23618 DEFAULT CHARSET=utf8;

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

/*Table structure for table `alert_2018` */

DROP TABLE IF EXISTS `alert_2018`;

CREATE TABLE `alert_2018` (
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

/*Table structure for table `alert_2019` */

DROP TABLE IF EXISTS `alert_2019`;

CREATE TABLE `alert_2019` (
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

/*Table structure for table `alert_2020` */

DROP TABLE IF EXISTS `alert_2020`;

CREATE TABLE `alert_2020` (
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

/*Table structure for table `api_log` */

DROP TABLE IF EXISTS `api_log`;

CREATE TABLE `api_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from_ip` varchar(255) NOT NULL DEFAULT '',
  `path` varchar(255) NOT NULL DEFAULT '',
  `user_id` int(11) NOT NULL DEFAULT '0',
  `date` int(11) NOT NULL,
  `remark` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=631 DEFAULT CHARSET=utf8;

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
  `level_id` int(11) NOT NULL DEFAULT '0',
  `source_id` int(11) NOT NULL DEFAULT '0' COMMENT '直接得到',
  `status` varchar(255) NOT NULL DEFAULT '' COMMENT '计算',
  `remark` varchar(255) NOT NULL DEFAULT '' COMMENT '计算or直接得到',
  `enable` int(11) NOT NULL DEFAULT '0' COMMENT '0-未处理',
  `server_type_id` int(11) NOT NULL DEFAULT '0',
  `rack_id` int(11) NOT NULL DEFAULT '0',
  `switch_ip` varchar(255) NOT NULL DEFAULT '',
  `probably_id` int(11) NOT NULL DEFAULT '0',
  `probably_reason` varchar(255) DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1533 DEFAULT CHARSET=utf8;

/*Table structure for table `kind_map` */

DROP TABLE IF EXISTS `kind_map`;

CREATE TABLE `kind_map` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

/*Table structure for table `level_map` */

DROP TABLE IF EXISTS `level_map`;

CREATE TABLE `level_map` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

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
  `enable` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `end_time` (`enable`,`start_time`,`end_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `source_map` */

DROP TABLE IF EXISTS `source_map`;

CREATE TABLE `source_map` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

/*Table structure for table `type_map` */

DROP TABLE IF EXISTS `type_map`;

CREATE TABLE `type_map` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `level_id` int(11) NOT NULL DEFAULT '0',
  `kind_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8;

/*Table structure for table `user_token` */

DROP TABLE IF EXISTS `user_token`;

CREATE TABLE `user_token` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(255) NOT NULL DEFAULT '',
  `token` varchar(255) NOT NULL DEFAULT '',
  `get_time` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
