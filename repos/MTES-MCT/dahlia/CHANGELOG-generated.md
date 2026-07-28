## Changelog : dahlia (30 derniers jours, au 27 juillet 2026)

### Résumé
Les dernières mises à jour de Dahlia se concentrent sur l'amélioration de la gestion des dossiers et des pièces jointes, ainsi que sur l'ajout de nouvelles fonctionnalités pour faciliter le travail des agents de l'administration. Des améliorations de l'interface utilisateur et des corrections de bugs ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'un bouton pour télécharger la liste des dossiers [#57](https://github.com/MTES-MCT/dahlia/issues/57).
- Possibilité de télécharger plusieurs pièces jointes dans un fichier ZIP [#64](https://github.com/MTES-MCT/dahlia/issues/64).
- Récupération de tous les acteurs liés à un dossier [#79](https://github.com/MTES-MCT/dahlia/issues/79).
- Affichage du dernier jugement si celui-ci existe [#78](https://github.com/MTES-MCT/dahlia/issues/78).
- Ajout d'un script pour créer des dossiers inscrits au rôle d'une audience [#77](https://github.com/MTES-MCT/dahlia/issues/77).
- Ajout d'un formulaire pour éditer les métadonnées des pièces d'un dossier [#51](https://github.com/MTES-MCT/dahlia/issues/51).
- Ajout d'un warning si la date limite de production est dans le passé [#80](https://github.com/MTES-MCT/dahlia/issues/80).
- Affichage de fichiers anonymisés dans les environnements autres que la production [#55](https://github.com/MTES-MCT/dahlia/issues/55).
- Ajustements d'affichage de l'interface utilisateur [#90](https://github.com/MTES-MCT/dahlia/issues/90).

### Évolutions techniques
- Utilisation d'une instance XL pour l'exécution des tâches planifiées (crons) [#93](https://github.com/MTES-MCT/dahlia/issues/93).
- Ajout d'un hook de precommit pour garantir la qualité du code [#75](https://github.com/MTES-MCT/dahlia/issues/75).
- Mise à jour des dépendances : TypeScript, Vite, PostCSS, better-auth, @types/node, @tailwindcss/postcss, vitest-mock-extended [#60, #61, #62, #63, #67, #70, #71, #73, #84, #86, #87].
- Mise à jour de l'action checkout de GitHub [#58](https://github.com/MTES-MCT/dahlia/issues/58).
- Pin de la version de l'action pnpm/action-setup en CI [#68](https://github.com/MTES-MCT/dahlia/issues/68).
- Réorganisation des tests unitaires et d'intégration [#56](https://github.com/MTES-MCT/dahlia/issues/56).
- Remplacement de "vs" par "c/" dans le code [#82](https://github.com/MTES-MCT/dahlia/issues/82).
- Renommage d'un dossier [#81](https://github.com/MTES-MCT/dahlia/issues/81).
- Ajustement des interfaces [#74](https://github.com/MTES-MCT/dahlia/issues/74).

### Autres changements
- Mise à jour du scrapping et de la gestion des dates de mise à jour [#66](https://github.com/MTES-MCT/dahlia/issues/66).
- Amélioration de la gestion des tableaux [#53](https://github.com/MTES-MCT/dahlia/issues/53).
