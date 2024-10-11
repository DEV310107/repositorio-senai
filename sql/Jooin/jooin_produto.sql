-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: jooin
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.32-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `produto`
--

DROP TABLE IF EXISTS `produto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `produto` (
  `id` int(3) NOT NULL AUTO_INCREMENT,
  `nome` varchar(20) DEFAULT NULL,
  `marca` varchar(20) DEFAULT NULL,
  `empresa` int(3) DEFAULT NULL,
  `estoque` int(5) DEFAULT NULL,
  `valor_bruto` float DEFAULT NULL,
  `imposto` float DEFAULT NULL,
  `margem_lucro` float DEFAULT NULL,
  `valor_final` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `empresa` (`empresa`),
  CONSTRAINT `produto_ibfk_1` FOREIGN KEY (`empresa`) REFERENCES `empresa` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produto`
--

LOCK TABLES `produto` WRITE;
/*!40000 ALTER TABLE `produto` DISABLE KEYS */;
INSERT INTO `produto` VALUES (1,'Smartwatch','WristTech',1,80,150,0.06,0.25,198.75),(2,'Tablet','TouchPad',2,70,300,0.08,0.2,388.8),(3,'Câmera','SnapLens',3,90,250,0.07,0.22,326.35),(4,'Impressora','PrintTech',4,60,200,0.05,0.18,247.8),(5,'Monitor','ViewScreen',5,40,180,0.04,0.15,215.28),(6,'Caixa de Som','SoundWave',6,120,80,0.03,0.2,98.88),(7,'Roteador','NetLink',7,95,70,0.02,0.25,89.25),(8,'Webcam','EyeSee',8,75,45,0.01,0.15,52.2675),(9,'HD Externo','DataVault',1,110,120,0.03,0.18,145.848),(10,'Carregador Portátil','PowerUp',2,130,25,0.02,0.2,30.6),(11,'Cabo USB','LinkCable',3,140,10,0.01,0.15,11.615),(12,'Hub USB','ConnectAll',4,105,15,0.01,0.18,17.877),(13,'Adaptador HDMI','ScreenLink',5,85,20,0.01,0.2,24.24),(14,'Case para HD','SafeCase',6,100,8,0.005,0.15,9.246),(15,'Cooler para Notebook','CoolDown',7,65,12,0.005,0.2,14.472),(16,'Pendrive','DataDrive',8,115,18,0.005,0.18,21.3462),(17,'Placa de Vídeo','Graphix',1,45,300,0.07,0.3,417.3),(18,'Memória RAM','SpeedRAM',2,55,80,0.03,0.25,103),(19,'Processador','SpeedCore',3,50,600,0.06,0.35,600),(20,'Placa-Mãe','CoreBoard',4,30,150,0.05,0.3,204.75),(21,'Mesa','TOPTOP',5,800,155,0.099,0.6,272.552);
/*!40000 ALTER TABLE `produto` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-02 10:23:05
