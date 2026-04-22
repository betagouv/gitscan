## Changelog : gallene-deployment (30 derniers jours, au 21 avril 2026)

### Résumé
Ce mois-ci, le projet Gallene-deployment a connu une refonte majeure avec l'ajout d'un Dockerfile et de scripts de déploiement basés sur le projet `deburau/galene-docker`. Ces changements facilitent grandement le déploiement de Gallene, notamment dans un environnement Kubernetes, en permettant la configuration via un fichier `.env`.

### Évolutions fonctionnelles
- Ajout de la possibilité de configurer Gallene via un fichier `.env` pour faciliter le déploiement Kubernetes. [#1](https://github.com/suitenumerique/gallene-deployment/pull/1)

### Évolutions techniques
- Intégration du Dockerfile initial et des scripts de déploiement du projet `deburau/galene-docker`.
- Correction d'une erreur de syntaxe dans le Dockerfile.
- Modification du Dockerfile pour l'adapter au contexte de Gallene-deployment.
- Initialisation du dépôt avec un premier commit.

### Autres changements
- Ajout du dossier racine contenant les scripts issus de `deburau/galene-docker`.
