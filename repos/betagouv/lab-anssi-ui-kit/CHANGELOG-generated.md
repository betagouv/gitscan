## Changelog : lab-anssi-ui-kit (30 derniers jours, au 18 septembre 2026)

### Résumé
Ce mois a été marqué par une montée en version majeure de l'infrastructure de build (Vite 8) et un travail important de fiabilisation des composants. La bibliothèque gagne en réactivité et en accessibilité, avec l'ajout de nouveaux éléments (composant de partage, nouvelles icônes) et une meilleure gestion des états pour de nombreux composants existants.

### Évolutions fonctionnelles
- **Nouveautés et composants**
  - Ajout du composant `DsfrShare` (partage).
  - Ajout d'un slot 'hint' pour le composant `DsfrToggle`.
  - Ajout de nouvelles icônes (notamment l'icône gamepad).
- **Améliorations de l'expérience et de l'accessibilité**
  - **Réactivité accrue** : Plusieurs composants ont été optimisés pour une meilleure synchronisation de leurs états (langue pour `DsfrTranslate`, pagination pour `DsfrTable`, sélection pour `MultiSelect`, valeur active pour `DsfrSegmented`, etc.).
  - **Accessibilité** : Amélioration de la visibilité du focus, nommage des boutons de fermeture pour les alertes et suppression de rôles ARIA redondants sur les groupes de cases à cocher et de boutons radio.
  - **Interface et Responsive** : Ajustements visuels sur les points de rupture (padding, position des icônes) et meilleure gestion de la taille des icônes en fonction du texte.
- **Corrections**
  - Correction d'un bug d'affichage mobile sur la variation sans image du `LabAnssiBandeauPage`.
  - Résolution de problèmes de navigation et de recherche dans le composant `DsfrDropdown`.

### Évolutions techniques
- **Infrastructure et Build**
  - Migration vers **Vite 8**, incluant le passage aux modules ESM et la correction de l'injection du nonce CSP.
  - Consolidation de la configuration `pnpm` et utilisation systématique du lockfile.
- **Qualité et Outillage**
  - Intégration de `svelte-check` pour renforcer la vérification des types.
  - Optimisation de la gestion des dépendances et de la configuration de mise à jour.
  - Nettoyage des logs de build (filtrage des warnings Vite).
- **Refactoring et Sécurité**
  - Renforcement de la sécurité via la correction de violations CSP sur la navigation du header.
  - Suppression de blocs de code "legacy" dans les composants `CentreAide` et `PageCrisp`.
  - Élargissement de la version supportée de Svelte en `peerDependency`.

### Autres changements
- **Storybook** : Mise en conformité des stories avec les standards du DSFR et correction de bugs de mutation d'état et de chemins d'images.
- **Maintenance** : Mise à jour de la documentation du processus de release et du formatage des fichiers (Prettier).
