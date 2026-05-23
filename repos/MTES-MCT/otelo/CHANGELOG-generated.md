## Changelog : otelo (30 derniers jours, au 21 mai 2026)

### Résumé
Ce mois-ci, l'application otelo a bénéficié d'une série d'améliorations significatives, notamment au niveau du tableau de bord avec une refonte complète et l'ajout de nouvelles fonctionnalités de comparaison de scénarios. Des améliorations ont également été apportées à l'importation de données via la CLI, à la gestion des utilisateurs et à la correction de bugs pour une meilleure expérience utilisateur.

### Évolutions fonctionnelles
- **Tableau de bord :** Refonte complète du tableau de bord avec de nouvelles fonctionnalités de comparaison de scénarios et d'affichage de données historiques. [#42](https://github.com/MTES-MCT/otelo/pull/42)
- **Comparaison de données :** Ajout de la comparaison en pourcentage entre les valeurs de logement vacant et de logements réservés.
- **Importation de données :** Nouvelle fonctionnalité permettant d'importer des données via la CLI. [#40](https://github.com/MTES-MCT/otelo/pull/40)
- **Gestion des utilisateurs :** Possibilité pour un administrateur d'usurper l'identité d'un autre utilisateur.
- **Pilotage :** Ajout d'une fonctionnalité de pilotage cartographique.
- **Nouvelle méthodologie :** Implémentation d'une nouvelle méthodologie sans hébergement. [#42](https://github.com/MTES-MCT/otelo/pull/42)
- **Données historiques :** Ajout de séries démographiques historiques.
- **Typologie utilisateur :** Ajout d'une typologie d'utilisateur.
- **Partage en lecture seule :** Implémentation d'un partage en lecture seule.
- **Gestion des clés API :** Ajout de la gestion des consommateurs de clés API.
- **Guide :** Ajout d'un guide pour le parc de données.

### Évolutions techniques
- **Mises à jour :** Mise à jour de Next.js et de pnpm.
- **CLI :** Amélioration de l'injection de modules dans la CLI.
- **Versioning des données :** Implémentation du versioning des données.
- **Swagger :** Amélioration des enums dans Swagger.
- **Cache :** Mise en cache des résultats pour améliorer les performances.
- **Build :** Corrections diverses du build web.

### Autres changements
- Correction de divers bugs et améliorations de l'UX.
- Amélioration des wordings et de la documentation.
- Corrections de tests et de linting.
- Suppression de l'envoi d'emails en environnement local.
- Correction de la gestion des années de millésime.
- Ajout d'une page changelog.
- Correction de la gestion des taux de vacance.
- Correction de la gestion des pics de logements réservés.
- Correction de la gestion des groupes EPCI.
- Correction de la gestion des taux LV dans Excel.
- Amélioration de la gestion des projections.
- Correction de la gestion des taux de vacance.
- Ajout de tests unitaires et corrections de tests existants.
