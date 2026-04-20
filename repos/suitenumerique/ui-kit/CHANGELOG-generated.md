## Changelog : ui-kit (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, l'équipe a apporté des améliorations significatives à la bibliothèque d'icônes, en automatisant leur génération à partir de Figma et en ajoutant un nouveau composant wrapper. De nouvelles fonctionnalités ont été ajoutées aux menus déroulants et contextuels, ainsi que de nouveaux composants pour la gestion du stockage, les formulaires de feedback et l'aide utilisateur. Des corrections de bugs et des améliorations de l'accessibilité ont également été implémentées.

### Évolutions fonctionnelles
- Ajout de sous-menus, d'une variante "tiny" et de la possibilité de maintenir les menus déroulants ouverts pour le composant `DropdownMenu`.
- Implémentation d'un filtre déroulant avec recherche intégrée (`SearchFilter`).
- Ajout d'un composant de visualisation de l'utilisation du stockage (`StorageGauge`).
- Nouveau composant de formulaire de feedback (`FeedbackForm`).
- Ajout d'un menu d'aide avec un composant icône (`HelpMenu`).
- Amélioration de la gestion du focus et de la sémantique des menus déroulants.
- Correction d'un problème de sélection fantôme entre les nœuds dans les arbres.
- Masquage de l'icône "waffle" des lecteurs d'écran pour améliorer l'accessibilité.
- Ajout de la possibilité de maintenir les éléments du menu contextuel ouverts (`keepOpen`).
- Ajout du support du footer dans le panneau de gauche (`Layout`).

### Évolutions techniques
- Automatisation de la génération des composants SVG d'icônes à partir de Figma via un script dédié.
- Création d'un composant wrapper `IconSvg` pour les icônes SVG.
- Refonte de l'organisation des stories des icônes.
- Ajout du support de déploiement sur Scalingo et configuration d'un environnement Docker local.
- Correction du chargement de la police Marianne sur Scalingo.
- Mise à jour des fichiers de police Marianne et du CSS associé.
- Harmonisation des poids de police et des styles des textarea.
- Correction d'une erreur de type dans les stories du composant `Modal` grâce à l'utilisation d'une union discriminée.

### Autres changements
- Ajout de documentation sur le déploiement.
- Mise à jour des versions des paquets dans `package.json` et `yarn.lock`.
- Amélioration du layout des stories du composant `AllIcons`.
- Correction d'une erreur de lint dans les stories du composant `IconSvg`.
- Mise à jour du changelog.
- Ajout de variables pour le `border-radius` des formulaires et correction des poids de police.
