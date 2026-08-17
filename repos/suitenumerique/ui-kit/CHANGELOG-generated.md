## Changelog : ui-kit (30 derniers jours, au 10/08/2026)

### Résumé
Ce mois a marqué une étape majeure avec la fusion de la bibliothèque Cunningham React au sein du monorepo `ui-kit`. Cette transition a permis de consolider l'ensemble des composants, d'améliorer l'expérience de téléchargement de fichiers et d'introduire de nouveaux éléments d'interface comme des alertes personnalisées et des modules d'importation de contacts optimisés.

### Évolutions fonctionnelles
- **Nouveaux composants** : Ajout de la famille de composants pour l'import de fichiers, du composant `Alert` (avec support d'icônes personnalisées) et du `ShareImportModal` pour l'import de contacts.
- **Améliorations de l'interface (UI/UX)** : 
    - Refonte des états de la zone de dépôt (*dropzone*) du téléchargeur de fichiers pour une meilleure interactivité.
    - Modernisation du style du `UserMenu`, de l'avatar utilisateur (ajout de dégradés) et du `ShareModal`.
    - Ajout d'une variante "inline" pour les champs de formulaire.
- **Corrections et contenu** : 
    - Amélioration des traductions pour les modules d'importation et de téléchargement.
    - Correction de la terminologie (utilisation de "XLSX" au lieu de "XLS").
    - Stabilisation de la taille de la zone de dépôt lors du glisser-déposer.

### Évolutions techniques
- **Architecture et Monorepo** : Migration vers une structure monorepo gérée par Yarn et Turborepo, incluant la fusion de la bibliothèque Cunningham React et la restructuration des packages (déplacement des sources vers le package `components`).
- **Outils de migration** : Création d'une interface en ligne de commande (CLI) via `npx` et de *codemods* pour automatiser la migration des anciens imports `@openfun/cunningham-*`.
- **Optimisation et Qualité** : 
    - Support du *tree-shaking* pour réduire la taille des bundles.
    - Renforcement du typage TypeScript (interdiction de l'usage de `any`).
    - Renommage des dossiers de composants en `kebab-case` pour la cohérence.
- **CI/CD et Tests** : Amélioration du déploiement de Storybook, stabilisation des tests de composants et automatisation des tests sur l'ensemble des espaces de travail (*workspaces*).
- **Release** : Publication de la version 1.0.0 de `ui-components`.

### Autres changements
- **Documentation** : Mise à jour de la documentation concernant les packages, les processus de release manuelle et l'utilisation des icônes Material.
- **Nettoyage** : Suppression des actifs de marque (*branding*) et des exports Sass obsolètes issus de l'ancienne bibliothèque.
