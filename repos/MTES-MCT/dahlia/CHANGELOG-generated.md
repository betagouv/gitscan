## Changelog : dahlia (30 derniers jours, au 18 juillet 2026)

### Résumé
Les dernières mises à jour de Dahlia se concentrent sur l'amélioration de la gestion des dossiers, des pièces jointes et de l'expérience utilisateur globale. Des améliorations significatives ont été apportées au scrapping, à la recherche, au tri, et à la gestion des fichiers, ainsi qu'à la configuration de l'environnement de développement et de la CI/CD.

### Évolutions fonctionnelles
- Ajout d'un avertissement si la date limite de production est dépassée. [#80](https://github.com/MTES-MCT/dahlia/issues/80)
- Récupération de tous les acteurs liés à un dossier. [#79](https://github.com/MTES-MCT/dahlia/issues/79)
- Affichage du dernier jugement si disponible. [#78](https://github.com/MTES-MCT/dahlia/issues/78)
- Possibilité de télécharger plusieurs pièces jointes dans un fichier ZIP. [#64](https://github.com/MTES-MCT/dahlia/issues/64)
- Ajout d'un bouton pour télécharger la liste des dossiers. [#57](https://github.com/MTES-MCT/dahlia/issues/57)
- Ajout du formulaire pour éditer les métadonnées des pièces d'un dossier. [#51](https://github.com/MTES-MCT/dahlia/issues/51)
- Amélioration de la recherche et du tri des dossiers et des pièces. [#19](https://github.com/MTES-MCT/dahlia/issues/19), [#22](https://github.com/MTES-MCT/dahlia/issues/22)
- Ajout d'un bandeau indiquant que l'environnement n'est pas en production. [#20](https://github.com/MTES-MCT/dahlia/issues/20)
- Ajout d'un badge "très urgent". [#21](https://github.com/MTES-MCT/dahlia/issues/21)
- Ajout de la colonne "dernier producteur". [#44](https://github.com/MTES-MCT/dahlia/issues/44)
- Ajout de la date de délétion. [#40](https://github.com/MTES-MCT/dahlia/issues/40)

### Évolutions techniques
- Mise à jour des dépendances (NextJS, TypeScript, Vite, PostCSS, etc.) pour bénéficier des dernières corrections et améliorations.
- Configuration de Dependabot améliorée pour une gestion plus efficace des mises à jour de dépendances. [#30](https://github.com/MTES-MCT/dahlia/issues/30)
- Pin de la version de pnpm/action-setup en CI pour plus de stabilité. [#68](https://github.com/MTES-MCT/dahlia/issues/68)
- Mise à jour de l'action checkout de GitHub. [#58](https://github.com/MTES-MCT/dahlia/issues/58)
- Ajout d'un hook de precommit. [#75](https://github.com/MTES-MCT/dahlia/issues/75)
- Ajout de permissions dans la CI. [#48](https://github.com/MTES-MCT/dahlia/issues/48)
- Surdéfinition de Vite dans la configuration npm. [#46](https://github.com/MTES-MCT/dahlia/issues/46)
- Amélioration du scrapping et de la gestion des dates de mise à jour. [#66](https://github.com/MTES-MCT/dahlia/issues/66)
- Réorganisation des tests unitaires et d'intégration. [#56](https://github.com/MTES-MCT/dahlia/issues/56)

### Autres changements
- Ajout de fichiers anonymisés pour les tests. [#76](https://github.com/MTES-MCT/dahlia/issues/76)
- Affichage des pièces anonymisées dans les environnements autres que la production. [#55](https://github.com/MTES-MCT/dahlia/issues/55)
- Ajustement des interfaces. [#74](https://github.com/MTES-MCT/dahlia/issues/74)
- Mise à jour de la documentation INVESTIGATION. [#37](https://github.com/MTES-MCT/dahlia/issues/37)
- Amélioration de la gestion des tableaux. [#53](https://github.com/MTES-MCT/dahlia/issues/53)
- Amélioration de la configuration du header et des filtres. [#23](https://github.com/MTES-MCT/dahlia/issues/23)
- Ajout d'un script pour créer des dossiers inscrits au rôle d'une audience. [#77](https://github.com/MTES-MCT/dahlia/issues/77)
