## Changelog : inclusion-connect (30 derniers jours, au 03/11/2026)

### Résumé
Ce mois-ci, le projet a connu des changements structurels importants, notamment une simplification des modes d'accès avec la suppression des fonctionnalités liées aux mots de passe et aux codes OTP, au profit d'un mode "DEMO" et d'une activation automatique des utilisateurs. Parallèlement, la maintenance technique a été optimisée grâce à une meilleure automatisation des mises à jour et une simplification de l'environnement de test.

### Évolutions fonctionnelles
- **Simplification de l'authentification** : Suppression des fonctionnalités liées aux mots de passe et aux codes OTP (One-Time Password).
- **Nouveaux modes de gestion** : 
    - Introduction d'un mode "DEMO" forcé.
    - Mise en place de l'activation automatique des utilisateurs inactifs.
- **Expérience utilisateur** : Amélioration du design et du template de la page de connexion.

### Évolutions techniques
- **Automatisation de la maintenance** : Mise en place de l'auto-merge pour les mises à jour de dépendances (Dependabot) afin de fluidifier la gestion des versions.
- **Infrastructure et serveur** : Ajout de Gunicorn pour la gestion du serveur web.
- **Optimisation des tests** : 
    - Amélioration de la commande de test (`make test`).
    - Simplification de la configuration des tests par la suppression d'une dépendance spécifique à Elasticsearch.
    - Nettoyage du code de test.

### Autres changements
- Mise à jour de la documentation (README).
