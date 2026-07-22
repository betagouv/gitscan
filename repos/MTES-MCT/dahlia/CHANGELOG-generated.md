## Changelog : dahlia (30 derniers jours, au 21 juillet 2026)

### Résumé
Les dernières mises à jour de Dahlia se concentrent sur l'amélioration des fonctionnalités existantes, notamment la gestion des pièces jointes, le scraping de données et l'affichage d'informations clés sur les dossiers. Des améliorations significatives ont également été apportées à l'infrastructure et à la configuration du projet, notamment la mise à jour des dépendances et l'optimisation de la CI/CD.

### Évolutions fonctionnelles
- Possibilité de télécharger plusieurs pièces jointes dans un dossier via une archive ZIP. [#64](https://github.com/MTES-MCT/dahlia/issues/64)
- Affichage du dernier jugement lié à un dossier, si disponible. [#78](https://github.com/MTES-MCT/dahlia/issues/78)
- Récupération de tous les acteurs liés à un dossier. [#79](https://github.com/MTES-MCT/dahlia/issues/79)
- Ajout d'un avertissement si la date limite de production d'un dossier est dépassée. [#80](https://github.com/MTES-MCT/dahlia/issues/80)
- Ajout d'un bouton pour télécharger la liste des dossiers. [#57](https://github.com/MTES-MCT/dahlia/issues/57)
- Amélioration de la gestion des tableaux. [#53](https://github.com/MTES-MCT/dahlia/issues/53)
- Ajout d'un formulaire pour éditer les métadonnées des pièces d'un dossier. [#51](https://github.com/MTES-MCT/dahlia/issues/51)
- Ajout de la colonne "dernier producteur" dans l'affichage des dossiers. [#44](https://github.com/MTES-MCT/dahlia/issues/44)
- Ajout de la date de délétion. [#40](https://github.com/MTES-MCT/dahlia/issues/40)
- Affichage des pièces anonymisées dans tous les environnements, pas seulement en production. [#55](https://github.com/MTES-MCT/dahlia/issues/55)

### Évolutions techniques
- Mise à jour de nombreuses dépendances (NextJS, React, TypeScript, Vite, PostCSS, etc.).
- Mise à jour de l'action `checkout` de GitHub. [#58](https://github.com/MTES-MCT/dahlia/issues/58)
- Pin de la version de l'action `pnpm/action-setup` en CI pour plus de stabilité. [#68](https://github.com/MTES-MCT/dahlia/issues/68)
- Ajout d'un hook de precommit pour garantir la qualité du code. [#75](https://github.com/MTES-MCT/dahlia/issues/75)
- Amélioration de la configuration de Dependabot pour une gestion plus efficace des mises à jour de dépendances. [#30](https://github.com/MTES-MCT/dahlia/issues/30)
- Refonte du scrapping et de la gestion des dates de mise à jour. [#66](https://github.com/MTES-MCT/dahlia/issues/66)
- Réorganisation des tests unitaires et d'intégration. [#56](https://github.com/MTES-MCT/dahlia/issues/56)
- Renommage du dossier. [#81](https://github.com/MTES-MCT/dahlia/issues/81)
- Remplacement de `vs` par `c/` dans le code. [#82](https://github.com/MTES-MCT/dahlia/issues/82)

### Autres changements
- Mise à jour de la documentation INVESTIGATION. [#37](https://github.com/MTES-MCT/dahlia/issues/37)
- Ajout de permissions dans la CI. [#48](https://github.com/MTES-MCT/dahlia/issues/48)
- Ajustement des interfaces. [#74](https://github.com/MTES-MCT/dahlia/issues/74)
- Ajout de fichiers anonymisés préparés par l'équipe. [#76](https://github.com/MTES-MCT/dahlia/issues/76)
- Ajout d'un script pour créer des dossiers inscrits au rôle d'une audience. [#77](https://github.com/MTES-MCT/dahlia/issues/77)
