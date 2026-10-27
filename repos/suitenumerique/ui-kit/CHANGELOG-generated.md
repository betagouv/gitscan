## Changelog : ui-kit (30 derniers jours, au 26 octobre 2026)

### Résumé
Ce mois-ci, le design system s'enrichit de nouveaux composants, notamment une barre de progression et des onglets plus accessibles. Nous avons également amélioré la gestion du partage de fichiers et affiné l'apparence de certains éléments visuels pour garantir une interface plus cohérente et robuste.

### Évolutions fonctionnelles
- **Nouveaux composants** : Ajout du composant `ProgressBar` et amélioration du composant `Tabs` (nouvelles variantes accessibles et gestion de la sélection contrôlée).
- **Partage de fichiers** : Introduction de l'expiration des liens de partage et simplification de l'interface de gestion des accès aux dossiers dans le `ShareModal`.
- **Interface utilisateur** : 
    - Mise à jour visuelle du composant `Alert` pour s'aligner sur les nouveaux tokens de design.
    - Amélioration de la gestion des accès refusés dans le mode prévisualisation.
    - Correction de problèmes de mise en page sur le composant `Modal`.

### Évolutions techniques
- **Refonte de composants** : Reconstruction du composant `Toast` basée sur `react-toastify` et refactorisation de l' `Alert` pour une meilleure modularité (extraction de `NotificationContent`).
- **Fiabilité des tests** : 
    - Stabilisation des tests de tri pour le `SimpleDataGrid`.
    - Amélioration de la robustesse des tests E2E (synchronisation des défilements de page).
    - Intégration des matchers `jest-dom` dans l'environnement de test Vitest.
- **Internationalisation** : Optimisation du système de traduction pour permettre le remplacement de variables dans les traductions personnalisées.

### Autres changements
- **Documentation** : Ajout d'exemples d'utilisation et de précisions sur l'expiration des liens pour le `ShareModal`.
- **Maintenance** : Publication de la version `ui-components` 1.3.0 et nettoyage du fichier CHANGELOG.
