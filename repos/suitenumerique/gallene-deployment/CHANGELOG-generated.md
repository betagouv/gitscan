## Changelog : gallene-deployment (30 derniers jours, au 21 avril 2026)

### Résumé
Ce mois-ci, le projet Gallene-deployment a connu une refonte majeure avec l'importation des scripts de déploiement et du Dockerfile originaux du projet `deburau/galene-docker`.  Ces changements permettent une meilleure base pour le déploiement de Gallene, notamment en facilitant son utilisation avec Kubernetes grâce à la configuration d'un fichier `.env`.

### Évolutions fonctionnelles
- Ajout de la source du fichier `.env` pour faciliter le déploiement Kubernetes.

### Évolutions techniques
- Importation du Dockerfile et des scripts de déploiement du projet `deburau/galene-docker` [#1](https://github.com/suitenumerique/gallene-deployment/pull/1).
- Correction d'une erreur de syntaxe dans le Dockerfile.
- Modification du Dockerfile pour s'aligner sur la version originale de `deburau/galene-docker`.
- Initialisation du dépôt avec un premier commit contenant le Dockerfile.

### Autres changements
- Initialisation du dépôt par Samuel Paccoud.
