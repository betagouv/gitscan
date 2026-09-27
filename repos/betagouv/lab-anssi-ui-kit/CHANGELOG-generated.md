## Changelog : lab-anssi-ui-kit (30 derniers jours, au 25 septembre 2026)

### Résumé
Ce mois a été marqué par un effort important de stabilisation et de montée en qualité du code. Outre l'ajout de nouveaux composants (partage et icônes), les corrections ont porté sur l'accessibilité (focus) et la réactivité des composants sur mobile. La robustesse technique a été renforcée par une gestion plus stricte des types et des règles de qualité de code automatisées.

### Évolutions fonctionnelles
- **Nouveaux composants et ressources** : Ajout du composant de partage `DsfrShare` et intégration de nouvelles icônes (gamepad).
- **Améliorations de l'interface** : 
    - Meilleure visibilité du focus pour l'accessibilité.
    - Possibilité de personnaliser la taille des icônes.
    - Meilleure compatibilité des icônes avec les styles du DSFR.
    - Rendu de la propriété `disabled` désormais réactive.
- **Corrections d'expérience utilisateur** :
    - Résolution de problèmes de navigation dans les modales (boucle de focus sur les boutons).
    - Correction de l'affichage du bandeau de page sur mobile (variante sans image).
    - Correction du comportement des menus déroulants (`DsfrDropdown`).
- **Optimisation responsive** : Ajustements des espacements (padding, entêtes) et de la position des éléments (Centre d'aide) selon la taille de l'écran.

### Évolutions techniques
- **Qualité et conformité du code** : 
    - Refonte majeure de la configuration ESLint pour supprimer les faux positifs et imposer des règles plus strictes.
    - Intégration de `lint-staged` et de l'analyse ESLint directement dans la chaîne de CI pour garantir la qualité avant chaque commit.
- **Robustesse du typage** : 
    - Renforcement de la sécurité du code via `svelte-check` (correction des erreurs de types, gestion des valeurs `null/undefined` et typage explicite des paramètres).
    - Remplacement des types `any` par des types explicites.
- **Outils de développement** : 
    - Alignement des Storybook sur les standards ISO du DSFR.
    - Optimisation du processus de release et des hooks de pré-commit.
    - Mise à jour de l'environnement de développement (Svelte, pnpm, Vite).

### Autres changements
- **Documentation** : Mise à jour de la description du processus de release.
- **Versions** : Plusieurs montées de version effectuées (passage de la 1.60.10 à la 1.61.3).
