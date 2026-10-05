## Changelog : ui-kit (30 derniers jours, au 28 septembre 2026)

### Résumé
Ce mois-ci, le design system s'enrichit de nouveaux éléments d'interface, notamment des bannières et des options de personnalisation pour les menus. Les outils de développement ont également été améliorés pour offrir une meilleure expérience de test et de prévisualisation, tout en optimisant la réactivité de l'interface.

### Évolutions fonctionnelles
- Ajout de nouveaux éléments d'interface : composant `HeaderBanner` et intégration d'un emplacement (`slot`) `topBanner` dans le `MainLayout`.
- Enrichissement du `ContextMenu` avec l'ajout de la propriété `isChecked` pour les éléments de menu.
- Amélioration de la flexibilité du `ShareModal` permettant l'extension de `SharedItemRow`.
- Ajout de nouveaux tokens de design pour renforcer la cohérence visuelle.
- Correction de problèmes de mise en page (layout) sur le composant `Modal`.

### Évolutions techniques
- Amélioration de l'expérience de développement dans Storybook : ajout d'un sélecteur de thème et persistance de la langue sélectionnée lors de la navigation entre les composants et la documentation.
- Optimisation des performances de l'interface responsive via l'ajout d'un mécanisme de "debounce" sur les écouteurs d'événements de redimensionnement.
- Refactorisation des hooks de calendrier pour centraliser l'utilisation de `react-aria`.
- Mise à jour de l'environnement d'exécution vers Node 24.

### Autres changements
- Nettoyage du fichier CHANGELOG.
