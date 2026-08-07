## Changelog : ui-kit (30 derniers jours, au 06 août 2026)

### Résumé
Ce mois a été marqué par une transformation structurelle majeure avec l'intégration de la bibliothèque Cunningham React, faisant évoluer le projet vers une architecture monorepo. Parallèlement, l'expérience utilisateur a été enrichie par l'ajout de nouveaux composants (Alertes, gestion de fichiers) et une amélioration globale de l'accessibilité et de la précision des traductions.

### Évolutions fonctionnelles
- **Nouveaux composants** : ajout de la famille de composants pour l'import de fichiers, du composant `Alert` (avec support d'icônes personnalisées) et du `ShareImportModal` pour l'import de contacts.
- **Expérience de téléchargement** : refonte des états de la zone de dépôt (dropzone), stabilisation visuelle lors du glisser-déposer et amélioration des retours d'information (feedback) lors de l'import.
- **Interface et accessibilité** : mise à jour esthétique du `UserMenu`, du `ShareModal` et du `UserAvatar`, ainsi qu'une amélioration de l'accessibilité du composant `StorageGauge`.
- **Internationalisation** : complétion des traductions pour les modules d'import et de téléchargement.

### Évolutions techniques
- **Architecture et Migration** : intégration de la bibliothèque Cunningham React et de son moteur de tokens, avec une transition vers une structure monorepo utilisant Yarn et Turborepo.
- **Outils de migration** : mise à disposition d'une interface en ligne de commande (CLI) via `npx` et de codemods pour automatiser la migration des anciennes importations `@openfun/cunningham-*`.
- **Performance et Build** : optimisation du chargement via le support du tree-shaking et amélioration du pipeline CI/CD (tests des workspaces et déploiement automatisé de Storybook).
- **Qualité de code** : renforcement du typage (interdiction du type `any`), passage des dossiers de composants au format `kebab-case` et amélioration de la gestion des types pour les locales.

### Autres changements
- **Documentation** : mise à jour des guides sur les packages, les processus de release manuelle et les crédits du moteur UI Kit.
- **Nettoyage** : suppression des actifs (assets) et de l'identité visuelle (branding) obsolètes liés à Cunningham.
