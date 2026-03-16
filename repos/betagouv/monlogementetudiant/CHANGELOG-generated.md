## Changelog : monlogementetudiant (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration significative de l'administration du site, avec l'ajout d'un back-office pour la gestion des logements et des utilisateurs. De nouvelles fonctionnalités ont été implémentées pour faciliter la recherche et la gestion des logements, notamment l'intégration de données de sources externes comme Fac-Habitat et Dossier Facile. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été apportées pour une meilleure expérience globale.

### Évolutions fonctionnelles
- Ajout d'un back-office pour l'administration du site, permettant la gestion des logements et des utilisateurs. [#4c05be0](https://github.com/betagouv/monlogementetudiant/commit/4c05be0)
- Intégration de données de Fac-Habitat via une CLI dédiée. [#e8d118d](https://github.com/betagouv/monlogementetudiant/commit/e8d118d)
- Intégration de Dossier Facile. [#d57dd83](https://github.com/betagouv/monlogementetudiant/commit/d57dd83)
- Possibilité de filtrer les logements par bailleur dans le widget de recherche. [#ce13547](https://github.com/betagouv/monlogementetudiant/commit/ce13547)
- Ajout d'un badge "Liste d'attente" pour les logements concernés. [#a4080d9](https://github.com/betagouv/monlogementetudiant/commit/a4080d9)
- Ajout d'un tooltip pour les disponibilités inconnues. [#e4edc08](https://github.com/betagouv/monlogementetudiant/commit/e4edc08)
- Pagination ajoutée au tableau de bord. [#235fdbd](https://github.com/betagouv/monlogementetudiant/commit/235fdbd)
- Amélioration de l'UX/UI du widget de recherche. [#2a100f9](https://github.com/betagouv/monlogementetudiant/commit/2a100f9)
- Ajout d'un simulateur d'aide. [#734c20f](https://github.com/betagouv/monlogementetudiant/commit/734c20f)
- Implémentation du tracking. [#154d9e6](https://github.com/betagouv/monlogementetudiant/commit/154d9e6)
- Ajout de liens vers les CGU et mentions légales. [#c211838](https://github.com/betagouv/monlogementetudiant/commit/c211838)

### Évolutions techniques
- Refonte de la gestion de l'authentification avec Drizzle ORM adapter. [#a23e598](https://github.com/betagouv/monlogementetudiant/commit/a23e598)
- Refonte de la CLI et des migrations. [#386adae](https://github.com/betagouv/monlogementetudiant/commit/386adae)
- Implémentation de tests d'intégration et unitaires. [#996b137](https://github.com/betagouv/monlogementetudiant/commit/996b137)
- Utilisation de PostGIS pour l'optimisation des requêtes géographiques. [#3fdcd48](https://github.com/betagouv/monlogementetudiant/commit/3fdcd48)
- Intégration de tRPC pour la communication client-serveur. [#7c0b29c](https://github.com/betagouv/monlogementetudiant/commit/7c0b29c)
- Mise en place d'un système de cache et de préchargement pour améliorer les performances. [#6bb4c0a](https://github.com/betagouv/monlogementetudiant/commit/6bb4c0a)
- Amélioration de la gestion des erreurs et des états de chargement avec Suspense et skeletons. [#1d6d869](https://github.com/betagouv/monlogementetudiant/commit/1d6d869)

### Autres changements
- Correction de plusieurs bugs liés à l'importation de données, à la gestion des permissions et à l'affichage de l'interface utilisateur.
- Amélioration de la sécurité en sanitizant les données HTML. [#ffef945](https://github.com/betagouv/monlogementetudiant/commit/ffef945)
- Mise à jour de l'adresse email du DPO. [#03697c2](https://github.com/betagouv/monlogementetudiant/commit/03697c2)
- Suppression de logs inutiles. [#1e4df21](https://github.com/betagouv/monlogementetudiant/commit/1e4df21)
- Refactoring du routeur. [#380d81c](https://github.com/betagouv/monlogementetudiant/commit/380d81c)
- Mise à jour de la documentation et du README. [#2372850](https://github.com/betagouv/monlogementetudiant/commit/2372850)
- Corrections de typographie et de wording.
