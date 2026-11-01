## Changelog : anssi-demain-specialiste-cyber (30 derniers jours, au 30 octobre 2026)

### Résumé
Ce mois a été marqué par une évolution majeure de la plateforme avec l'intégration de nouvelles données sur les métiers de la cybersécurité et le déploiement d'une nouvelle section dédiée à la formation et à l'entraînement. L'interface utilisateur a également été affinée pour améliorer la clarté et l'expérience de navigation.

### Évolutions fonctionnelles
- **Nouveaux parcours de formation** : Implémentation de la page et de la route "Se former et s'entraîner en ligne".
- **Gestion des métiers** : Intégration de nouvelles données permettant d'afficher les familles de métiers, les profils associés et les ressources correspondantes.
- **Parcours d'évaluation** : Ajout d'API pour alimenter les sections "Je me mesure" et "Je m'entraîne".
- **Améliorations de l'interface (UI/UX)** :
    - Optimisation de l'affichage du mode sombre.
    - Corrections de textes (wording) sur la page d'accueil et les sections de présentation.
    - Mise à jour de l'identité visuelle (retrait du logo et de la tagline ANSSI).

### Évolutions techniques
- **Infrastructure et Environnement** :
    - Migration de la stack vers Node.js 26.
    - Passage de l'environnement de CI sur Ubuntu 26.04.
    - Introduction du shell Nix pour le développement.
- **Refactorisation et Qualité** :
    - Nettoyage massif du code pour supprimer de nombreuses surcharges de types inutiles dans les dépendances.
    - Centralisation des instructions pour les agents d'IA.
    - Amélioration de la gestion des logs pour le débogage de l'authentification.
- **Tests et Outillage** :
    - Mise à jour du support de testing-library avec Vitest 5.
    - Automatisation du tri des imports.
- **Dépendances** :
    - Mise à jour majeure de l'UI Kit (v1.64.0).
    - Montée de version de plusieurs bibliothèques clés (Svelte, Vite, Axios, Zod, etc.).

### Autres changements
- **Documentation** : Réorganisation complète du guide de développement pour une meilleure lisibilité.
