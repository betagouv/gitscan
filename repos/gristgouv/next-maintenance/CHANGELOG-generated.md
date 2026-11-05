## Changelog : next-maintenance (30 derniers jours, au 03/11/2026)

### Résumé
Initialisation du projet visant à centraliser les informations relatives aux périodes de maintenance des instances DINUM et ANCT. Le dépôt est désormais structuré pour permettre une gestion automatisée et sécurisée des annonces de maintenance.

### Évolutions fonctionnelles
- Création de la structure de données principale via le fichier `maintenance.yaml` pour le suivi des périodes de maintenance.

### Évolutions techniques
- Mise en place de l'automatisation (CI/CD) avec l'ajout de workflows GitHub Actions pour le déploiement et la validation automatique de la conformité du contenu YAML lors des modifications.
- Optimisation du traitement des fichiers YAML via la configuration de l'outil `yq` pour garantir le respect des spécifications.

### Autres changements
- Initialisation du dépôt et ajout de la documentation (README).
