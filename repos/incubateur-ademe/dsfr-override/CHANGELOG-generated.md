## Changelog : dsfr-override (30 derniers jours, au 09 mai 2026)

### Résumé
Ce mois-ci, le projet a connu une transformation majeure avec la migration complète vers TypeScript et le développement d'une interface utilisateur (Builder UI) pour faciliter la personnalisation du Design System Français de Référence (DSFR). L'objectif est de permettre aux utilisateurs de modifier et de prévisualiser les styles du DSFR de manière intuitive, tout en automatisant le processus de génération des overrides SCSS. De nombreuses améliorations ont été apportées à la documentation et aux outils de construction.

### Évolutions fonctionnelles
- **Builder UI :** Ajout d'une interface utilisateur complète pour l'édition visuelle du mapping du DSFR, avec aperçu en direct des modifications. Cela inclut :
    - Éditeur de palette de couleurs LCh avec aperçu.
    - Autocomplétion pour les polices et les icônes.
    - Gestion des thèmes clair et sombre.
    - Possibilité d'ajouter des overrides manuels.
    - Galerie d'éléments pour visualiser les changements.
- **Icônes :** Intégration de Lucide Static pour la gestion des icônes, avec possibilité de les overrider via le mapping.
- **Exemple d'utilisation :** Ajout d'un exemple concret avec un bandeau de consentement RGPD utilisant les composants DSFR.
- **Documentation :** Refonte complète de la documentation avec un guide d'utilisation du Builder UI et des exemples.
- **Génération de fichiers :** Amélioration de la génération des fichiers SCSS avec prise en charge des polices, des ombres et des rayons de bordure.

### Évolutions techniques
- **Migration TypeScript :** Conversion complète du code source en TypeScript pour une meilleure maintenabilité et une plus grande robustesse.
- **Pipeline PostCSS :** Mise en place d'un pipeline PostCSS pour optimiser le code CSS généré (mqpacker, dedup, ajout de bannières ADEME).
- **Intégration Storybook :** Configuration de Storybook pour visualiser et tester les composants du DSFR avec les overrides.
- **CI/CD :** Amélioration du pipeline CI/CD pour automatiser la construction, les tests et le déploiement du Builder UI sur GitHub Pages.
- **Refactoring :** Refactorisation du code pour améliorer la structure et la lisibilité.
- **Outils de construction :** Mise à jour et amélioration des outils de construction (pnpm, sass).

### Autres changements
- Ajout d'une licence MIT.
- Nettoyage du code et suppression des références aux anciennes routes API.
- Mise à jour de la documentation concernant les assets tiers.
- Correction de bugs mineurs et améliorations de la performance.
- Ajout de tests unitaires pour valider le mapping, l'accessibilité et le processus de génération.
- Configuration de gitignore pour exclure les fichiers inutiles.
