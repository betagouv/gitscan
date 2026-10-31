## Changelog : acceslibre (30 derniers jours, au 28 octobre 2026)

### Résumé
Ce mois-ci, la plateforme a franchi une étape importante dans sa capacité d'analyse grâce à l'ajout de nouveaux outils de visualisation de données (widgets santé et domaines). L'expérience utilisateur a été affinée par des ajustements visuels et des corrections de bugs, tandis que l'infrastructure a été profondément modernisée pour gagner en performance et en stabilité.

### Évolutions fonctionnelles
- **Nouveaux outils de visualisation** : Ajout d'un widget dédié au secteur de la santé ([#2923](https://github.com/MTES-MCT/acceslibre/issues/2923)) et d'un tableau de bord permettant d'agréger les données par domaine ([#2882](https://github.com/MTES-MCT/acceslibre/issues/2882)).
- **Améliorations de l'interface (UI)** : Mise à jour des couleurs de la page d'accueil et de la page "challenge" ([#2881](https://github.com/MTES-MCT/acceslibre/issues/2881)), et correction de l'affichage de la modale RPA ainsi que de la génération de PDF ([#2867](https://github.com/MTES-MCT/acceslibre/issues/2867)).
- **Corrections de données et de logique** : Correction du comptage des villes avec des arrondissements ([#2868](https://github.com/MTES-MCT/acceslibre/issues/2868)), mise en place d'un décompte des sources externes ([#2866](https://github.com/MTES-MCT/acceslibre/issues/2866)) et résolution de problèmes de calcul sur le "jour 0" des challenges ([#2879](https://github.com/MTES-MCT/acceslibre/issues/2879)).

### Évolutions techniques
- **Optimisation des performances** : Suppression des requêtes "N+1" pour optimiser les temps de réponse de la base de données ([#2884](https://github.com/MTES-MCT/acceslibre/issues/2884)).
- **Infrastructure et DevOps** : Modernisation de l'environnement Docker, ajout d'un script de restauration ([#2885](https://github.com/MTES-MCT/acceslibre/issues/2885)) et amélioration de la gestion des dumps de données ([#2913](https://github.com/MTES-MCT/acceslibre/issues/2913)).
- **API et Backend** : Amélioration de la gestion et du suivi des clés API ([#2909](https://github.com/MTES-MCT/acceslibre/issues/2909)), enrichissement du schéma de réponse de l'API ([#2925](https://github.com/MTES-MCT/acceslibre/issues/2925)) et corrections de sécurité sur la documentation Swagger ([#2915](https://github.com/MTES-MCT/acceslibre/issues/2915)).
- **Mises à jour système et compatibilité** : Passage à Python 3.14.8 ([#2911](https://github.com/MTES-MCT/acceslibre/issues/2911)), gestion de la rétrocompatibilité pour les questions parentes des tribunes ([#2936](https://github.com/MTES-MCT/acceslibre/issues/2936)) et correction de faux positifs lors du traitement de mots avec tirets ([#2937](https://github.com/MTES-MCT/acceslibre/issues/2937)).

### Autres changements
- Suppression de l'ancienne version de la contribution (contrib v2) ([#2886](https://github.com/MTES-MCT/acceslibre/issues/2886)).
