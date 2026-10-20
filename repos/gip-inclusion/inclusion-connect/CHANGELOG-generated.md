## Changelog : inclusion-connect (30 derniers jours, au 20 octobre 2026)

### Résumé
Ce mois-ci, le projet a introduit un mode "Démo" complet pour faciliter les présentations et les tests, en simplifiant considérablement le parcours d'accès. L'authentification a été allégée par la suppression de certaines étapes (mots de passe, OTP) et l'automatisation de la maintenance technique a été renforcée.

### Évolutions fonctionnelles
- **Introduction d'un mode Démo** :
    - Ajout d'une bannière distinctive pour signaler le mode démo.
    - Suppression de la saisie de mot de passe pour simplifier l'accès.
    - Restriction de l'utilisation aux adresses e-mail internes.
    - Possibilité de personnaliser le prénom et le nom lors de la connexion.
- **Simplification de l'authentification** :
    - Suppression des fonctionnalités liées aux mots de passe et au code OTP (One-Time Password).
- **Gestion des utilisateurs** :
    - Activation automatique des utilisateurs inactifs.
    - Amélioration de l'interface visuelle du formulaire de connexion.

### Évolutions techniques
- **Automatisation et CI/CD** :
    - Mise en place de l'auto-merge pour les mises à jour de dépendances (Dependabot) via une application GitHub dédiée.
- **Infrastructure et Environnement** :
    - Ajout de `gunicorn` aux dépendances pour le serveur de production.
    - Optimisation de l'environnement de test : amélioration de la commande `make test` et suppression de la dépendance Elasticsearch dans les réglages de test.

### Autres changements
- Mise à jour de la documentation (README).
- Nettoyage du code de test et suppression de code obsolète.
