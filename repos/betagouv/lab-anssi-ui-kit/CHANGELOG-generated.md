## Changelog : lab-anssi-ui-kit (30 derniers jours, au 12 novembre 2026)

### Résumé
Ce mois a été marqué par une transition majeure vers la version 2.0 du kit. Les évolutions incluent l'ajout de nouveaux composants de saisie, l'amélioration des outils de navigation (filtres) et une refonte structurelle profonde visant à stabiliser l'intégration des composants et à optimiser les processus de développement et de publication.

### Évolutions fonctionnelles
- **Nouveaux composants** : Ajout du composant `DsfrUpload` pour la gestion des téléchargements de fichiers.
- **Amélioration de l'expérience utilisateur** : Optimisation du composant `FiltresCatalogue` avec l'ajout d'une variation de liens et une amélioration des styles visuels.
- **Corrections** : Résolution de problèmes d'importation des composants DSFR pour les éléments `Card`, `User` et `Dropdown`.

### Évolutions techniques
- **Architecture & Web Components** : 
    - Refonte de l'enregistrement des Web Components pour le rendre idempotent, évitant ainsi les doublons d'enregistrement pour les composants Lab ANSSI et DSFR.
    - Unification de l'extraction des métadonnées des Web Components.
    - Optimisation du *tree-shaking* pour une meilleure gestion de la taille des paquets.
- **CI/CD & Qualité** :
    - Alignement des workflows de CI sur la version Node.js du projet.
    - Intégration de la configuration `pnpm/setup` et ajout de vérifications automatiques des types Svelte et TypeScript.
- **Toolchain & Publication** :
    - Centralisation de la configuration du registre et des accès dans `publishConfig`.
    - Mise à jour de la gestion des dépendances avec `pnpm` et modification du comportement de repli lors des téléchargements.
