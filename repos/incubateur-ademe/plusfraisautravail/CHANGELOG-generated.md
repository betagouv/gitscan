## Changelog : plusfraisautravail (30 derniers jours, au 25 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'ajout de nouvelles fonctionnalités au CMS, notamment l'intégration d'une application "sites-conformes" pour gérer les sites compatibles, ainsi que des corrections pour améliorer la stabilité et la configuration des environnements de production. Des ajustements ont également été apportés à l'intégration de Climadiag.

### Évolutions fonctionnelles
- Ajout d'une nouvelle application "sites-conformes" au CMS, permettant de gérer les sites compatibles avec l'outil. [#23](https://github.com/incubateur-ademe/plusfraisautravail/issues/23)
- Intégration de Climadiag commune. [#21](https://github.com/incubateur-ademe/plusfraisautravail/issues/21)
- Correction de l'affichage de l'auto-montage de la page d'accueil de Climadiag. [#20](https://github.com/incubateur-ademe/plusfraisautravail/issues/20)
- Mise à jour du texte du lien d'alerte pour refléter l'urgence.

### Évolutions techniques
- Migration vers Publicodes. [#20](https://github.com/incubateur-ademe/plusfraisautravail/issues/20)
- Configuration du CMS pour se connecter à la base de données via un réseau privé.
- Passage du déploiement du CMS à la version 1 de l'API.
- Amélioration de la gestion des mots de passe pour la base de données Postgres.
- Suppression d'une application IAM spécifique et réutilisation d'une clé de compte existante pour le bucket média.
- Correction de l'hypothèse concernant l'existence d'un projet Scaleway nommé "default".

### Autres changements
- Documentation mise à jour pour refléter les nouvelles fonctionnalités et corrections.
- Ajustements de configuration pour l'environnement de production de Climadiag.
