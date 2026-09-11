## Changelog : Docurba (30 derniers jours, au 10 septembre 2026)

### Résumé
Ce mois-ci, les développements ont principalement porté sur le renforcement de la sécurité des comptes utilisateurs, avec une mise en conformité des politiques de mots de passe (recommandations CNIL) et une gestion plus robuste des sessions. L'expérience de communication a également été améliorée grâce à une intégration plus fiable des services d'envoi d'emails et de notifications Slack.

### Évolutions fonctionnelles
- **Gestion des accès et sécurité** :
    - Refonte complète du processus de réinitialisation et de mise à jour des mots de passe.
    - Mise en place de validations de sécurité renforcées lors de la création ou du changement de mot de passe.
    - Amélioration de la clarté des messages d'erreur lors de la tentative de connexion.
- **Interface d'administration** :
    - Ajout de nouveaux filtres et de colonnes de données (dates de création) pour faciliter la gestion des procédures et des profils.
- **Notifications** :
    - Amélioration de la lisibilité des sujets d'emails et des messages Slack pour une meilleure identification des contextes.

### Évolutions techniques
- **Sécurité et API** :
    - Migration des vues API Django vers Django Rest Framework (DRF) pour une meilleure standardisation.
    - Sécurisation des API par défaut (déclaration comme privées).
    - Centralisation de la logique d'envoi d'emails dans le backend (Django) via l'intégration de Sendgrid.
    - Optimisation de la gestion des sessions pour éviter les durées de connexion infinies.
- **Architecture et Intégration** :
    - Consolidation de l'architecture en remplaçant les endpoints Nuxt par l'utilisation systématique de l'API interne.
    - Optimisation de l'intégration avec Supabase (gestion des clés de service et des tokens).
- **Infrastructure et Performance** :
    - Optimisation de la configuration Nginx pour améliorer les taux de transfert.
    - Amélioration de l'efficacité des scripts de sauvegarde (réduction de la consommation de RAM et de disque).
    - Mise à niveau des plans d'infrastructure (Scalingo) pour supporter les besoins de déploiement.

### Autres changements
- **Nettoyage du code** : Suppression de composants frontend et de répertoires de tests obsolètes.
- **CI/CD** : Mise à jour des outils de déploiement et de la CLI Supabase dans les workflows GitHub Actions.
