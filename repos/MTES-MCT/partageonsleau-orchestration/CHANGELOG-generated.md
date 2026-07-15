## Changelog : partageonsleau-orchestration (30 derniers jours, au 13 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à l'ingestion et au traitement des données provenant de différentes sources (Aquasys, Gidaf, BV Tech, Murgat).  Les corrections et ajouts se concentrent sur la normalisation des volumes prélevés, la gestion des timestamps et l'amélioration de la robustesse de l'import des données.

### Évolutions fonctionnelles
- Amélioration de l'import des données Gidaf [#862c9cf](https://github.com/MTES-MCT/partageonsleau-orchestration/commit/862c9cf).
- Correction du replay des déclarations BV Tech [#703dfaf](https://github.com/MTES-MCT/partageonsleau-orchestration/commit/703dfaf).
- Ajout du support pour le connecteur Murgat [#4709448](https://github.com/MTES-MCT/partageonsleau-orchestration/commit/4709448).
- Ajout de l'usage dans la déclaration [#7405e38](https://github.com/MTES-MCT/partageonsleau-orchestration/commit/7405e38).
- Correction du parser Aquasys [#3a4d626](https://github.com/MTES-MCT/partageonsleau-orchestration/commit/3a4d626).
- Correction de l'import Aquasys [#6dc1f59](https://github.com/MTES-MCT/partageonsleau-orchestration/commit/6dc1f59).
- Ajout du support pour Gidaf [#de2d0d7](https://github.com/MTES-MCT/partageonsleau-orchestration/commit/de2d0d7).

### Évolutions techniques
- Les volumes Aquasys partagés sont désormais divisés par déclarant [#6791a28](https://github.com/MTES-MCT/partageonsleau-orchestration/commit/6791a28).
- Les compteurs Aquasys partagés non alloués sont conservés [#8d2a569](https://github.com/MTES-MCT/partageonsleau-orchestration/commit/8d2a569).
- Les volumes Aquasys dupliqués sont divisés [#fc92e59](https://github.com/MTES-MCT/partageonsleau-orchestration/commit/fc92e59).
- Les données Willie sont protégées lors de l'ingestion Aquasys [#e93e428](https://github.com/MTES-MCT/partageonsleau-orchestration/commit/e93e428).
- Utilisation d'une politique d'ingestion de fichiers non écrasante [#9fb0c58](https://github.com/MTES-MCT/partageonsleau-orchestration/commit/9fb0c58).
- Rattachement des volumes Aquasys aux préleveurs [#cd95575](https://github.com/MTES-MCT/partageonsleau-orchestration/commit/cd95575).
- Préservation des timestamps de déclaration sous-quotidienne [#4b99f5f](https://github.com/MTES-MCT/partageonsleau-orchestration/commit/4b99f5f).
- Ajout d'un contexte de connecteur [#d7e53fe](https://github.com/MTES-MCT/partageonsleau-orchestration/commit/d7e53fe).
- Correction des usages et de Gidaf [#d51d445](https://github.com/MTES-MCT/partageonsleau-orchestration/commit/d51d445).
- Ajout d'une commande `watch` [#31877a4](https://github.com/MTES-MCT/partageonsleau-orchestration/commit/31877a4).
- Envoi des types de flux de points avec les mesures [#b3f9f04](https://github.com/MTES-MCT/partageonsleau-orchestration/commit/b3f9f04).
