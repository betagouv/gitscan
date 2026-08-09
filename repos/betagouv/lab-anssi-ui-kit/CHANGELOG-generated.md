## Changelog : lab-anssi-ui-kit (30 derniers jours, au 07/08/2026)

### Résumé
Ce mois-ci, la bibliothèque s'enrichit de nouveaux composants essentiels, tels que les fenêtres modales et les infobulles, tout en renforçant la cohérence de l'ensemble avec le Design System de l'État (DSFR). Les composants existants ont été améliorés pour offrir plus de flexibilité et une meilleure accessibilité, garantissant une expérience utilisateur plus fluide et conforme aux standards.

### Évolutions fonctionnelles

**Nouveaux composants**
- Ajout du composant `DsfrModal` incluant la gestion du focus (`trapFocus`) pour l'accessibilité.
- Ajout du composant `DsfrTooltip` (infobulles).
- Ajout du composant `Bloc Fonctionnalités` pour la gamme Lab ANSSI.

**Améliorations des composants existants**
- **DSFR** :
    - `DsfrButton` : ajout de nouvelles variations (inversé tertiaire et tertiaire sans bordure).
    - `DsfrConnect` : ajout de l'attribut `disabled` sur les liens.
    - `DsfrTagsGroup` : définition d'une valeur par défaut pour la propriété `groupMarkup`.
    - `DsfrCallout` : le label du bouton est désormais optionnel.
- **Lab ANSSI** :
    - `LabAnssiBandeauPage` : ajout des propriétés `theme` et `type`.
    - `CarrouselTuiles` et `Marelle` : mise en conformité avec le DSFR.
    - `Marelle` : amélioration de la flexibilité des étapes via l'utilisation de slots.

### Évolutions techniques
- **Infrastructure et outils** :
    - Mise à jour majeure de Storybook vers la version 10.5.0.
    - Mise à jour de PNPM vers la version 11.17.0.
    - Stabilisation de l'environnement de développement en figeant la version de Node.js sur la dernière version LTS (24.18.0).
    - Optimisation de la configuration du workspace pnpm (`allowBuilds` pour `@parcel/watcher` et `esbuild`).
- **Versions** : Passage aux versions 1.56.0, 1.57.0 et 1.58.0.

### Autres changements
- **Documentation et Storybook** :
    - Réorganisation complète de l'arborescence des titres pour les composants Lab ANSSI et DSFR dans Storybook.
    - Nettoyage de l'interface Storybook (suppression des options de tri).
    - Amélioration des stories pour les composants `LabAnssiBandeauPage` et `DsfrSelect`.
- **Configuration** :
    - Optimisation de la configuration de Renovate (mise en place de règles de groupe et de préfixes de commit).
