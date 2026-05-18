## Changelog : gallene-deployment (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur la préparation du déploiement de Gallene via Helm, un gestionnaire de paquets pour Kubernetes.  Les modifications incluent l'adaptation de l'image Docker, l'ajout de la configuration nécessaire pour Kubernetes et la correction de quelques erreurs initiales.

### Évolutions fonctionnelles
- Première version du chart Helm pour Gallene est disponible. [#1](https://github.com/suitenumerique/gallene-deployment/pull/1)
- Possibilité de spécifier la source du fichier `.env` pour faciliter le déploiement Kubernetes.

### Évolutions techniques
- L'image Docker de base a été modifiée pour utiliser `galene-headless` et inclut l'argument `-headless`.
- Intégration des scripts de `deburau/galene-docker` dans le dépôt.
- Correction d'une erreur de syntaxe dans le Dockerfile.
- La variable `VCS_REF` est maintenant correctement prise en compte lors de la construction de l'image Docker.
- Modification du Dockerfile pour s'aligner sur la version originale de `deburau/galene-docker`.

### Autres changements
- Aucun changement significatif à signaler.
