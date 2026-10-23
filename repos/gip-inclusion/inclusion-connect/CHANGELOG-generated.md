## Changelog : inclusion-connect (30 derniers jours, au 23 octobre 2026)

### Résumé
Ce mois-ci, le projet a introduit un "Mode Démo" complet pour faciliter les tests et les démonstrations, permettant de naviguer sans mot de passe. Parallèlement, le système d'authentification a été simplifié par la suppression des fonctionnalités liées aux mots de passe et aux codes OTP (One-Time Password).

### Évolutions fonctionnelles
- **Introduction d'un mode démo** :
    - Possibilité de tester le service sans saisie de mot de passe.
    - Ajout d'une bannière d'information pour signaler l'utilisation du mode démo.
    - Restriction de l'utilisation aux adresses e-mails internes.
    - Possibilité de personnaliser le nom et le prénom lors de l'utilisation de ce mode.
- **Simplification de l'authentification** : suppression des fonctionnalités liées aux mots de passe et à l'authentification par OTP.
- **Amélioration de l'interface** : optimisation du template de la page de connexion.

### Évolutions techniques
- **Automatisation de la maintenance** : mise en place d'une application GitHub pour l'auto-merge des Pull Requests de Dependabot, fluidifiant la gestion des mises à jour de dépendances.
- **Optimisation des tests** :
    - Amélioration de la commande `make test`.
    - Nettoyage du code de test et suppression de hacks liés à Elasticsearch.
- **Infrastructure** : ajout de `gunicorn` aux dépendances pour le serveur d'application.

### Autres changements
- Mise à jour de la documentation (README).
