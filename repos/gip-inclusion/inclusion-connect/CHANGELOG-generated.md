## Changelog : inclusion-connect (30 derniers jours, au 08/10/2026)

### Résumé
Ce mois-ci, le projet a introduit un **mode Démo** complet, conçu pour simplifier les tests et les démonstrations en supprimant les contraintes de mot de passe et en limitant l'usage à des e-mails internes. Parallèlement, des améliorations ont été apportées à l'expérience de connexion et à l'automatisation des processus de test et de maintenance.

### Évolutions fonctionnelles
- **Introduction d'un mode Démo** :
    - Connexion simplifiée sans saisie de mot de passe.
    - Possibilité de choisir le prénom et le nom de l'utilisateur.
    - Restriction de l'utilisation aux adresses e-mail internes uniquement.
    - Ajout d'une bannière visuelle pour identifier clairement l'utilisation du mode démo.
- **Gestion des utilisateurs** :
    - Activation automatique des utilisateurs inactifs.
    - Suppression des fonctionnalités liées aux mots de passe et à l'OTP (One-Time Password) pour simplifier les parcours de test.
- **Interface utilisateur** :
    - Amélioration du template de la page de connexion.

### Évolutions techniques
- **CI/CD** : Automatisation de la fusion des Pull Requests de mise à jour des dépendances (Dependabot).
- **Tests** :
    - Optimisation de la commande de test (`make test`).
    - Simplification de l'environnement de test par la suppression de la dépendance à Elasticsearch dans les configurations de test.
    - Nettoyage et suppression de code superflu dans la suite de tests.

### Autres changements
- Mise à jour de la documentation (README).
- Nettoyage du dépôt (suppression d'anciens templates et de code obsolète).
