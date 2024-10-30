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
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente` (
  `id` int(3) NOT NULL AUTO_INCREMENT,
  `nome` varchar(20) DEFAULT NULL,
  `cpf` float DEFAULT NULL,
  `data_nascimento` int(8) DEFAULT NULL,
  `celular` float DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `item_comprado` int(3) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `item_comprado` (`item_comprado`),
  CONSTRAINT `cliente_ibfk_1` FOREIGN KEY (`item_comprado`) REFERENCES `produto` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` VALUES (1,'João Silva',12345700000,19900101,11987700000,'joao@example.com',1),(2,'Maria Santos',98765400000,19851225,11888900000,'maria@example.com',2),(3,'Carlos Oliveira',45678900000,19780315,11777800000,'carlos@example.com',3),(4,'Ana Souza',12309900000,19870228,12000000000,'ana@example.com',4),(5,'Pedro Lima',54321700000,19930415,11666700000,'pedro@example.com',5),(6,'Juliana Pereira',98712300000,19801020,115,'juliana@example.com',6),(7,'Mariana Castro',65498700000,19850912,11444400000,'mariana@example.com',7),(8,'Fernando Santos',98765400000,19820507,11333300000,'fernando@example.com',8),(9,'Lucas Oliveira',45632200000,19890730,11222200000,'lucas@example.com',9),(10,'Gabriela Silva',32198800000,19980125,11888900000,'gabriela@example.com',10),(11,'Bruno Souza',12365500000,19841218,11777800000,'bruno@example.com',11),(12,'Patrícia Lima',98745600000,19800210,11666700000,'patricia@example.com',12),(13,'Rafaela Pereira',65412400000,19900905,115,'rafaela@example.com',13),(14,'Thiago Castro',32179000000,19760703,11444400000,'thiago@example.com',14),(15,'Vanessa Santos',78965400000,19890115,11333300000,'vanessa@example.com',15),(16,'Rodrigo Oliveira',98765400000,19811228,11222200000,'rodrigo@example.com',16),(17,'Camila Silva',45678900000,19950410,11888900000,'camila@example.com',17),(18,'Diego Souza',12398700000,19830807,11777800000,'diego@example.com',18),(19,'Aline Lima',98765400000,19921120,11666700000,'aline@example.com',19),(20,'Marcela Pereira',65432200000,19790415,115,'marcela@example.com',20),(21,'Roberto Castro',32165500000,19860518,11444400000,'roberto@example.com',1),(22,'Laura Santos',78912400000,19930928,11333300000,'laura@example.com',2),(23,'Gustavo Oliveira',98765400000,19800710,11222200000,'gustavo@example.com',3),(24,'Isabela Silva',45698700000,19850105,11888900000,'isabela@example.com',4),(25,'Ricardo Souza',12379000000,19980320,11777800000,'ricardo@example.com',5),(26,'Tatiane Lima',98745600000,19730815,11666700000,'tatiane@example.com',6),(27,'Vinícius Pereira',65412400000,19870910,115,'vinicius@example.com',7),(28,'Carolina Castro',32198800000,19801103,11444400000,'carolina@example.com',8),(29,'Luiz Santos',78932200000,19911028,11333300000,'luiz@example.com',9),(30,'Nathália Oliveira',98765400000,19760214,11222200000,'nathalia@example.com',10),(31,'Paulo Silva',45678900000,19840430,11888900000,'paulo@example.com',11),(32,'Fernanda Souza',12365500000,19920405,11777800000,'fernanda@example.com',12),(33,'André Lima',98712300000,19820908,11666700000,'andre@example.com',13),(34,'Beatriz Pereira',65498700000,19780923,115,'beatriz@example.com',14),(35,'José Castro',32179000000,19951210,11444400000,'jose@example.com',15),(36,'Sandra Santos',78965400000,19821205,11333300000,'sandra@example.com',16),(37,'Leandro Oliveira',98765400000,19770818,11222200000,'leandro@example.com',17),(38,'Cristina Silva',45632200000,19931007,11888900000,'cristina@example.com',18),(39,'Daniel Souza',12365500000,19860412,11777800000,'daniel@example.com',19),(40,'Renata Lima',98745600000,19910417,11666700000,'renata@example.com',20),(41,'Luciana Pereira',65412400000,19721030,115,'luciana@example.com',21),(42,'Marcos Castro',32165400000,19890525,11444400000,'marcos@example.com',21),(43,'Simone Santos',78912400000,19830518,11333300000,'simone@example.com',3),(44,'Henrique Oliveira',98765400000,19980410,11222200000,'henrique@example.com',4),(45,'Catarina Silva',45698700000,19810715,11888900000,'catarina@example.com',5),(46,'Lucas Souza',12379000000,19761020,11777800000,'lucas@example.com',6),(47,'Mariana Lima',98745600000,19941205,11666700000,'mariana@example.com',7),(48,'Diego Pereira',65412400000,19800308,115,'diego@example.com',8),(49,'Carla Castro',32198800000,19960214,11444400000,'carla@example.com',9),(50,'Roberto Santos',78932200000,19811227,11333300000,'roberto@example.com',10),(51,'João Silva',12345700000,19900101,11987700000,'joao@example.com',11);
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
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
