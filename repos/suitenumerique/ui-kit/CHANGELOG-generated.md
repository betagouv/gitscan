## Changelog : ui-kit (30 derniers jours, au 27 avril 2026)

### Résumé
Cette version apporte des améliorations significatives à la bibliothèque, notamment de nouveaux composants pour la gestion des icônes, des menus déroulants, des filtres, et des indicateurs d'utilisation de stockage. Des améliorations de l'accessibilité et de l'expérience utilisateur ont également été apportées, ainsi que des corrections de bugs et des optimisations de performance. L'ajout de scripts pour la génération d'icônes SVG à partir de Figma facilite l'intégration de nouvelles icônes.

### Évolutions fonctionnelles
- Ajout de composants pour les sous-menus et une variante "tiny" aux menus déroulants, avec la possibilité de les maintenir ouverts [#190](https://github.com/suitenumerique/ui-kit/issues/190).
- Implémentation d'un filtre déroulant avec une fonctionnalité de recherche.
- Ajout d'un indicateur d'utilisation du stockage.
- Nouveau composant de formulaire de feedback.
- Ajout d'un menu d'aide avec un composant d'icône.
- Ajout d'un support pour le pied de page dans le panneau gauche.
- Possibilité de maintenir les éléments ouverts dans le menu contextuel.
- Génération automatique de composants d'icônes SVG à partir de fichiers Figma, avec un composant wrapper `IconSvg`.
- Amélioration de la présentation des icônes dans Storybook.
- Correction d'un problème d'enveloppement de texte dans les étiquettes des filtres.

### Évolutions techniques
- Mise à jour des fichiers de police Marianne.
- Ajout de la configuration Renovate pour la gestion des dépendances.
- Mise à jour des étapes du workflow GitHub Actions vers les dernières versions.
- Ajout du support pour le déploiement sur Scalingo et un environnement Docker local.
- Correction du chargement de la police Marianne sur Scalingo.
- Refactorisation et organisation des stories des icônes.
- Mise à jour des versions des paquets dans `package.json` et `yarn.lock`.
- Harmonisation des poids de police et des styles des zones de texte.
- Correction d'erreurs de linting dans les stories des icônes.

### Autres changements
- Correction de fautes de frappe dans la documentation.
- Ajout de documentation sur le déploiement.
- Publication d'une nouvelle version du package.
- Correction d'une erreur de type dans les stories de la modale.
- Ajout de tokens pour le rayon de bordure des formulaires et correction des poids de police.
