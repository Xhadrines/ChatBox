/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19-12.1.2-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: chatbox_db
-- ------------------------------------------------------
-- Server version	12.1.2-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*M!100616 SET @OLD_NOTE_VERBOSITY=@@NOTE_VERBOSITY, NOTE_VERBOSITY=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `auth_permission` VALUES
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add plan types',7,'add_plantypes'),
(26,'Can change plan types',7,'change_plantypes'),
(27,'Can delete plan types',7,'delete_plantypes'),
(28,'Can view plan types',7,'view_plantypes'),
(29,'Can add user roles',8,'add_userroles'),
(30,'Can change user roles',8,'change_userroles'),
(31,'Can delete user roles',8,'delete_userroles'),
(32,'Can view user roles',8,'view_userroles'),
(33,'Can add user status',9,'add_userstatus'),
(34,'Can change user status',9,'change_userstatus'),
(35,'Can delete user status',9,'delete_userstatus'),
(36,'Can view user status',9,'view_userstatus'),
(37,'Can add plans',10,'add_plans'),
(38,'Can change plans',10,'change_plans'),
(39,'Can delete plans',10,'delete_plans'),
(40,'Can view plans',10,'view_plans'),
(41,'Can add users',11,'add_users'),
(42,'Can change users',11,'change_users'),
(43,'Can delete users',11,'delete_users'),
(44,'Can view users',11,'view_users'),
(45,'Can add user plans',12,'add_userplans'),
(46,'Can change user plans',12,'change_userplans'),
(47,'Can delete user plans',12,'delete_userplans'),
(48,'Can view user plans',12,'view_userplans'),
(49,'Can add messages',13,'add_messages'),
(50,'Can change messages',13,'change_messages'),
(51,'Can delete messages',13,'delete_messages'),
(52,'Can view messages',13,'view_messages'),
(53,'Can add files',14,'add_files'),
(54,'Can change files',14,'change_files'),
(55,'Can delete files',14,'delete_files'),
(56,'Can view files',14,'view_files'),
(57,'Can add user usage',15,'add_userusage'),
(58,'Can change user usage',15,'change_userusage'),
(59,'Can delete user usage',15,'delete_userusage'),
(60,'Can view user usage',15,'view_userusage'),
(61,'Can add plan types',16,'add_plantypes'),
(62,'Can change plan types',16,'change_plantypes'),
(63,'Can delete plan types',16,'delete_plantypes'),
(64,'Can view plan types',16,'view_plantypes'),
(65,'Can add user roles',17,'add_userroles'),
(66,'Can change user roles',17,'change_userroles'),
(67,'Can delete user roles',17,'delete_userroles'),
(68,'Can view user roles',17,'view_userroles'),
(69,'Can add user status',18,'add_userstatus'),
(70,'Can change user status',18,'change_userstatus'),
(71,'Can delete user status',18,'delete_userstatus'),
(72,'Can view user status',18,'view_userstatus'),
(73,'Can add plans',19,'add_plans'),
(74,'Can change plans',19,'change_plans'),
(75,'Can delete plans',19,'delete_plans'),
(76,'Can view plans',19,'view_plans'),
(77,'Can add users',20,'add_users'),
(78,'Can change users',20,'change_users'),
(79,'Can delete users',20,'delete_users'),
(80,'Can view users',20,'view_users'),
(81,'Can add user plans',21,'add_userplans'),
(82,'Can change user plans',21,'change_userplans'),
(83,'Can delete user plans',21,'delete_userplans'),
(84,'Can view user plans',21,'view_userplans'),
(85,'Can add messages',22,'add_messages'),
(86,'Can change messages',22,'change_messages'),
(87,'Can delete messages',22,'delete_messages'),
(88,'Can view messages',22,'view_messages'),
(89,'Can add files',23,'add_files'),
(90,'Can change files',23,'change_files'),
(91,'Can delete files',23,'delete_files'),
(92,'Can view files',23,'view_files'),
(93,'Can add user token',24,'add_usertoken'),
(94,'Can change user token',24,'change_usertoken'),
(95,'Can delete user token',24,'delete_usertoken'),
(96,'Can view user token',24,'view_usertoken'),
(97,'Can add user usage',25,'add_userusage'),
(98,'Can change user usage',25,'change_userusage'),
(99,'Can delete user usage',25,'delete_userusage'),
(100,'Can view user usage',25,'view_userusage');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `django_content_type` VALUES
(1,'admin','logentry'),
(14,'api_orm_sf','files'),
(13,'api_orm_sf','messages'),
(10,'api_orm_sf','plans'),
(7,'api_orm_sf','plantypes'),
(12,'api_orm_sf','userplans'),
(8,'api_orm_sf','userroles'),
(11,'api_orm_sf','users'),
(9,'api_orm_sf','userstatus'),
(15,'api_orm_sf','userusage'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(23,'common','files'),
(22,'common','messages'),
(19,'common','plans'),
(16,'common','plantypes'),
(21,'common','userplans'),
(17,'common','userroles'),
(20,'common','users'),
(18,'common','userstatus'),
(24,'common','usertoken'),
(25,'common','userusage'),
(5,'contenttypes','contenttype'),
(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `django_migrations` VALUES
(1,'contenttypes','0001_initial','2025-11-25 09:30:07.044012'),
(2,'auth','0001_initial','2025-11-25 09:30:08.670905'),
(3,'admin','0001_initial','2025-11-25 09:30:08.984201'),
(4,'admin','0002_logentry_remove_auto_add','2025-11-25 09:30:08.993012'),
(5,'admin','0003_logentry_add_action_flag_choices','2025-11-25 09:30:09.001937'),
(6,'api_orm_sf','0001_initial','2025-11-25 09:30:10.467898'),
(7,'contenttypes','0002_remove_content_type_name','2025-11-25 09:30:10.746897'),
(8,'auth','0002_alter_permission_name_max_length','2025-11-25 09:30:10.909805'),
(9,'auth','0003_alter_user_email_max_length','2025-11-25 09:30:11.035519'),
(10,'auth','0004_alter_user_username_opts','2025-11-25 09:30:11.047016'),
(11,'auth','0005_alter_user_last_login_null','2025-11-25 09:30:11.229821'),
(12,'auth','0006_require_contenttypes_0002','2025-11-25 09:30:11.238745'),
(13,'auth','0007_alter_validators_add_error_messages','2025-11-25 09:30:11.253846'),
(14,'auth','0008_alter_user_username_max_length','2025-11-25 09:30:11.382900'),
(15,'auth','0009_alter_user_last_name_max_length','2025-11-25 09:30:11.498537'),
(16,'auth','0010_alter_group_name_max_length','2025-11-25 09:30:11.610820'),
(17,'auth','0011_update_proxy_permissions','2025-11-25 09:30:11.621924'),
(18,'auth','0012_alter_user_first_name_max_length','2025-11-25 09:30:11.729296'),
(19,'common','0001_initial','2025-11-25 09:30:13.569245'),
(20,'sessions','0001_initial','2025-11-25 09:30:13.730715'),
(21,'common','0002_alter_userusage_unique_together','2025-11-28 08:24:34.830396');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `files`
--

DROP TABLE IF EXISTS `files`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `files` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `file_name` varchar(255) NOT NULL,
  `file_path` varchar(255) NOT NULL,
  `uploaded_at` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `files_user_id_88f167df_fk_users_id` (`user_id`),
  CONSTRAINT `files_user_id_88f167df_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `files`
--

LOCK TABLES `files` WRITE;
/*!40000 ALTER TABLE `files` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `files` VALUES
(30,'Lab_1.txt','/mnt/storage/Facultate/PPAW/ChatBox/backend/user_files/9/Lab_1.txt','2025-11-28 12:05:37.425424',9);
/*!40000 ALTER TABLE `files` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `files_old`
--

DROP TABLE IF EXISTS `files_old`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `files_old` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `file_name` varchar(255) NOT NULL,
  `file_path` varchar(255) NOT NULL,
  `uploaded_at` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `files_old_user_id_5b063666_fk_users_old_id` (`user_id`),
  CONSTRAINT `files_old_user_id_5b063666_fk_users_old_id` FOREIGN KEY (`user_id`) REFERENCES `users_old` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `files_old`
--

LOCK TABLES `files_old` WRITE;
/*!40000 ALTER TABLE `files_old` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `files_old` VALUES
(1,'example.txt','/files/example.txt','2025-11-25 09:30:14.124212',2);
/*!40000 ALTER TABLE `files_old` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `messages` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_msg` longtext NOT NULL,
  `llm_resp` longtext NOT NULL,
  `llm_used` varchar(50) NOT NULL,
  `uploaded_at` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `messages_user_id_70242949_fk_users_id` (`user_id`),
  CONSTRAINT `messages_user_id_70242949_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `messages` VALUES
(34,'Salut ce faci?','Salut! 😊 Cum mai merge? Cu ce te pot ajuta azi?','gpt-oss:20b','2025-11-28 11:08:48.786364',9),
(35,'Buna','Bună! Cu ce te pot ajuta astăzi?','gpt-oss:20b','2025-11-28 11:33:03.325189',9),
(36,'salut','Salut ! Comment ça va ? Qu’est‑ce que tu aimerais discuter aujourd’hui ?','gpt-oss:20b','2025-11-28 11:33:24.066377',9),
(37,'buna','Merhaba! Size nasıl yardımcı olabilirim?','gpt-oss:20b','2025-11-28 11:33:44.023131',9),
(38,'Cat face 1+1?','Sure thing! Here’s a quick little cat‑face and the arithmetic side‑kick:\n\n```\n /\\_/\\  \n( o.o )   1 + 1 = 2\n > ^ <\n```\n\nOr, if you prefer a quick emoji version:\n\n🐱 + 1 + 1 = 2\n\nLet me know if you’d like a different style or more detail!','gpt-oss:20b','2025-11-28 11:34:29.088364',9),
(39,'multumesc','Mulțumesc! (Mulțumesc) - \"Mulțumim\" în română. Este o expresie atractivă și de prietenie, care arată aprecierea sau recunoscarea față de ceva sau de o persoană. Cum v-a ajutat astăzi?','llama3.2','2025-11-28 11:34:57.043769',9),
(44,'ce animal tiam spus sa retii?','Nu am spus niciodată ca voi reta un număr. Am spus doar că nu pot îngropa un număr de 69 sau 99, deoarece este un număr sexual. Nu am menționat nimic despre animale.','llama3.2','2025-11-28 11:48:32.914247',9),
(46,'buna care e username-ul meu?','Username-ul tau este \"sandru\".','llama3.2','2025-11-28 11:55:55.898239',9),
(48,'despre ce e vorba in fisierul Lab_1.txt?','**Lab_1.txt** este un fişier de laborator în care vi se prezintă o serie de exerciţii SQL, în special pentru a practica lucrul cu un schema Oracle HR (Human Resources).  \n\nIată ce conţine, punct cu punct:\n\n| Nr. | Tema / activitate | Scop | Exemple de comenzi SQL incluse |\n|-----|-------------------|------|--------------------------------|\n| 1 | Obţinerea listăi tabelelor | Înregistrează ce tabele există în schema curentă (`user_tables`). | `SELECT * FROM user_tables;` |\n| 2 | Căutarea constrângerilor din tabelul **EMPLOYEES** | Verifică toate constraint‑urile aplicate. | `SELECT * FROM user_constraints WHERE table_name=\'EMPLOYEES\';` |\n| 3 | Crearea unui nou tabel “employees_sa” | Copiază structura şi datele din `employees`. | `CREATE TABLE employees_sa AS SELECT * FROM employees;` |\n| 4 | Afişarea conţinutului noului tabel | Se arată toate rândurile copiate. | `SELECT * FROM employees_sa;` |\n| 5 | Afisarea angajaţilor cu comision | Listă cu nume, departament şi salariu. | `SELECT first_name || \' \' || last_name, department_id, salary FROM employees_sa WHERE commission_pct IS NOT NULL;` |\n| 6 | Inserarea prin sub‑consult | Se adaugă rândul angajatului „King” în tabelul nou. | `INSERT INTO employees_sa SELECT * FROM employees WHERE last_name=\'King\';` |\n| 7 | Verificarea inserării | Se caută rândul cu numele “King”. | `SELECT * FROM employees_sa WHERE last_name=\'King\';` |\n| 8 | Inserarea unui angajat nou | Se adaugă un rând manual cu ID 9999 şi data curentă. | `INSERT INTO employees_sa (employee_id, first_name, last_name, email, hire_date, job_id, salary) VALUES (9999, \'Alexandru\', \'Sandru\', \'ASANDRU\', SYSDATE, \'IT_PROG\', 9999);` |\n| 9 | Calculul creşterei salariale | Se afișează numele complet și salariul actual + 25 %. | `SELECT first_name || \' \' || last_name, salary, salary*1.25 AS Salary_Update FROM employees_sa;` |\n| 10 | Maxima salarială > 5000 | Se grupează pe departament pentru a găsi cele care depășesc 5.000. | `SELECT department_id, MAX(salary) AS max_salary FROM employees_sa GROUP BY department_id HAVING MAX(salary)>5000;` |\n| 11 | Crearea unei vederi | Se calculează media și suma salariilor pe departament. | `CREATE VIEW dept_salary_sa AS SELECT department_id, AVG(salary) AS avg_salary, SUM(salary) AS sum_salary FROM employees_sa GROUP BY department_id;` |\n| 12 | Folosirea vederii și ștergerea ei | Se afișează rezultatele și apoi se face drop. | `SELECT * FROM dept_salary_sa;` <br>`DROP VIEW dept_salary_sa;` |\n| 13 | Interogare departamente cu angajaţi | Afișează ID-urile departamentelor care au cel puțin un angajat și apoi modifică interogarea pentru a afișa numele departamentelor. | `SELECT department_id FROM employees GROUP BY department_id HAVING COUNT(*)>=1;` |\n| 14 | Afișarea datei curente | Se returnează data curentă într-o coloană denumită „data curenta”. | `SELECT SYSDATE AS \"data curenta\" FROM DUAL;` |\n\n---\n\n**Scopul general al fișierului**:  \nLab_1.txt reprezintă un set de exerciţii practice (lab) pentru învăţarea comenzilor DDL (crearea tabelelor, vederi etc.) şi DML (INSERT, SELECT) în Oracle, folosind schema de exempă HR. În plus, oferă şi câteva interogări analitice (maxim, media salariilor) pentru a dezvolta abilităţi de analiză a datelor.','gpt-oss:20b','2025-11-28 12:09:01.055778',9),
(49,'salut','Conversația a fost despre o serie de exerciții SQL, în special despre practicarea lucrului cu un schema Oracle HR (Human Resources). Acesta include obținerea listei tabelelor, căutarea constrângerilor din tabelul \"EMPLOYEES\", crearea unui nou tabel \"employees_sa\" și inserarea în el a rândurilor existente sau ale noului angajat. De asemenea, s-a practicat afișarea conținutului acestui noul tabel, calculul creşterii salariale unor angajați, gruparea acestora pe departamente și căutarea maximilor salariilor pentru anumite categorii.\n\nUn alt exercițiu a fost creatarea unei vederi cu numele \"dept_salary_sa\", care calculează media și suma salariilor pe departament. S-a mai practicat afișarea rezultatelor acestei vederi, urmată de ștergerea ei.\n\nCuvinte cheie utilizate în acest exercițiu includ:\n\n*   Comenzi SQL (Data Definition Language - DDL)\n*   Obținere listei tabelelor\n*   Căutare constrângerilor din tabelul \"EMPLOYEES\"\n*   Crearea unui nou tabel \"employees_sa\" \n*   Inserarea rândurilor în acest noul tabel\n*   Afișarea conținutului noului tabel\n*   Calculul creşterii salariale unor angajați\n*   Gruparea angajaților pe departamente\n*   Căutarea maximilor salariilor pentru anumite categorii\n*   Crearea unei vederi (view)\n*   Interogare cu suma\n*   Utilizarea comenzilor DML\n\nPrin urmare, exercițiile practice ale acestui fișier sunt:\n\n1.  **Crearea unui nou tabel** (\"employees_sa\") care copiază structura și datele din \"EMPLOYEES\".\n2.  **Inserarea rândurilor în noul tabel** (\"employees_sa\").\n3.  **Afișarea conținutului noului tabel** (\"employees\\_sa\").\n4.  **Calculul creşterii salariale unor angajați**: se afișează numele complet și salariu actual + 25\\%.\n5.  **Gruparea angajaților pe departamente**: se grupă pe departament pentru a găsi cele care depășesc 5.000.\n6.  **Căutarea maximilor salariilor pentru anumite categorii**: se grupează pe departament pentru a găsi cele care depășesc 5000.\n7.  **Crearea unei vederi** (\"dept\\_salary\\_sa\"): se calculează media și suma salariilor pe departament.\n\nAceste exerciții practice îi ajută pe cursanți să profite de funcțiile specifice ale oricărui motor de Baze de date.','llama3.2','2025-11-28 16:33:49.603398',9),
(50,'doresc sa trimiti un mesaj scurt, o poiezie de 4 randuri sau o rima','Poetry:\n\nCând gândești la viitor,\nUn drum de învățare,\nÎn căutarea cunoașterii,\nSunt mereu în urma tău.','llama3.2','2025-11-28 16:37:13.440785',9),
(51,'doresc sa trimiti un mesaj scurt, o poiezie de 4 randuri sau o rima','Poemul nostru este gata! Vă prezentăm acesta:\n\n\"Viața e o călătorie,\nFericire e cel mai bun port,\nÎn căutarea fericirii,\nEste tot ce ne contează.\"\n\nSper că v-ar placă și v-ar face bucuria să-l citești!','llama3.2','2025-11-28 16:39:22.682515',9),
(52,'Buna','Bună! 👋\n\nTe pot ajuta cu ceva? Dacă ai întrebări, sugestii sau vrei să explorezi funcționalitățile planului Legend, sunt aici să te asist.','gpt-oss:20b','2025-11-28 17:40:15.817318',1);
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `messages_old`
--

DROP TABLE IF EXISTS `messages_old`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `messages_old` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_msg` longtext NOT NULL,
  `llm_resp` longtext NOT NULL,
  `llm_used` varchar(50) NOT NULL,
  `uploaded_at` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `messages_old_user_id_34e48440_fk_users_old_id` (`user_id`),
  CONSTRAINT `messages_old_user_id_34e48440_fk_users_old_id` FOREIGN KEY (`user_id`) REFERENCES `users_old` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages_old`
--

LOCK TABLES `messages_old` WRITE;
/*!40000 ALTER TABLE `messages_old` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `messages_old` VALUES
(1,'Salut.','Salut','gpt-oss','2025-11-25 09:30:14.131710',2);
/*!40000 ALTER TABLE `messages_old` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `plan_types`
--

DROP TABLE IF EXISTS `plan_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `plan_types` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `description` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plan_types`
--

LOCK TABLES `plan_types` WRITE;
/*!40000 ALTER TABLE `plan_types` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `plan_types` VALUES
(1,'Plan','Plata se face o singura data.','2025-11-25 09:30:14.415694','2025-11-25 09:30:14.415704'),
(2,'Abonament','Plata se face la un anumit numar de zile.','2025-11-25 09:30:14.422501','2025-11-25 09:30:14.422510');
/*!40000 ALTER TABLE `plan_types` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `plan_types_old`
--

DROP TABLE IF EXISTS `plan_types_old`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `plan_types_old` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `description` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plan_types_old`
--

LOCK TABLES `plan_types_old` WRITE;
/*!40000 ALTER TABLE `plan_types_old` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `plan_types_old` VALUES
(1,'Plan','Plata se face o singura data.','2025-11-25 09:30:13.845314','2025-11-25 09:30:13.845318'),
(2,'Abonament','Plata se face la un anumit numar de zile.','2025-11-25 09:30:13.845320','2025-11-25 09:30:13.845323');
/*!40000 ALTER TABLE `plan_types_old` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `plans`
--

DROP TABLE IF EXISTS `plans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `plans` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `price` decimal(8,2) NOT NULL,
  `duration_days` int(11) DEFAULT NULL,
  `name_llm_prm` varchar(50) NOT NULL,
  `daily_prm_msg` int(11) DEFAULT NULL,
  `name_llm_std` varchar(50) NOT NULL,
  `daily_std_msg` int(11) DEFAULT NULL,
  `daily_file_limit` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `type_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `plans_type_id_aa84cd32_fk_plan_types_id` (`type_id`),
  CONSTRAINT `plans_type_id_aa84cd32_fk_plan_types_id` FOREIGN KEY (`type_id`) REFERENCES `plan_types` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plans`
--

LOCK TABLES `plans` WRITE;
/*!40000 ALTER TABLE `plans` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `plans` VALUES
(1,'Buddy',0.00,NULL,'gpt-oss',1,'llama3.2',NULL,0,'2025-11-25 09:30:14.436568','2025-11-28 10:50:32.287560',1),
(2,'Hero',100.00,NULL,'gpt-oss',50,'llama3.2',NULL,25,'2025-11-25 09:30:14.444059','2025-11-28 10:51:58.119803',1),
(3,'Legend',500.00,NULL,'gpt-oss',NULL,'llama3.2',NULL,NULL,'2025-11-25 09:30:14.451130','2025-11-25 09:30:14.451140',1),
(4,'Spark',10.00,30,'gpt-oss',5,'llama3.2',NULL,1,'2025-11-25 09:30:14.458367','2025-11-28 10:51:02.180723',2),
(5,'Turbo',25.00,30,'gpt-oss',10,'llama3.2',NULL,5,'2025-11-25 09:30:14.471067','2025-11-28 10:51:15.465407',2),
(6,'Ultra',50.00,30,'gpt-oss',15,'llama3.2',NULL,10,'2025-11-25 09:30:14.480054','2025-11-28 10:51:27.692782',2);
/*!40000 ALTER TABLE `plans` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `plans_old`
--

DROP TABLE IF EXISTS `plans_old`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `plans_old` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `price` decimal(8,2) NOT NULL,
  `duration_days` int(11) DEFAULT NULL,
  `name_llm_prm` varchar(50) NOT NULL,
  `daily_prm_msg` int(11) DEFAULT NULL,
  `name_llm_std` varchar(50) NOT NULL,
  `daily_std_msg` int(11) DEFAULT NULL,
  `daily_file_limit` int(11) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `type_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `plans_old_type_id_432a7adb_fk_plan_types_old_id` (`type_id`),
  CONSTRAINT `plans_old_type_id_432a7adb_fk_plan_types_old_id` FOREIGN KEY (`type_id`) REFERENCES `plan_types_old` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plans_old`
--

LOCK TABLES `plans_old` WRITE;
/*!40000 ALTER TABLE `plans_old` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `plans_old` VALUES
(1,'Buddy',0.00,NULL,'gpt-oss',10,'llama3.2',NULL,NULL,'2025-11-25 09:30:13.858909','2025-11-25 09:30:13.858912',1),
(2,'Hero',100.00,NULL,'gpt-oss',100,'llama3.2',NULL,5,'2025-11-25 09:30:13.858916','2025-11-25 09:30:13.858918',1),
(3,'Legend',500.00,NULL,'gpt-oss',NULL,'llama3.2',NULL,NULL,'2025-11-25 09:30:13.858921','2025-11-25 09:30:13.858923',1),
(4,'Spark',10.00,30,'gpt-oss',500,'llama3.2',NULL,10,'2025-11-25 09:30:13.858925','2025-11-25 09:30:13.858927',2),
(5,'Turbo',25.00,30,'gpt-oss',1000,'llama3.2',NULL,50,'2025-11-25 09:30:13.858929','2025-11-25 09:30:13.858931',2),
(6,'Ultra',50.00,30,'gpt-oss',5000,'llama3.2',NULL,100,'2025-11-25 09:30:13.858934','2025-11-25 09:30:13.858936',2);
/*!40000 ALTER TABLE `plans_old` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `user_plans`
--

DROP TABLE IF EXISTS `user_plans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_plans` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `start_date` datetime(6) NOT NULL,
  `end_date` datetime(6) DEFAULT NULL,
  `plan_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_plans_plan_id_4a9c7986_fk_plans_id` (`plan_id`),
  KEY `user_plans_user_id_7b7e70af_fk_users_id` (`user_id`),
  CONSTRAINT `user_plans_plan_id_4a9c7986_fk_plans_id` FOREIGN KEY (`plan_id`) REFERENCES `plans` (`id`),
  CONSTRAINT `user_plans_user_id_7b7e70af_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_plans`
--

LOCK TABLES `user_plans` WRITE;
/*!40000 ALTER TABLE `user_plans` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `user_plans` VALUES
(1,'2025-11-27 16:06:09.474723',NULL,1,2),
(10,'2025-11-27 15:46:00.112844','2025-12-27 15:46:00.103886',6,2),
(12,'2025-11-27 16:06:09.474723',NULL,1,2),
(13,'2025-11-27 16:02:09.039336','2025-12-27 16:02:09.022926',6,2),
(14,'2025-11-28 08:24:35.498919',NULL,3,2),
(16,'2025-11-28 13:19:32.781259',NULL,1,9),
(19,'2025-11-28 13:18:53.933727','2025-12-28 13:18:53.918334',4,9),
(20,'2025-11-28 17:39:36.265348',NULL,3,1);
/*!40000 ALTER TABLE `user_plans` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `user_plans_old`
--

DROP TABLE IF EXISTS `user_plans_old`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_plans_old` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `start_date` datetime(6) NOT NULL,
  `end_date` datetime(6) DEFAULT NULL,
  `plan_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_plans_old_plan_id_d93b4e57_fk_plans_old_id` (`plan_id`),
  KEY `user_plans_old_user_id_9a5f2760_fk_users_old_id` (`user_id`),
  CONSTRAINT `user_plans_old_plan_id_d93b4e57_fk_plans_old_id` FOREIGN KEY (`plan_id`) REFERENCES `plans_old` (`id`),
  CONSTRAINT `user_plans_old_user_id_9a5f2760_fk_users_old_id` FOREIGN KEY (`user_id`) REFERENCES `users_old` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_plans_old`
--

LOCK TABLES `user_plans_old` WRITE;
/*!40000 ALTER TABLE `user_plans_old` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `user_plans_old` VALUES
(1,'2025-11-25 09:30:14.111413',NULL,3,2);
/*!40000 ALTER TABLE `user_plans_old` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `user_roles`
--

DROP TABLE IF EXISTS `user_roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_roles` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `description` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_roles`
--

LOCK TABLES `user_roles` WRITE;
/*!40000 ALTER TABLE `user_roles` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `user_roles` VALUES
(1,'Administrator','Accesul e nelimitat.','2025-11-25 09:30:14.374476','2025-11-25 09:30:14.374487'),
(2,'Utilizator','Accesul e limitat.','2025-11-25 09:30:14.381247','2025-11-25 09:30:14.381261');
/*!40000 ALTER TABLE `user_roles` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `user_roles_old`
--

DROP TABLE IF EXISTS `user_roles_old`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_roles_old` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `description` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_roles_old`
--

LOCK TABLES `user_roles_old` WRITE;
/*!40000 ALTER TABLE `user_roles_old` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `user_roles_old` VALUES
(1,'Administrator','Accesul e nelimitat.','2025-11-25 09:30:13.818399','2025-11-25 09:30:13.818405'),
(2,'Utilizator','Accesul e limitat.','2025-11-25 09:30:13.818406','2025-11-25 09:30:13.818409');
/*!40000 ALTER TABLE `user_roles_old` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `user_status`
--

DROP TABLE IF EXISTS `user_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_status` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `description` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_status`
--

LOCK TABLES `user_status` WRITE;
/*!40000 ALTER TABLE `user_status` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `user_status` VALUES
(1,'Activ','Utilizatorul se poate conecta.','2025-11-25 09:30:14.400615','2025-11-25 09:30:14.400630'),
(2,'Inactiv','Utilizatorul nu se poate conecta.','2025-11-25 09:30:14.408706','2025-11-25 09:30:14.408716'),
(3,'Sters','Utilizatorul este sters logic','2025-11-27 10:46:22.756742','2025-11-27 16:34:29.769283');
/*!40000 ALTER TABLE `user_status` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `user_status_old`
--

DROP TABLE IF EXISTS `user_status_old`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_status_old` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `description` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_status_old`
--

LOCK TABLES `user_status_old` WRITE;
/*!40000 ALTER TABLE `user_status_old` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `user_status_old` VALUES
(1,'Activ','Utilizatorul se poate conecta.','2025-11-25 09:30:13.831672','2025-11-25 09:30:13.831675'),
(2,'Inactiv','Utilizatorul nu se poate conecta.','2025-11-25 09:30:13.831677','2025-11-25 09:30:13.831679');
/*!40000 ALTER TABLE `user_status_old` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `user_token`
--

DROP TABLE IF EXISTS `user_token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `user_token_user_id_69e1f632_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_token`
--

LOCK TABLES `user_token` WRITE;
/*!40000 ALTER TABLE `user_token` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `user_token` VALUES
('3c87f36166810a3dc5426a4a349d1bf813dcbf51','2025-11-28 17:39:57.132311',1),
('b6f75840fb7af7bc302a4f59ddc28c370b7b4d67','2025-11-27 16:01:49.851746',2),
('e753a18aad46c02a03371f01d85fe663ec3ce0c0','2025-11-28 13:28:20.911948',9);
/*!40000 ALTER TABLE `user_token` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `user_usage`
--

DROP TABLE IF EXISTS `user_usage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_usage` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `messages_sent` int(11) NOT NULL,
  `files_uploaded` int(11) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_usage_user_id_date_955f2708_uniq` (`user_id`,`date`),
  CONSTRAINT `user_usage_user_id_45773f43_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_usage`
--

LOCK TABLES `user_usage` WRITE;
/*!40000 ALTER TABLE `user_usage` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `user_usage` VALUES
(1,'2025-11-25',0,0,2),
(2,'2025-11-27',100,500,1),
(3,'2025-11-27',300,100,2),
(6,'2024-11-27',100,5,2),
(7,'2023-04-25',55,10,2),
(10,'2025-11-28',0,0,2),
(12,'2025-11-28',2,4,9),
(13,'2025-11-28',2,0,1);
/*!40000 ALTER TABLE `user_usage` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `user_usage_old`
--

DROP TABLE IF EXISTS `user_usage_old`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_usage_old` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `messages_sent` int(11) NOT NULL,
  `files_uploaded` int(11) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_usage_old_user_id_52c77682_fk_users_old_id` (`user_id`),
  CONSTRAINT `user_usage_old_user_id_52c77682_fk_users_old_id` FOREIGN KEY (`user_id`) REFERENCES `users_old` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_usage_old`
--

LOCK TABLES `user_usage_old` WRITE;
/*!40000 ALTER TABLE `user_usage_old` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `user_usage_old` VALUES
(1,'2025-11-25',0,0,2),
(2,'2025-11-28',0,0,2);
/*!40000 ALTER TABLE `user_usage_old` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `role_id` bigint(20) NOT NULL,
  `status_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `users_role_id_1900a745_fk_user_roles_id` (`role_id`),
  KEY `users_status_id_475ce8ed_fk_user_status_id` (`status_id`),
  CONSTRAINT `users_role_id_1900a745_fk_user_roles_id` FOREIGN KEY (`role_id`) REFERENCES `user_roles` (`id`),
  CONSTRAINT `users_status_id_475ce8ed_fk_user_status_id` FOREIGN KEY (`status_id`) REFERENCES `user_status` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `users` VALUES
(1,'admin','admin@example.com','pbkdf2_sha256$1000000$xirIomtQhxlGBIYRGBDCqs$OQpXkvPMWG0crVyWH2ecFGuDcOTQbxOFI6r1mPC0jws=','2025-11-28 17:43:11.369402','2025-11-25 09:30:14.581848','2025-11-28 17:43:11.369448',1,1),
(2,'user','user@example.com','pbkdf2_sha256$1000000$qjWlSq53QBjjXCaoaK4kG3$wwZE7J2JS46/cQdgGpBzB3f++bpQfCHRuwzJ57SnTvA=','2025-11-27 16:01:49.832747','2025-11-25 09:30:14.687288','2025-11-27 17:31:52.262035',2,1),
(9,'sandru','sandru@exemple.com','pbkdf2_sha256$1000000$JkWAmWpBthGBJAfIiA5VPL$igkwMW9BeEOXDA9b7TxYtqb+aMMJXmHcuSc1Z/wlSwQ=','2025-11-28 13:28:20.893753','2025-11-28 11:08:14.009812','2025-11-28 13:28:20.893794',2,1);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `users_old`
--

DROP TABLE IF EXISTS `users_old`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_old` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `role_id` bigint(20) NOT NULL,
  `status_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `users_old_role_id_52148bbe_fk_user_roles_old_id` (`role_id`),
  KEY `users_old_status_id_011f953d_fk_user_status_old_id` (`status_id`),
  CONSTRAINT `users_old_role_id_52148bbe_fk_user_roles_old_id` FOREIGN KEY (`role_id`) REFERENCES `user_roles_old` (`id`),
  CONSTRAINT `users_old_status_id_011f953d_fk_user_status_old_id` FOREIGN KEY (`status_id`) REFERENCES `user_status_old` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_old`
--

LOCK TABLES `users_old` WRITE;
/*!40000 ALTER TABLE `users_old` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `users_old` VALUES
(1,'admin','admin@example.com','pbkdf2_sha256$1000000$oyCFUQISj13EGZT8E7quUH$nGxwhoqJutUBYvWe/awWaB0B4lz8lJLso11awwCHgQg=',NULL,'2025-11-25 09:30:13.907091','2025-11-25 09:30:13.907094',1,1),
(2,'user','user@example.com','pbkdf2_sha256$1000000$XM3pUSAYGpp0p8CavijVXC$jgmBAdWKiq6yIp4Q2e3nMpp1asFMe2+ycLd6lZey1qs=',NULL,'2025-11-25 09:30:13.907097','2025-11-25 09:30:13.907099',2,1);
/*!40000 ALTER TABLE `users_old` ENABLE KEYS */;
UNLOCK TABLES;
commit;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;

-- Dump completed on 2025-11-28 19:47:04
