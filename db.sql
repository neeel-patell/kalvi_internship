/*
SQLyog Community
MySQL - 10.4.10-MariaDB : Database - schedules
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`schedules` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `schedules`;

/*Table structure for table `scheduled_classes` */

CREATE TABLE `scheduled_classes` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `topic` varchar(50) NOT NULL,
  `subject` int(11) NOT NULL,
  `clss` int(11) NOT NULL,
  `board` varchar(10) NOT NULL,
  `description` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `start_time` time(6) NOT NULL,
  `end_time` time(6) NOT NULL,
  `meeting_link` varchar(50) NOT NULL,
  `language` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `scheduled_classes` */

insert  into `scheduled_classes`(`id`,`topic`,`subject`,`clss`,`board`,`description`,`date`,`start_time`,`end_time`,`meeting_link`,`language`) values (1,'Chapter-1',1,8,'CBSE','About Linear Algebra','2021-09-12','10:00:00.000000','11:00:00.000000','https://meet.google.com/aassasasasas',1);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
