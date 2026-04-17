## Changelog : ui-kit (30 derniers jours, au 3 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur avec l'ajout de nouveaux composants comme des menus déroulants avec sous-menus, des jauges d'utilisation du stockage et un formulaire de feedback. Des améliorations ont également été apportées aux icônes, aux polices et à la gestion de l'accessibilité. Enfin, des outils de déploiement et de génération d'icônes SVG ont été ajoutés pour faciliter le développement et la maintenance du projet.

### Évolutions fonctionnelles
- Ajout de sous-menus, d'une variante "tiny" et de la possibilité de maintenir les menus déroulants ouverts pour le composant `DropdownMenu` [#fd17ed1](https://github.com/suitenumerique/ui-kit/commit/fd17ed1).
- Implémentation d'un filtre de recherche dans les menus déroulants (`SearchFilter`) [#eee1928](https://github.com/suitenumerique/ui-kit/commit/eee1928).
- Ajout d'un composant de visualisation de l'utilisation du stockage (`StorageGauge`) [#376b582](https://github.com/suitenumerique/ui-kit/commit/376b582).
- Nouveau composant de formulaire de feedback (`FeedbackForm`) [#6b44533](https://github.com/suitenumerique/ui-kit/commit/6b44533).
- Ajout d'un menu d'aide avec un composant icône (`HelpMenu`) [#01fe3fe](https://github.com/suitenumerique/ui-kit/commit/01fe3fe).
- Support du footer dans le panneau latéral (`layout`) [#873f83e](https://github.com/suitenumerique/ui-kit/commit/873f83e).
- Possibilité de maintenir les éléments ouverts dans le menu contextuel (`ContextMenu`) [#7e838df](https://github.com/suitenumerique/ui-kit/commit/7e838df).
- Correction d'un problème de sélection fantôme entre les nœuds dans l'interface utilisateur [#345e918](https://github.com/suitenumerique/ui-kit/commit/345e918).
- Amélioration de l'accessibilité en masquant l'icône waffle des lecteurs d'écran [#3b50700](https://github.com/suitenumerique/ui-kit/commit/3b50700).

### Évolutions techniques
- Ajout d'un script de génération d'icônes SVG à partir de Figma [#bd5ec5e](https://github.com/suitenumerique/ui-kit/commit/bd5ec5e).
- Création d'un composant wrapper `IconSvg` pour les icônes SVG [#378cb38](https://github.com/suitenumerique/ui-kit/commit/378cb38).
- Génération automatique de composants d'icônes SVG [#edf722a](https://github.com/suitenumerique/ui-kit/commit/edf722a).
- Refonte de l'organisation des stories et exportation des icônes SVG [#852e3a2](https://github.com/suitenumerique/ui-kit/commit/852e3a2).
- Mise en place d'un déploiement sur Scalingo et d'un environnement Docker local [#c0083ea](https://github.com/suitenumerique/ui-kit/commit/c0083ea).
- Correction du chargement de la police Marianne sur Scalingo [#1e0a305](https://github.com/suitenumerique/ui-kit/commit/1e0a305).
- Mise à jour des fichiers de police Marianne et du CSS associé [#f3fc147](https://github.com/suitenumerique/ui-kit/commit/f3fc147).
- Harmonisation des poids de police et des styles textarea [#8a5e7e7](https://github.com/suitenumerique/ui-kit/commit/8a5e7e7).
- Correction d'une erreur de lint dans les stories `IconSvg` [#fc3b7e3](https://github.com/suitenumerique/ui-kit/commit/fc3b7e3).
- Correction d'une erreur de type dans les stories du composant `Modal` [#ce36a66](https://github.com/suitenumerique/ui-kit/commit/ce36a66).

### Autres changements
- Ajout de documentation sur le déploiement [#e249727](https://github.com/suitenumerique/ui-kit/commit/e249727).
- Amélioration de la mise en page des stories du composant `AllIcons` [#144d463](https://github.com/suitenumerique/ui-kit/commit/144d463).
- Mise à jour de la version du package [#b09f605](https://github.com/suitenumerique/ui-kit/commit/b09f605).
- Mise à jour des tokens de style (bordure des formulaires, poids des polices) [#db7bb76](https://github.com/suitenumerique/ui-kit/commit/db7bb76).
- Mise à jour des versions des paquets dans `package.json` et `yarn.lock` [#5402e2b](https://github.com/suitenumerique/ui-kit/commit/5402e2b).
- Publication de la version `0.20.0` du package [#b09f605](https://github.com/suitenumerique/ui-kit/commit/b09f605).
