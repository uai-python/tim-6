-- MySQL dump 10.13  Distrib 5.7.9, for Win64 (x86_64)
--
-- Host: localhost    Database: webq
-- ------------------------------------------------------
-- Server version	5.7.10-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `guest`
--

DROP TABLE IF EXISTS `guest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `guest` (
  `idguess` int(11) NOT NULL AUTO_INCREMENT,
  `usia` int(11) NOT NULL,
  `jenis_kelamin` varchar(15) NOT NULL,
  `kota` varchar(45) NOT NULL,
  `user` varchar(45) NOT NULL,
  PRIMARY KEY (`idguess`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `guest`
--

LOCK TABLES `guest` WRITE;
/*!40000 ALTER TABLE `guest` DISABLE KEYS */;
INSERT INTO `guest` VALUES (2,22,'Laki - Laki','Jakarta Selatan','iqbal'),(3,23,'Laki - Laki','Jakarta Utara','blink'),(4,22,'Laki - Laki','Jakarta Selatan','iqbal'),(5,18,'Laki - Laki','Jakarta Selatan','iqbalas'),(6,24,'Laki - Laki','Jakarta Selatan','blink'),(7,23,'Laki - Laki','Jakarta Selatan','kaskus'),(8,43,'Laki - Laki','Jakarta Selatan','hilmi'),(9,12,'Laki - Laki','Jakarta Selatan','blinkbink'),(10,23,'Laki - Laki','Jakarta Selatan','dewa'),(11,12,'Laki - Laki','Jakarta Selatan','kaskusasdasd'),(12,1,'Perempuan','Jakarta Barat','hilmi'),(13,32,'Laki - Laki','Jakarta Selatan','ganool'),(14,21,'Lainnya','Jakarta Selatan','Nanang'),(15,19,'Laki - Laki','Jakarta Selatan','dimas'),(16,19,'Laki - Laki','Jakarta Selatan','dimas'),(17,12,'Laki - Laki','Jakarta Selatan','ag'),(18,33,'Laki - Laki','Jakarta Selatan','nanang'),(19,23,'Laki - Laki','Jakarta Selatan','gininih'),(20,12,'Laki - Laki','Jakarta Selatan','cius'),(21,12,'Perempuan','Jakarta Selatan','bljn'),(22,23,'Laki - Laki','Jakarta Selatan','as'),(23,23,'Laki - Laki','Jakarta Selatan','asasd'),(24,1,'Laki - Laki','Jakarta Selatan','asd'),(25,12,'Laki - Laki','Jakarta Selatan','kaskus'),(26,23,'Laki - Laki','Jakarta Selatan','inul'),(27,12313,'Perempuan','Jakarta Utara','asdasd'),(28,12,'Laki - Laki','Jakarta Selatan','askjda'),(29,2,'Laki - Laki','Jakarta Selatan','akjb'),(30,12,'Laki - Laki','Jakarta Selatan','asd'),(31,33,'Laki - Laki','Jakarta Selatan','as'),(32,22,'Laki - Laki','Jakarta Selatan','mahaba'),(33,12,'Laki - Laki','Jakarta Selatan','ga'),(34,12,'Laki - Laki','Jakarta Selatan','hore'),(35,12,'Perempuan','Jakarta Utara','irel'),(36,18,'Laki - Laki','Jakarta Selatan','dimas'),(37,78,'Laki - Laki','Jakarta Selatan','hjhj'),(38,89,'Laki - Laki','Jakarta Selatan','gih'),(39,19,'Laki - Laki','Jakarta Selatan','galak'),(40,25,'Laki - Laki','Jakarta Selatan','kurnia'),(41,12,'Perempuan','Jakarta Selatan','blinkbinka');
/*!40000 ALTER TABLE `guest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question`
--

DROP TABLE IF EXISTS `question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `question` (
  `idquestion` int(11) NOT NULL AUTO_INCREMENT,
  `question` longtext NOT NULL,
  `answer` varchar(30) NOT NULL,
  PRIMARY KEY (`idquestion`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question`
--

LOCK TABLES `question` WRITE;
/*!40000 ALTER TABLE `question` DISABLE KEYS */;
INSERT INTO `question` VALUES (1,'Jumlah Kematian Akibat Bunuh Diri ditahun 2015 ?','16'),(2,'Berapakah angka pengguna penyalahgunaan narkotika di daerah Jakarta Selatan ?','465'),(3,'Berapa jumlah guru SD Perempuan di Jakarta Timur pada tahun 2015 ?','8898'),(4,'Jumlah siswa SMK putus sekolah di jakarta Timur ?','430'),(5,'Penyebab Kematian Ibu DKI Jakarta ?','1'),(6,'Jumlah Halte Busway DKI Jakarta Pada Tahun 2011 ? ','207'),(7,'jumlah truk sampah jakarta timur pada tahun 2011','165'),(8,'jumlah migrasi dari luar kota ke tanah abang','1093'),(9,'jumlah laki-laki yang berstatus belum kawin daerah menteng 2015','12923'),(10,'jumlah pengunjung perpustakaan kuningan','13529'),(11,'produksi sampah pada daerah jakarta tmur dalam sehari (TON)','1487'),(12,'jumlah kematian laki-laki akibat kecelakaan pada Provinsi DKI JAKARTA','401'),(13,'jumlah guru sd perempuan daerah jakarta timur','8898'),(14,'jumlah guru sma perempuan daerah jakarta pusat','761'),(15,'jumlah kematian akibat melahirkan tahun 2015','6');
/*!40000 ALTER TABLE `question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quiz`
--

DROP TABLE IF EXISTS `quiz`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `quiz` (
  `idquiz` int(11) NOT NULL AUTO_INCREMENT,
  `user` varchar(45) NOT NULL,
  `jumlah_soal` varchar(45) NOT NULL,
  `WaktuMasuk` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `WaktuAkhir` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `score` varchar(45) NOT NULL,
  PRIMARY KEY (`idquiz`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quiz`
--

LOCK TABLES `quiz` WRITE;
/*!40000 ALTER TABLE `quiz` DISABLE KEYS */;
INSERT INTO `quiz` VALUES (1,'blinkbinka','11','2017-04-05 13:08:20','2017-04-05 13:08:20',''),(2,'blinkbinka','11','2017-04-05 13:23:04','2017-04-05 13:23:04','0');
/*!40000 ALTER TABLE `quiz` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-04-05 20:38:09
