## Changelog : fondation (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la recherche et du filtrage des dossiers, notamment les nominations et les rapports. Des corrections ont été apportées pour améliorer la stabilité et l'expérience utilisateur, et des fonctionnalités ont été ajoutées pour la gestion des présentations et des plans de justice. L'équipe a également continué à améliorer l'infrastructure et la qualité du code.

### Évolutions fonctionnelles
- Ajout de la recherche en texte intégral dans les dossiers de nomination [#336](https://github.com/betagouv/fondation/issues/336).
- Possibilité de filtrer les dossiers par résultat (issue d'approbation/rejet) [#307](https://github.com/betagouv/fondation/issues/307) et [#308](https://github.com/betagouv/fondation/issues/308).
- Ajout de la fonctionnalité de suppression de session de nomination [#315](https://github.com/betagouv/fondation/issues/315).
- Ajout d'un tooltip pour le résultat d'une nomination [#314](https://github.com/betagouv/fondation/issues/314).
- Implémentation des plans de présentation de justice [#311](https://github.com/betagouv/fondation/issues/311).
- Ajout de la possibilité de lier une pièce jointe à une observation [#317](https://github.com/betagouv/fondation/issues/317).
- Récupération des présidents de formation [#324](https://github.com/betagouv/fondation/issues/324).
- Ajout de l'affichage des rapports officiels [#304](https://github.com/betagouv/fondation/issues/304).
- Amélioration de l'affichage des libellés des positions spéciales (VPCP, JCP) [#305](https://github.com/betagouv/fondation/issues/305).

### Évolutions techniques
- Refactorisation du modèle de date pour simplifier la gestion [#332](https://github.com/betagouv/fondation/issues/332).
- Suppression des modèles partagés du frontend pour alléger le code [#331](https://github.com/betagouv/fondation/issues/331).
- Suppression des migrations Drizzle [#322](https://github.com/betagouv/fondation/issues/322).
- Suppression de la librairie `fast-xml-parser` [#323](https://github.com/betagouv/fondation/issues/323).
- Introduction d'un utilitaire `multipart json` pour améliorer la gestion des requêtes multipart [#318](https://github.com/betagouv/fondation/issues/318).
- Amélioration de la recherche des observations des magistrats [#316](https://github.com/betagouv/fondation/issues/316).
- Ajout de tests d'acceptation supplémentaires [#325](https://github.com/betagouv/fondation/issues/325).
- Configuration améliorée de l'interface utilisateur Swagger [#312](https://github.com/betagouv/fondation/issues/312).
- Ajout de l'internationalisation (i18n) [#303](https://github.com/betagouv/fondation/issues/303).

### Autres changements
- Correction d'un bug où les fichiers suspendus continuaient de s'exécuter [#338](https://github.com/betagouv/fondation/issues/338).
- Ajout d'une animation de recherche de fichiers [#337](https://github.com/betagouv/fondation/issues/337).
- Correction d'un problème empêchant la session LOLFI d'être vide [#328](https://github.com/betagouv/fondation/issues/328).
- Correction du positionnement de la sélection de l'agenda du rapport officiel [#326](https://github.com/betagouv/fondation/issues/326).
- Ajout de l'intégration d'Oxlint et Oxfmt pour la qualité du code [#329](https://github.com/betagouv/fondation/issues/329).
- Correction de problèmes de style divers (combobox, largeur des éléments) [#327](https://github.com/betagouv/fondation/issues/327), [#320](https://github.com/betagouv/fondation/issues/320).
- Correction d'un bug lié à la récupération des arrondissements [#310](https://github.com/betagouv/fondation/issues/310).
- Correction d'un bug nécessitant deux rapporteurs pour une fonction [#313](https://github.com/betagouv/fondation/issues/313).
- Initialisation de Renovate pour la gestion des dépendances [#334](https://github.com/betagouv/fondation/issues/334).
- Déplacement du fichier Renovate à la racine du dépôt [#335](https://github.com/betagouv/fondation/issues/335).
- Mise à jour de TailwindCSS et DSFR.
