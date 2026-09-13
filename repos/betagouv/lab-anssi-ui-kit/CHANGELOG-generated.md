## Changelog : lab-anssi-ui-kit (30 derniers jours, au 11 septembre 2026)

### Résumé
Cette période a été marquée par une amélioration significative de la réactivité des composants et de leur accessibilité. Le kit a bénéficié d'une mise à jour technique majeure avec le passage à Vite 8, garantissant une meilleure compatibilité et des performances accrues. Les composants de la suite "Lab" ont été affinés pour offrir une meilleure expérience sur mobile et un meilleur contrôle utilisateur (notamment via la gestion des animations).

### Évolutions fonctionnelles
- **Nouveautés** : Ajout du composant `DsfrShare`.
- **Accessibilité** : 
    - Amélioration de la visibilité du focus.
    - Nommage des boutons de fermeture pour les alertes.
    - Suppression de rôles ARIA redondants dans les groupes de boutons (Radios, Checkboxes).
    - Support du mode "réduction de mouvement" (`prefers-reduced-motion`) et ajout d'un bouton de pause pour les défilements automatiques.
- **Réactivité et synchronisation** : 
    - Plusieurs composants ont été rendus dynamiques (propriété `disabled`, langue active, sélection dans les listes et tableaux, pagination, etc.).
    - Synchronisation des valeurs et des alignements pour les composants `MultiSelect`, `DsfrSegmented`, `DsfrTable` et `DsfrUser`.
- **Expérience utilisateur (UX)** :
    - Optimisation de l'affichage et de la taille des éléments (icônes, titres, boutons) en fonction des points de rupture (responsive design) pour `LabAnssiCentreAide`, `LabAnssiBandeauPage` et `LabAnssiFonctionnalites`.
    - Ajout de slots de personnalisation pour les médias et les indices (`hint`) dans plusieurs composants.

### Évolutions techniques
- **Infrastructure & Build** : 
    - Migration vers **Vite 8** avec passage au format ESM et correction de l'injection du nonce CSP.
    - Optimisation du déploiement vers S3 avec l'application de politiques de cache.
- **Qualité & Tooling** :
    - Intégration de `svelte-check` pour renforcer la vérification des types.
    - Mise en conformité des stories Storybook avec les standards DSFR.
    - Consolidation de la configuration `pnpm` et utilisation du lockfile dans les workflows.
- **Refactoring** : 
    - Nettoyage de code "legacy" et suppression d'effets obsolètes dans les composants `CentreAide` et `PageCrisp`.
    - Remplacement des couleurs codées en dur par des variables CSS pour une meilleure personnalisation.

### Autres changements
- Mise à jour de la documentation concernant le processus de release.
- Ajout d'icônes manquantes (gamepad).
