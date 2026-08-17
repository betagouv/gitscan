## Changelog : lab-anssi-ui-kit (30 derniers jours, au 13 août 2026)

### Résumé
Cette période est marquée par une montée en version importante (jusqu'à la v1.59.0) et l'enrichissement de la bibliothèque. De nouveaux composants ont été ajoutés (Modale, Tooltip, Bloc Fonctionnalités) et plusieurs composants existants ont été mis en conformité avec le DSFR pour garantir une meilleure cohérence visuelle et fonctionnelle.

### Évolutions fonctionnelles

**Nouveaux composants**
- Ajout du composant `DsfrModal` avec gestion du focus.
- Ajout du composant `DsfrTooltip`.
- Ajout du composant `LabAnssiBlocFonctionnalites`.

**Améliorations et conformité DSFR**
- Mise en conformité avec le DSFR des composants `LabAnssiCentreAide`, `LabAnssiCarrouselTuiles` et `LabAnssiMarelle`.
- `DsfrButton` : ajout de nouvelles variations de boutons tertiaires inversés et sans bordure.
- `DsfrCard` : ajout de la propriété `noIcon` pour masquer l'icône du lien.
- `DsfrConnect` : ajout de l'attribut `disabled` sur le lien.
- `DsfrCallout` : le label du bouton est désormais optionnel.
- `DsfrTagsGroup` : définition d'une valeur par défaut pour la propriété `groupMarkup`.
- `DsfrHeader` : ajout d'un slot `afternavigation`.

**Personnalisation et Design**
- `LabAnssiBandeauPage` : ajout des propriétés `theme` et `type`, et support de couleurs de fond personnalisées.
- `LabAnssiFonctionnalites` : amélioration des styles du chapeau et de la couleur de la description.
- `LabAnssiMarelleEtape` : ajout d'une couleur par défaut pour le fond des cercles d'étape.

**Adaptabilité (Responsive)**
- `LabAnssiBandeauPage` : modification du point de rupture (passage de `md` à `lg`).
- `LabAnssiCarrouselTuiles` : modification du point de rupture (passage de `md` à `sm`).

### Évolutions techniques

**Infrastructure et Outillage**
- Mise à jour de Storybook vers la version 10.5.0.
- Mise à jour de PNPM vers la version 11.17.0.
- Stabilisation de l'environnement avec le figement de la version Node.js sur la dernière version LTS (24.18.0).
- Optimisation de la configuration de build pour `@parcel/watcher` et `esbuild`.

**Architecture et Code**
- Implémentation et amélioration de la directive `trapFocus` pour la gestion de l'accessibilité dans les modales.
- `LabAnssiCarrouselTuiles` : les propriétés `contenu` et `illustration` sont désormais optionnelles.

### Autres changements

**Documentation et Storybook**
- Correction de l'affichage de la couleur de fond personnalisée dans la documentation de `LabAnssiBandeauPage`.
- Réorganisation des stories du LAB dans un dossier `legacy`.
- Correction d'un chemin d'importation dans Storybook (`generateurImagesPlaceholders.js`).
