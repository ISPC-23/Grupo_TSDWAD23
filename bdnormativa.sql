-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: bdnormativa
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `categoria`
--

DROP TABLE IF EXISTS `categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categoria` (
  `id_categoria` int NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_categoria`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categoria`
--

LOCK TABLES `categoria` WRITE;
/*!40000 ALTER TABLE `categoria` DISABLE KEYS */;
INSERT INTO `categoria` VALUES (1,'Laboral'),(2,'Penal'),(3,'Civil'),(4,'Comercial'),(5,'Familia y Sucesiones'),(6,'Agrario y Ambiental'),(7,'Minería'),(8,'Derecho informático'),(9,'Educacion');
/*!40000 ALTER TABLE `categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jurisdiccion`
--

DROP TABLE IF EXISTS `jurisdiccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jurisdiccion` (
  `id_jurisdiccion` int NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_jurisdiccion`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jurisdiccion`
--

LOCK TABLES `jurisdiccion` WRITE;
/*!40000 ALTER TABLE `jurisdiccion` DISABLE KEYS */;
INSERT INTO `jurisdiccion` VALUES (1,'Nacional'),(2,'Provincial');
/*!40000 ALTER TABLE `jurisdiccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `normativa`
--

DROP TABLE IF EXISTS `normativa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `normativa` (
  `id_normativa` int NOT NULL AUTO_INCREMENT,
  `id_tipo_normativa` int DEFAULT NULL,
  `numero` varchar(45) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `descripcion` varchar(300) DEFAULT NULL,
  `id_categoria` int DEFAULT NULL,
  `id_jurisdiccion` int DEFAULT NULL,
  `id_organo_legislativo` int DEFAULT NULL,
  PRIMARY KEY (`id_normativa`),
  KEY `id_jurisdiccion_idx` (`id_jurisdiccion`),
  KEY `id_categoria_idx` (`id_categoria`),
  KEY `id_organo_legislativo_idx` (`id_organo_legislativo`),
  KEY `id_tipo_normativa_idx` (`id_tipo_normativa`),
  CONSTRAINT `id_categoria` FOREIGN KEY (`id_categoria`) REFERENCES `categoria` (`id_categoria`),
  CONSTRAINT `id_jurisdiccion` FOREIGN KEY (`id_jurisdiccion`) REFERENCES `jurisdiccion` (`id_jurisdiccion`),
  CONSTRAINT `id_organo_legislativo` FOREIGN KEY (`id_organo_legislativo`) REFERENCES `organo_legislativo` (`id_organo_legislativo`),
  CONSTRAINT `id_tipo_normativa` FOREIGN KEY (`id_tipo_normativa`) REFERENCES `tipo_normativa` (`id_tipo_normativa`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `normativa`
--

LOCK TABLES `normativa` WRITE;
/*!40000 ALTER TABLE `normativa` DISABLE KEYS */;
INSERT INTO `normativa` VALUES (1,1,'20744','1974-09-11','La Ley de Contratos de Trabajo nº 20.744: Es la norma legal que regula las relaciones laborales de los trabajadores que se encuentran bajo relación de\r dependencia, excluyendo a los empleados de la Administración Pública',1,1,1),(2,1,'27555','2020-07-30','La ley de teletrabajo modifica la ley de Contrato de Trabajo para regular los derechos y obligaciones de las partes cuando la relación laboral se desarrolla a distancia.',1,1,1),(3,1,'7642','1987-11-21','Establecer entre los profesionales de Ciencias Informáticas una comunidad\r de intereses e ideales éticos, normativos y profesionales a fin de propender a su continuo\r perfeccionamiento',8,1,2),(4,3,'136','2014-03-20','Esta Resulución dispone, para la provincia de Córdoba, la creación de las Escuelas Secundarias ProA (Programa Avanzado) que otorga titulación de Bachiller en Desarrollo de Software',9,2,3),(5,3,'214','2022-03-22','Se aprueba el plan de estudios de la carrera Tecnicatura Superior en Desarrollo Web y Aplicaciones Digitales, para ser aplicado en el Instituto Superior Politécnico Córdoba, dependiente de este Ministerio.',9,2,3);
/*!40000 ALTER TABLE `normativa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `organo_legislativo`
--

DROP TABLE IF EXISTS `organo_legislativo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `organo_legislativo` (
  `id_organo_legislativo` int NOT NULL AUTO_INCREMENT,
  `descripcoin` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_organo_legislativo`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `organo_legislativo`
--

LOCK TABLES `organo_legislativo` WRITE;
/*!40000 ALTER TABLE `organo_legislativo` DISABLE KEYS */;
INSERT INTO `organo_legislativo` VALUES (1,'Honorable Congreso de la Nación Argentina'),(2,'Legislatura de la Provincia de Córdoba'),(3,'Ministerio de Educación de la Provincia de Córdoba');
/*!40000 ALTER TABLE `organo_legislativo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `palabra_clave`
--

DROP TABLE IF EXISTS `palabra_clave`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `palabra_clave` (
  `id_palabra_clave` int NOT NULL AUTO_INCREMENT,
  `id_normativa` int DEFAULT NULL,
  `descripcion` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_palabra_clave`),
  KEY `id_normativa_idx` (`id_normativa`),
  CONSTRAINT `id_normativa` FOREIGN KEY (`id_normativa`) REFERENCES `normativa` (`id_normativa`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `palabra_clave`
--

LOCK TABLES `palabra_clave` WRITE;
/*!40000 ALTER TABLE `palabra_clave` DISABLE KEYS */;
INSERT INTO `palabra_clave` VALUES (1,1,'contrato'),(2,1,'trabajo'),(3,1,'laboral'),(4,1,'derecho'),(5,2,'distancia'),(6,2,'teletrabajo'),(7,2,'homeoffice'),(8,3,'honorarios'),(9,3,'consejo'),(10,3,'informatica'),(11,3,'informacion'),(12,4,'programa'),(13,4,'avanzado'),(14,4,'proa'),(15,4,'experimental'),(16,4,'escuelas'),(17,4,'secundaria'),(18,5,'plan de estudio'),(19,5,'carreras'),(20,5,'educacion tecnica superior'),(21,5,'tecnicaturas');
/*!40000 ALTER TABLE `palabra_clave` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_normativa`
--

DROP TABLE IF EXISTS `tipo_normativa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_normativa` (
  `id_tipo_normativa` int NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_tipo_normativa`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_normativa`
--

LOCK TABLES `tipo_normativa` WRITE;
/*!40000 ALTER TABLE `tipo_normativa` DISABLE KEYS */;
INSERT INTO `tipo_normativa` VALUES (1,'Ley'),(2,'Decreto'),(3,'Resolución');
/*!40000 ALTER TABLE `tipo_normativa` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-14  0:18:39
