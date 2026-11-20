## Changelog : sites-conformes-buildpack (30 derniers jours, au 17 novembre 2026)

### Résumé
Ce buildpack permet d'automatiser le déploiement de l'application "Sites Conformes" sur la plateforme Scalingo. Les récentes évolutions ont permis de mettre en place l'outil et d'automatiser certains réglages de configuration réseau pour simplifier l'installation et le déploiement.

### Évolutions fonctionnelles
- Simplification du déploiement grâce à la détection automatique du domaine de l'application, limitant les configurations manuelles.

### Évolutions techniques
- Mise en place du buildpack Scalingo dédié à l'intégration automatique du code de l'application Sites Conformes.
- Automatisation de la configuration des variables d'environnement `HOST_URL` et `ALLOWED_HOSTS` en utilisant le domaine par défaut de l'application Scalingo.
