## Changelog : ui-kit (30 derniers jours, au 23 octobre 2026)

### Résumé
Ce mois-ci, le design system s'enrichit de nouveaux composants (barre de progression, notifications) et de mises à jour visuelles pour les alertes. Les efforts se sont également concentrés sur l'accessibilité des onglets, la fiabilité des tests automatisés et une expérience utilisateur plus fluide lors de la gestion des accès aux dossiers.

### Évolutions fonctionnelles
- **Nouveaux composants et refontes** :
  - Ajout du composant `ProgressBar`.
  - Refonte complète du composant `Toast` (basée sur `react-toastify`).
  - Mise à jour du design du composant `Alert` avec l'application des nouveaux tokens.
- **Améliorations des composants existants** :
  - `Tabs` : Ajout de variantes accessibles et de la gestion de sélection contrôlée.
  - `Modal` : Correction de problèmes de mise en page.
- **Expérience utilisateur (UX)** :
  - Amélioration de la gestion des accès aux dossiers (affichage immédiat de l'accès refusé sans chargement de contenu inutile).
  - Simplification de la gestion d'état du modal de partage.
  - Optimisation de la synchronisation du défilement lors de la saisie de texte dans les modes de prévisualisation.

### Évolutions techniques
- **Tests et fiabilité** :
  - Stabilisation des tests de tri pour le composant `SimpleDataGrid`.
  - Amélioration des tests de bout en bout (E2E) pour mieux gérer les sauts de page et les contenus de tailles variables.
  - Intégration des matchers `jest-dom` dans l'environnement de test Vitest.
- **Architecture et Refactoring** :
  - Restructuration du composant `Alert` via l'extraction de `NotificationContent`.
- **CI/CD** :
  - Standardisation de la configuration de la CI en utilisant les presets par défaut de la Suite numérique.

### Autres changements
- Publication de la version `ui-components` 1.3.0.
- Nettoyage du fichier CHANGELOG.
