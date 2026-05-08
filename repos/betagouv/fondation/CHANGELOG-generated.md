## Changelog : fondation (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, les évolutions de la fondation se concentrent sur l'amélioration de la gestion des nominations, des rapports et des agendas, avec des corrections de bugs et des optimisations de l'interface utilisateur. De nouvelles fonctionnalités ont été ajoutées pour faciliter la gestion des pièces jointes, la recherche et le filtrage des données, ainsi que la suppression de sessions de nomination.

### Évolutions fonctionnelles
- Ajout de la possibilité de supprimer une session de nomination. [#315](https://github.com/betagouv/fondation/issues/315)
- Implémentation d'un tooltip pour le résultat d'une nomination. [#314](https://github.com/betagouv/fondation/issues/314)
- Ajout de la possibilité de filtrer les nominations par résultat. [#308](https://github.com/betagouv/fondation/issues/308) et [#307](https://github.com/betagouv/fondation/issues/307)
- Ajout de la gestion des plans de présentation de justice. [#311](https://github.com/betagouv/fondation/issues/311)
- Amélioration de la récupération des arrondissements. [#310](https://github.com/betagouv/fondation/issues/310)
- Ajout de la possibilité de lier une pièce jointe à une observation. [#317](https://github.com/betagouv/fondation/issues/317)
- Ajout de la gestion des statuts des documents des nominations. [#320](https://github.com/betagouv/fondation/issues/320)
- Ajout de la possibilité de récupérer les présidents de formation. [#324](https://github.com/betagouv/fondation/issues/324)
- Mise à jour de l'agenda avec des informations plus précises. [#300](https://github.com/betagouv/fondation/issues/300)
- Amélioration de la recherche des observations des magistrats. [#316](https://github.com/betagouv/fondation/issues/316)
- Ajout de l'ID de fonction dans le sélecteur de fichiers. [#302](https://github.com/betagouv/fondation/issues/302)
- Amélioration de la mise en page de l'agenda. [#301](https://github.com/betagouv/fondation/issues/301)

### Évolutions techniques
- Refactorisation pour introduire un utilitaire multipart/json. [#318](https://github.com/betagouv/fondation/issues/318)
- Suppression des migrations Drizzle. [#322](https://github.com/betagouv/fondation/issues/322)
- Suppression de `fast-xml-parser`. [#323](https://github.com/betagouv/fondation/issues/323)
- Suppression de `shared-models` du front-end. [#331](https://github.com/betagouv/fondation/issues/331)
- Ajout de tests d'acceptation supplémentaires. [#325](https://github.com/betagouv/fondation/issues/325)
- Amélioration de la configuration de l'interface utilisateur Swagger. [#312](https://github.com/betagouv/fondation/issues/312)
- Réduction de l'utilisation du réseau lors de l'édition d'un rapport. [#298](https://github.com/betagouv/fondation/issues/298)
- Ajout de l'internationalisation (i18n). [#303](https://github.com/betagouv/fondation/issues/303)

### Autres changements
- Correction d'un bug empêchant l'ingestion de sessions LOLFI vides. [#328](https://github.com/betagouv/fondation/issues/328)
- Correction de l'emplacement de la sélection de l'agenda du rapport officiel.
- Correction du style de la combobox vide.
- Correction de la largeur de l'élément de résultat du sélecteur de fichiers de nomination.
- Correction de l'ingestion de la formation de la session lolfi. [#326](https://github.com/betagouv/fondation/issues/326)
- Correction d'un bug lié à la fonction nécessitant 2 rapporteurs. [#313](https://github.com/betagouv/fondation/issues/313)
- Corrections diverses de l'interface utilisateur (largeurs, styles).
- Mise à jour de Tailwind CSS. [#330](https://github.com/betagouv/fondation/issues/330)
- Mise à jour de DSFR. [#321](https://github.com/betagouv/fondation/issues/321)
- Ajout d'OXlint et OXfmt pour l'amélioration de la qualité du code. [#329](https://github.com/betagouv/fondation/issues/329)
- Correction des labels des positions spéciales pour VPCP et JCP. [#305](https://github.com/betagouv/fondation/issues/305)
