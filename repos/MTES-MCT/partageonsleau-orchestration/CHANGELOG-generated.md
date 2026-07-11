## Changelog : partageonsleau-orchestration (30 derniers jours, au 10 juillet 2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de l'ingestion et du traitement des données provenant de différentes sources (Aquasys, BV Tech, Gidaf, Murgat). Des corrections ont été apportées pour assurer la fiabilité de l'import des données et la bonne association des volumes prélevés aux déclarants.

### Évolutions fonctionnelles
- Correction de l'import des déclarations BV Tech pour éviter les relectures incorrectes. [#703dfaf](https://github.com/MTES-MCT/partageonsleau-orchestration/issues/703dfaf)
- Correction de l'import des données Gidaf. [#862c9cf](https://github.com/MTES-MCT/partageonsleau-orchestration/issues/862c9cf)
- Amélioration du parser Aquasys pour corriger des erreurs d'import. [#3a4d626](https://github.com/MTES-MCT/partageonsleau-orchestration/issues/3a4d626)
- Correction de l'association des volumes Aquasys aux préleveurs. [#cd95575](https://github.com/MTES-MCT/partageonsleau-orchestration/issues/cd95575)
- Ajout de la prise en charge du connecteur Murgat. [#4709448](https://github.com/MTES-MCT/partageonsleau-orchestration/issues/4709448)
- Ajout de la prise en charge de Gidaf. [#de2d0d7](https://github.com/MTES-MCT/partageonsleau-orchestration/issues/de2d0d7)

### Évolutions techniques
- Mise en place d'une politique d'ingestion de fichiers qui ne remplace pas les fichiers existants. [#9fb0c58](https://github.com/MTES-MCT/partageonsleau-orchestration/issues/9fb0c58)
- Protection des données Willie lors de l'ingestion Aquasys. [#e93e428](https://github.com/MTES-MCT/partageonsleau-orchestration/issues/e93e428)
- Préservation des timestamps des déclarations sous-quotidiennes. [#4b99f5f](https://github.com/MTES-MCT/partageonsleau-orchestration/issues/4b99f5f)
- Séparation des volumes Aquasys partagés par déclarant. [#6791a28](https://github.com/MTES-MCT/partageonsleau-orchestration/issues/6791a28)
- Maintien des compteurs Aquasys partagés non alloués. [#8d2a569](https://github.com/MTES-MCT/partageonsleau-orchestration/issues/8d2a569)
- Séparation des volumes de compteurs Aquasys dupliqués. [#fc92e59](https://github.com/MTES-MCT/partageonsleau-orchestration/issues/fc92e59)
- Ajout d'un contexte de connecteur. [#d7e53fe](https://github.com/MTES-MCT/partageonsleau-orchestration/issues/d7e53fe)
- Ajout d'une information d'usage dans la déclaration. [#7405e38](https://github.com/MTES-MCT/partageonsleau-orchestration/issues/7405e38)

### Autres changements
- Ajout d'une commande `watch`. [#31877a4](https://github.com/MTES-MCT/partageonsleau-orchestration/issues/31877a4)
- Mise à jour de npm. [#672f54b](https://github.com/MTES-MCT/partageonsleau-orchestration/issues/672f54b)
- Correction des usages et de Gidaf. [#d51d445](https://github.com/MTES-MCT/partageonsleau-orchestration/issues/d51d445)
