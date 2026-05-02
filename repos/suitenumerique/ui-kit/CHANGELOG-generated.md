## Changelog : ui-kit (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, la bibliothèque ui-kit a connu une importante évolution avec l'ajout de nombreux nouveaux composants et fonctionnalités, notamment une gestion améliorée des icônes, des menus déroulants plus flexibles, et des composants pour l'affichage de l'utilisation du stockage et la collecte de feedback utilisateur. Des améliorations ont également été apportées à l'infrastructure de déploiement et à la documentation.

### Évolutions fonctionnelles
- Ajout de sous-menus, d'une variante "tiny" et de la possibilité de maintenir un menu déroulant ouvert pour le composant `DropdownMenu`.
- Implémentation d'un filtre déroulant avec recherche intégrée (`SearchFilter`).
- Nouveau composant `StorageGauge` pour visualiser l'utilisation du stockage.
- Ajout d'un formulaire de feedback (`FeedbackForm`).
- Nouveau composant `HelpMenu` avec icône.
- Ajout d'un support pour un pied de page dans le panneau latéral (`Layout`).
- Possibilité de maintenir les éléments ouverts dans le `ContextMenu`.
- Amélioration de la gestion des icônes avec la génération automatique de composants SVG à partir de Figma.
- Correction de l'affichage de l'icône dans le menu déroulant.
- Correction de l'emballage du libellé dans les conteneurs restreints du filtre.
- Correction d'erreurs de typage dans les stories du composant `Modal`.

### Évolutions techniques
- Ajout de scripts pour la génération de composants SVG à partir de fichiers Figma.
- Refonte de l'organisation des stories des icônes et exportation des icônes SVG.
- Mise à jour des fichiers de polices Marianne et du CSS associé.
- Ajout de la possibilité de déployer l'application sur Scalingo et configuration d'un environnement Docker local.
- Correction du chargement de la police Marianne sur Scalingo.
- Mise à jour des versions des paquets dans `package.json` et `yarn.lock`.
- Amélioration de la gestion des événements click dans le `ContextMenu` pour éviter les sélections fantômes.
- Mise à jour des étapes du workflow GitHub Actions vers les dernières versions.

### Autres changements
- Correction de fautes de frappe dans la documentation.
- Ajout de documentation sur le déploiement.
- Harmonisation des poids de police et des styles des zones de texte.
- Ajout de tokens pour le rayon de bordure des formulaires.
- Configuration de Renovate pour la gestion des dépendances.
- Publication de nouvelles versions du package.
