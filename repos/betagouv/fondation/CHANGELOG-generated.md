## Changelog : fondation (30 derniers jours, au 07 mai 2026)

### Résumé
Ce mois-ci, l'équipe a continué d'améliorer l'application Fondation avec de nouvelles fonctionnalités axées sur la gestion des nominations, des rapports officiels et des observations. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été apportées pour une meilleure expérience utilisateur. Plusieurs optimisations techniques ont été réalisées en arrière-plan pour améliorer la performance et la maintenabilité du code.

### Évolutions fonctionnelles
- Ajout de la possibilité de supprimer une session de nomination. [#315](https://github.com/betagouv/fondation/issues/315)
- Ajout d'un tooltip informatif pour les résultats de nomination. [#314](https://github.com/betagouv/fondation/issues/314)
- Implémentation du filtrage des nominations par résultat. [#308](https://github.com/betagouv/fondation/issues/308) et [#307](https://github.com/betagouv/fondation/issues/307)
- Ajout de la gestion des plans de présentation de justice. [#311](https://github.com/betagouv/fondation/issues/311)
- Amélioration de la récupération des arrondissements. [#310](https://github.com/betagouv/fondation/issues/310)
- Ajout de la fonctionnalité de liaison de pièces jointes aux observations. [#317](https://github.com/betagouv/fondation/issues/317)
- Ajout de la fonctionnalité de statut des documents de nomination. [#320](https://github.com/betagouv/fondation/issues/320)
- Ajout de la possibilité de récupérer les présidents de formation. [#324](https://github.com/betagouv/fondation/issues/324)
- Ajout de la gestion des rapports officiels. [#304](https://github.com/betagouv/fondation/issues/304)
- Amélioration de la recherche des observations des magistrats. [#316](https://github.com/betagouv/fondation/issues/316)

### Évolutions techniques
- Suppression de `shared-models` du frontend pour simplifier l'architecture. [#331](https://github.com/betagouv/fondation/issues/331)
- Suppression des migrations Drizzle. [#322](https://github.com/betagouv/fondation/issues/322)
- Suppression de la librairie `fast-xml-parser`. [#323](https://github.com/betagouv/fondation/issues/323)
- Introduction d'un utilitaire `multipart json` pour améliorer la gestion des requêtes. [#318](https://github.com/betagouv/fondation/issues/318)
- Refonte de la configuration de l'interface utilisateur Swagger. [#312](https://github.com/betagouv/fondation/issues/312)
- Ajout de tests d'acceptation supplémentaires. [#325](https://github.com/betagouv/fondation/issues/325)
- Mise à jour de la librairie DSFR. [#321](https://github.com/betagouv/fondation/issues/321)
- Mise à jour de TailwindCSS. [#330](https://github.com/betagouv/fondation/issues/330)
- Implémentation d'OxLint et OxFmt pour améliorer la qualité du code. [#329](https://github.com/betagouv/fondation/issues/329)

### Autres changements
- Correction d'un bug empêchant la création de session LOLFI lorsque celle-ci est vide. [#328](https://github.com/betagouv/fondation/issues/328)
- Correction de l'affichage de la sélection de l'agenda du rapport officiel.
- Correction de l'affichage de la largeur des éléments de la combobox vide.
- Correction de la largeur de l'élément de sélection du fichier de nomination de l'agenda.
- Correction de l'ingestion de la formation de la session LOLFI. [#326](https://github.com/betagouv/fondation/issues/326)
- Correction d'un bug lié à la fonction nécessitant 2 rapporteurs. [#313](https://github.com/betagouv/fondation/issues/313)
- Ajout de la gestion de l'internationalisation (i18n). [#303](https://github.com/betagouv/fondation/issues/303)
- Amélioration de la mise en page de l'agenda. [#301](https://github.com/betagouv/fondation/issues/301)
- Correction des labels des positions spéciales pour VPCP et JCP. [#305](https://github.com/betagouv/fondation/issues/305)
- Amélioration du tri de la liste des rapports des membres. [#306](https://github.com/betagouv/fondation/issues/306)
- Corrections mineures de l'interface utilisateur.
