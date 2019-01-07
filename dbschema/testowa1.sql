CREATE DATABASE testowa1;
USE testowa1;
--
-- Table structure for table `mytable`
--

DROP TABLE IF EXISTS `mytable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mytable` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) DEFAULT NULL,
  `Value` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mytable`
--

LOCK TABLES `mytable` WRITE;
/*!40000 ALTER TABLE `mytable` DISABLE KEYS */;
INSERT INTO `mytable` VALUES (1,'Genius','me'),(2,'Genius','me'),(3,'Genius','me'),(4,'Genius','me'),(5,'Genius','me'),(6,'Genius','me'),(7,'Genius','me'),(8,'Genius','me'),(9,'54f7749e-05ec-11e9-89a0-000d3a22998e','me'),(10,'5669bbde-05ec-11e9-89a0-000d3a22998e','me'),(11,'afdb45a2-05ec-11e9-89a0-000d3a22998e','me'),(12,'c71e5614-05ec-11e9-89a0-000d3a22998e','me'),(13,'de2609ba-05ec-11e9-89a0-000d3a22998e','me'),(14,'f80f4134-05ec-11e9-89a0-000d3a22998e','me'),(15,'3f29ecfe-05ed-11e9-89a0-000d3a22998e','me'),(16,'87470e86-05ed-11e9-89a0-000d3a22998e','me'),(17,'927fd81e-05ed-11e9-89a0-000d3a22998e','me'),(18,'9903a5b2-05ed-11e9-89a0-000d3a22998e','me'),(19,'a98df0e0-05ed-11e9-89a0-000d3a22998e','me'),(20,'eac3f692-060e-11e9-89a0-000d3a22998e','me'),(21,'eba2d2a4-060e-11e9-89a0-000d3a22998e','me'),(22,'ec27e868-060e-11e9-89a0-000d3a22998e','me'),(23,'40ff1e56-060f-11e9-89a0-000d3a22998e','me'),(24,'814670cc-060f-11e9-89a0-000d3a22998e','me'),(25,'9f4a292e-060f-11e9-89a0-000d3a22998e','me'),(26,'1a4519cc-0610-11e9-89a0-000d3a22998e','me'),(27,'2f60c41e-0610-11e9-89a0-000d3a22998e','me'),(28,'b040e5fa-0610-11e9-89a0-000d3a22998e','me'),(29,'81a589de-0693-11e9-89a0-000d3a22998e','me'),(30,'387c520a-0694-11e9-89a0-000d3a22998e','me'),(31,'3fb4f248-0694-11e9-89a0-000d3a22998e','me'),(32,'61ae4700-0694-11e9-89a0-000d3a22998e','me'),(33,'a6014358-0694-11e9-89a0-000d3a22998e','me');
/*!40000 ALTER TABLE `mytable` ENABLE KEYS */;
UNLOCK TABLES;
