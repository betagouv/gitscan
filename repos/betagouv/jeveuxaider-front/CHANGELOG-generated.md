## Changelog : jeveuxaider-front (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur, notamment en ajoutant de nouvelles fonctionnalités pour la campagne d'été, en optimisant la recherche de missions et en améliorant la gestion des organisations. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Ajout d'un lien vers la page "Canicule" dans la navigation principale, tant sur desktop que mobile. [#348](https://github.com/betagouv/jeveuxaider-front/issues/348)
- Amélioration de la gestion des inscriptions aux missions, avec un changement de libellé de "Fermer les inscriptions" à "Mettre en pause les inscriptions".
- Amélioration de l'interface pour l'ajout de ressources, avec un formulaire complet incluant la validation, le téléchargement de médias et la gestion des rôles. [#342](https://github.com/betagouv/jeveuxaider-front/issues/342)
- Amélioration de l'interface pour la création de modèles de messages, avec un formulaire complet incluant la validation et la gestion des rôles utilisateurs. [#340](https://github.com/betagouv/jeveuxaider-front/issues/340)
- Mise à jour des informations de la campagne d'été dans les composants "MissionInfos" et "Section". [#341](https://github.com/betagouv/jeveuxaider-front/issues/341)
- Amélioration du filtre de localisation avec des options de rayon mises à jour, incluant 0 et 1000. [#337](https://github.com/betagouv/jeveuxaider-front/issues/337)
- Possibilité pour les organisations de se désinscrire de manière autonome. [#322](https://github.com/betagouv/jeveuxaider-front/issues/322)
- Amélioration de la participation au tirage au sort pour les utilisateurs non-gestionnaires. [#343](https://github.com/betagouv/jeveuxaider-front/issues/343)
- Ajout de filtres pour les notes autres que les "mines". [#328](https://github.com/betagouv/jeveuxaider-front/issues/328)
- Ajout de champs supplémentaires dans les exports de données. [#327](https://github.com/betagouv/jeveuxaider-front/issues/327)

### Évolutions techniques
- Mise à jour de la librairie Plausible Statistics pour utiliser l'API v2 et correction d'un filtre de date incorrect. [#344](https://github.com/betagouv/jeveuxaider-front/issues/344)
- Refactorisation du composant `statistics` pour supprimer les props inutilisés et simplifier la logique des paramètres de requête. [#339](https://github.com/betagouv/jeveuxaider-front/issues/339)
- Optimisation de l'inclusion des dépendances dans la configuration Nuxt pour éviter les rechargements en développement. [#336](https://github.com/betagouv/jeveuxaider-front/issues/336)
- Correction de l'affichage du nom au lieu de la clé dans les statistiques des visites. [#337](https://github.com/betagouv/jeveuxaider-front/issues/337)
- Correction d'un problème d'attributs avec un tiret dans le composant `FormControl` pour assurer la compatibilité avec les standards HTML. [#349](https://github.com/betagouv/jeveuxaider-front/issues/349)
- Amélioration du support de la géolocalisation pour les villes multidistribuées, avec l'ajout de Saint-Paul et Avignon. [#330](https://github.com/betagouv/jeveuxaider-front/issues/330)

### Autres changements
- Mise à jour de plusieurs dépendances (qs, nitropack, axios, fast-uri, simple-git, fast-xml-builder, postcss, fast-xml-parser, uuid) pour bénéficier des dernières corrections et améliorations.
- Suppression du composable `useAutocompleteSuggestions`. [#340](https://github.com/betagouv/jeveuxaider-front/issues/340)
- Ajout de dépendances manquantes pour les graphiques (chartjs-plugin-annotation et chartjs-plugin-datalabels). [#335](https://github.com/betagouv/jeveuxaider-front/issues/335)
