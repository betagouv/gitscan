## Changelog : anssi-demain-specialiste-cyber (30 derniers jours, au 28 octobre 2026)

### Résumé
Ce mois-ci, la plateforme a franchi une étape importante avec le développement et l'intégration de la nouvelle section dédiée à la formation et à l'entraînement en ligne. Parallèlement, une modernisation profonde de l'infrastructure et des outils de développement a été réalisée pour améliorer la stabilité, la performance et la maintenabilité du projet.

### Évolutions fonctionnelles
- **Nouvelle section de formation** : Implémentation de la page "Se former et s'entraîner en ligne" (nouvelle route `/se-former`) et de ses composants associés.
- **Nouvelles capacités d'évaluation** : Mise à disposition d'API dédiées pour les parcours "Je me mesure" et "Je m'entraîne".
- **Améliorations de l'interface utilisateur** :
    - Optimisation de l'application du mode sombre.
    - Corrections d'affichage sur le bloc "Comment ça marche ?".
    - Ajustements de la rédaction (wording) pour une meilleure clarté (notamment sur la page d'accueil et la section de présentation).
- **Évolution de l'identité visuelle** : Retrait du logo ANSSI et de la tagline dans l'en-tête du site.

### Évolutions techniques
- **Infrastructure et CI/CD** :
    - Migration de la stack vers Node.js 26.
    - Mise à jour de l'environnement de CI vers Ubuntu 26.04.
- **Tests et Qualité** :
    - Support de Vitest 5 pour la bibliothèque `testing-library/jest-dom`.
    - Passage de la configuration Vitest backend en mode ESM.
- **Outillage de développement** :
    - Introduction du shell Nix pour la gestion de l'environnement.
    - Automatisation du tri des imports.
    - Centralisation des instructions pour les agents d'intelligence artificielle.
- **Refactoring et Optimisation** :
    - Nettoyage massif du code via la suppression de nombreuses surcharges de types inutiles.
    - Suppression des logs de debug d'authentification en production.
- **Mises à jour majeures** : Montée de version de plusieurs dépendances critiques, notamment le UI Kit (v1.64.0), Svelte, Axios, Knex et Zod.

### Autres changements
- **Documentation** : Réorganisation complète du guide de développement pour une meilleure lisibilité.
