## Changelog : fondation (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration des fonctionnalités de recherche et de gestion des dossiers, notamment les nominations et les rapports. Des corrections ont été apportées pour améliorer la stabilité et l'expérience utilisateur, et des optimisations techniques ont été réalisées pour préparer le projet à long terme.

### Évolutions fonctionnelles
- Ajout de la recherche en texte intégral dans les dossiers de nomination. [#336](https://github.com/betagouv/fondation/issues/336)
- Possibilité de supprimer une session de nomination. [#315](https://github.com/betagouv/fondation/issues/315)
- Ajout d'un tooltip pour le résultat d'une nomination. [#314](https://github.com/betagouv/fondation/issues/314)
- Ajout de la possibilité de filtrer les nominations par résultat. [#308](https://github.com/betagouv/fondation/issues/308) et [#307](https://github.com/betagouv/fondation/issues/307)
- Ajout de la gestion des plans de présentation de justice. [#311](https://github.com/betagouv/fondation/issues/311)
- Amélioration de la récupération des présidents de formation. [#324](https://github.com/betagouv/fondation/issues/324)
- Ajout de la possibilité de lier une pièce jointe à une observation. [#317](https://github.com/betagouv/fondation/issues/317)
- Ajout des libellés des positions spéciales pour VPCP et JCP. [#305](https://github.com/betagouv/fondation/issues/305)
- Ajout de la gestion des rapports officiels. [#304](https://github.com/betagouv/fondation/issues/304)
- Correction de la récupération des arrondissements. [#310](https://github.com/betagouv/fondation/issues/310)

### Évolutions techniques
- Refactorisation du modèle de date pour une meilleure gestion. [#332](https://github.com/betagouv/fondation/issues/332)
- Suppression de `shared-models` du frontend pour simplifier l'architecture. [#331](https://github.com/betagouv/fondation/issues/331)
- Suppression des migrations Drizzle. [#322](https://github.com/betagouv/fondation/issues/322)
- Suppression de `fast-xml-parser`. [#323](https://github.com/betagouv/fondation/issues/323)
- Introduction d'un utilitaire `multipart json` pour faciliter la gestion des requêtes. [#318](https://github.com/betagouv/fondation/issues/318)
- Amélioration de la recherche des observations des magistrats. [#316](https://github.com/betagouv/fondation/issues/316)
- Mise à jour de Tailwind CSS. [#330](https://github.com/betagouv/fondation/issues/330) et de DSFR [#321](https://github.com/betagouv/fondation/issues/321)
- Intégration des outils d'analyse de code Oxlint et Oxfmt. [#329](https://github.com/betagouv/fondation/issues/329)

### Autres changements
- Ajout d'une animation de recherche de fichiers. [#337](https://github.com/betagouv/fondation/issues/337)
- Correction d'un problème empêchant la suppression de sessions LOLFI. [#328](https://github.com/betagouv/fondation/issues/328)
- Correction d'un bug empêchant la sélection de l'agenda du rapport officiel.
- Correction de l'affichage de la combobox vide.
- Correction de la largeur du sélecteur de fichier de nomination de l'agenda.
- Ajout de tests d'acceptation. [#325](https://github.com/betagouv/fondation/issues/325)
- Amélioration de la configuration de l'interface utilisateur Swagger. [#312](https://github.com/betagouv/fondation/issues/312)
- Audit de sécurité Zizmor. [#339](https://github.com/betagouv/fondation/issues/339)
- Correction d'un problème lié à l'ingestion des sessions LOLFI. [#326](https://github.com/betagouv/fondation/issues/326)
- Initialisation de Renovate pour la gestion des dépendances. [#334](https://github.com/betagouv/fondation/issues/334) et déplacement du fichier de configuration Renovate à la racine du projet [#335](https://github.com/betagouv/fondation/issues/335)
- Correction de problèmes de largeur des actions dans le tableau des nominations.
- Suppression de l'extraction i18n.
- Correction du tri de la liste des rapports des membres. [#306](https://github.com/betagouv/fondation/issues/306)
- Correction d'un bug nécessitant 2 rapporteurs pour une fonction. [#313](https://github.com/betagouv/fondation/issues/313)
