## Changelog : inclusion-connect (30 derniers jours, au 12 octobre 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante avec l'introduction d'un "Mode Démo" complet, conçu pour simplifier les phases de test et de présentation en supprimant les contraintes d'authentification classiques. Parallèlement, les processus de développement ont été optimisés grâce à une meilleure automatisation des mises à jour et une simplification de l'environnement de tests.

### Évolutions fonctionnelles
- **Introduction du "Mode Démo"** :
    - Ajout d'une bannière visuelle pour identifier le mode actif.
    - Simplification de l'accès : suppression de la demande de mot de passe et de l'OTP (One-Time Password).
    - Restriction de l'utilisation aux adresses e-mail internes uniquement.
    - Possibilité de personnaliser le prénom et le nom lors de l'utilisation de ce mode.
- **Gestion des utilisateurs** :
    - Activation automatique des utilisateurs inactifs.
- **Interface utilisateur** :
    - Amélioration du template de la page de connexion.
    - Suppression des fonctionnalités liées aux mots de passe et à l'OTP pour alléger l'expérience.

### Évolutions techniques
- **CI/CD et Automatisation** :
    - Mise en place de l'auto-merge pour les mises à jour de dépendances (Dependabot), réduisant la charge de maintenance manuelle.
- **Tests et Qualité** :
    - Optimisation de la commande `make test` pour améliorer l'expérience de développement.
    - Simplification de l'environnement de test par la suppression des dépendances à Elasticsearch.
    - Nettoyage du code de test obsolète.
- **Infrastructure** :
    - Ajout de `gunicorn` aux dépendances pour la gestion du serveur d'application.

### Autres changements
- **Documentation** : Mise à jour du fichier README.
- **Nettoyage** : Suppression d'anciens templates et de code non utilisé.
