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
-- Table structure for table `empresa`
--

DROP TABLE IF EXISTS `empresa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empresa` (
  `id` int(3) NOT NULL AUTO_INCREMENT,
  `nome` varchar(20) DEFAULT NULL,
  `nome_fantasia` varchar(20) DEFAULT NULL,
  `cnpj` float DEFAULT NULL,
  `endereco` varchar(50) DEFAULT NULL,
  `cidade` varchar(20) DEFAULT NULL,
  `estado` varchar(20) DEFAULT NULL,
  `pais` varchar(20) DEFAULT NULL,
  `telefone_01` float DEFAULT NULL,
  `telefone_02` float DEFAULT NULL,
  `celular` float DEFAULT NULL,
  `representante` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empresa`
--

LOCK TABLES `empresa` WRITE;
/*!40000 ALTER TABLE `empresa` DISABLE KEYS */;
INSERT INTO `empresa` VALUES (1,'Empresa da Trapalhad','Trapalhada Inc.',98765400000000,'Avenida da Confusão, 456','Bagunçópolis','Confusão','Desordemlândia',5551230000,5559880000,5553330000,'Sr. Desastre'),(2,'Empresa dos Problema','Problemas Corp.',12345700000000,'Rua dos Erros, 789','Caosville','Incerto','Desenrolândia',4449880000,4445560000,4442220000,'Sra. Engano'),(3,'Fábrica da Confusão ','Confusion Factory',55555600000000,'Estrada da Desorganização, 123','Desajustópolis','Descontrole','Desarrumação',6661110000,6664450000,6667780000,'Dr. Caos'),(4,'Empresa do Caos Ltda','Caos e Cia.',65498700000000,'Rua da Desordem, 789','Desregulópolis','Desorganização','Descontroslândia',7778890000,7776670000,7773330000,'Sr. Bagunça'),(5,'Indústria do Equívoc','Equívoco Ind.',78965400000000,'Avenida do Engano, 456','Desorientópolis','Desgovernado','Desconhecido',8889990000,8882220000,8884450000,'Sra. Engano'),(6,'Empresa da Bagunça &','Bagunça Ltda.',99988900000000,'Travessa da Desordem, 789','Bagunçalândia','Bagunçado','Bagunçalândia',7774450000,7772230000,7773340000,'Sr. Confusão'),(7,'Companhia do Descont','Descontrole Corp.',32165500000000,'Rua do Descontrole, 123','Desatino','Desregrado','Descompasso',5556670000,5558890000,5551110000,'Sr. Caos'),(8,'Familia Senai Ltda.','Odio Descontrolado.',1233210000000,'Rua Roberto Manje, 3000','Jundiai','São Paulo','Brasil',5556670000,5558880000,5551120000,'Sr. Carlos'),(9,'Dev. Sistemas Corp.','Tech Informatica.',1233210000000,'Rua Roberto Manje, 3000','Jundiai','São Paulo','Brasil',5556670000,5558880000,5551120000,'Sr. Jamal');
/*!40000 ALTER TABLE `empresa` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-02 10:23:06
