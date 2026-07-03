## Changelog : lab-anssi-ui-kit (30 derniers jours, au 01 juillet 2026)

### Résumé
Ce mois-ci, l'équipe a continué d'améliorer et d'étendre la bibliothèque de composants, en se concentrant sur l'ajout de nouvelles fonctionnalités aux composants existants, l'amélioration de l'accessibilité et la correction de bugs. Plusieurs composants ont été mis à jour pour correspondre plus précisément aux spécifications du DSFR et offrir une plus grande flexibilité aux développeurs.

### Évolutions fonctionnelles
- **DsfrRange:** Ajout de la prise en charge de `box-sizing` pour une meilleure gestion de la mise en page.
- **DsfrTabnav:** Possibilité de définir des slots pour les liens du composant, offrant plus de contrôle sur leur contenu.
- **DsfrCheckboxesGroup & DsfrRadiosGroup:** Ajout de la prise en charge de la taille et de la graisse pour les légendes, améliorant la lisibilité et l'accessibilité.
- **DsfrLabel:** Ajout du composant `DsfrLabel` pour une meilleure sémantique et accessibilité. Remplacement de l'utilisation directe de la balise `<label>` par ce nouveau composant dans l'ensemble du code.
- **DsfrInput:** Ajout de variations 'addon' (avec un bouton submit associé) et 'action' (avec un bouton d'action associé) pour plus de flexibilité. Factorisation du code pour une meilleure maintenabilité.
- **DsfrAlert:** Ajout de la prop `titleTag` pour personnaliser la balise HTML du titre de l'alerte. Amélioration de la logique d'affichage du titre et de la description en fonction de la taille de l'alerte.
- **DsfrTile:** Ajout de la prop `noIcon` pour masquer l'icône associée au lien.
- **DsfrTable:** Ajout de la gestion des lignes désactivées et d'une action pour gérer la propriété `--row-height`. Ajout d'une story d'exemple pour les tableaux avec lignes désactivées.
- **DsfrToggle:** Ajout de la propriété `hideLabel` pour masquer le label et correction de l'affichage de l'état "checked".
- **DsfrDropdown:** Ajout de la prop `disabled` pour désactiver le bouton d'ouverture et correction de l'alignement à droite du menu déroulant.

### Évolutions techniques
- **Gestion des événements:** Uniformisation de la façon de déclarer les `CustomEvent` et ajout des événements émis par les composants en tant qu'attributs des éléments.
- **Génération de `web-types`:** Ajout d'un fichier `web-types` pour améliorer l'intégration avec les éditeurs de code.
- **Storybook:** Ajout de la déclaration du dossier statique pour Storybook.
- **CI/CD:** Mise à jour de l'étape de checkout dans le workflow CI pour utiliser la référence du dépôt et un `fetch-depth` de 0.
- **Dépendances:** Mise à jour des versions de plusieurs dépendances (Vitest, Storybook, eslint, etc.).
- **Thèmes MSC:** Ajout des couleurs `hover` et `active` pour le composant `DsfrTag`.

### Autres changements
- **Documentation:** Amélioration de l'organisation des stories d'exemples. Ajout des URLs de documentation pour chaque composant.
- **Version:** Passage à la version 1.55.0, puis 1.54.2, 1.54.1, 1.54.0 et 1.53.4.
- **PrésentationANSSI:** Uniformisation de la structure et du style du composant `PresentationANSSI` avec les éléments du DSFR.
- **Configuration:** Mise à jour du fichier `renovate.json`.
- **Corrections:** Correction de la création du dossier `/dist` dans le workflow CI.
