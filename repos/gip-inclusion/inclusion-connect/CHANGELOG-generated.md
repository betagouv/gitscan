## Changelog : inclusion-connect (30 derniers jours, au 05/11/2026)

### Résumé
Ce mois-ci, le projet a connu une simplification majeure de son processus d'authentification, notamment par la suppression de la gestion des mots de passe et des codes OTP. Parallèlement, des efforts importants ont été consacrés à l'automatisation de la maintenance technique et à l'optimisation des outils de test et de déploiement.

### Évolutions fonctionnelles
- **Simplification de l'authentification** : suppression des fonctionnalités liées aux mots de passe et au code OTP (One-Time Password).
- **Nouveaux modes de gestion** : introduction d'un mode "DEMO" forcé et de l'activation automatique des utilisateurs inactifs.
- **Expérience utilisateur** : amélioration de l'interface (template) de la page de connexion.

### Évolutions techniques
- **Automatisation de la maintenance** : mise en place de l'auto-merge pour les mises à jour de dépendances (Dependabot) afin de fluidifier la gestion des versions.
- **Optimisation des tests et du développement** : 
    - Amélioration de la commande `make test`.
    - Nettoyage du code de test (suppression d'un correctif spécifique à Elasticsearch).
    - Suppression de code de test obsolète.
- **Infrastructure** : ajout de `gunicorn` aux dépendances pour la gestion du serveur d'application.

### Autres changements
- Mise à jour de la documentation (README).
