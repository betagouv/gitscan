## Changelog : anssi-demain-specialiste-cyber (30 derniers jours, au 22 octobre 2026)

### Résumé
Ce mois a été marqué par une évolution majeure de l'offre de contenu avec l'implémentation de la nouvelle section "Se former et s'entraîner". Parallèlement, le projet a bénéficié d'un important travail de nettoyage technique et de refonte de l'identité visuelle (en-tête), visant à améliorer la qualité du code et la clarté de l'interface utilisateur.

### Évolutions fonctionnelles
- **Nouvelle section de formation** : Mise en ligne de la page "Se former et s'entraîner en ligne" (route `/se-former`) incluant ses vues et composants dédiés.
- **Identité visuelle** : Mise à jour de l'en-tête avec le retrait du logo ANSSI et de la tagline "Innovation ANSSI".
- **Améliorations de l'interface (UI)** :
    - Optimisation de l'application du mode sombre sur les pages de sélection.
    - Correction de l'affichage du bloc "Comment ça marche ?" sur la page d'accueil.
- **Corrections éditoriales** : Ajustements du wording sur la page d'accueil et dans la section de présentation pour une meilleure clarté.

### Évolutions techniques
- **Développement d'API** : Création de nouveaux points de terminaison (endpoints) pour gérer les sélections "Je me mesure" et "Je m'entraîne".
- **Refactoring et nettoyage de code** :
    - Suppression massive de surcharges de types (overrides) inutiles pour de nombreuses dépendances (Svelte, Axios, Lodash, Vitest, etc.), allégeant ainsi la base de code.
    - Nettoyage des logs de debug liés à l'authentification.
- **Environnement de développement et Outillage** :
    - Introduction du shell Nix pour une meilleure reproductibilité de l'environnement.
    - Mise en place du tri automatique des imports.
    - Centralisation des instructions pour les agents d'intelligence artificielle.
- **Optimisations de configuration** :
    - Migration de la configuration Vitest vers le format ESM.
    - Utilisation de `import.meta.dirname` pour les configurations Vite.
    - Limitation des versions majeures de TypeScript et de Sentry pour stabiliser l'environnement.

### Autres changements
- **Documentation** : Réorganisation complète du guide de développement pour en faciliter la lecture.
