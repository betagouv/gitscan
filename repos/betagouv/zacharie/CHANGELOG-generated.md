## Changelog : zacharie (30 derniers jours, au 8 juillet 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la traçabilité des données, en particulier pour les transmissions entre les différents acteurs (chasseurs, collecteurs, ETG). Des améliorations significatives ont été apportées à l'interface utilisateur, notamment pour les utilisateurs SVI et les administrateurs, ainsi que des corrections de bugs pour assurer une meilleure stabilité et une expérience utilisateur plus fluide. L'application a également bénéficié d'optimisations de performance, notamment pour la gestion des carcasses et des données.

### Évolutions fonctionnelles
- Ajout d'une interface pour les laboratoires [#435](https://github.com/betagouv/zacharie/issues/435).
- Les chasseurs avec un CFEI peuvent désormais créer une fiche sans la transmettre immédiatement [#469](https://github.com/betagouv/zacharie/issues/469).
- Amélioration de l'affichage des statistiques pour les utilisateurs SVI sur la page utilisateur ETG [#502](https://github.com/betagouv/zacharie/issues/502).
- Notification de l'expéditeur lorsqu'un destinataire renvoie une fiche [#508](https://github.com/betagouv/zacharie/issues/508).
- Refonte de l'export des fiches, permettant une sélection modulaire des données à exporter [#445](https://github.com/betagouv/zacharie/issues/445).
- Amélioration de l'affichage du dernier intermédiaire avant l'ETG sur la FEI [#433](https://github.com/betagouv/zacharie/issues/433).
- Ajout d'une sidebar pour les collecteurs [#526](https://github.com/betagouv/zacharie/issues/526).
- Affichage du statut "Transmise" en vert pour les carcasses transmises en circuit court [#505](https://github.com/betagouv/zacharie/issues/505).
- Amélioration de l'interface utilisateur pour la création de fiches et les demandes de modifications [#444](https://github.com/betagouv/zacharie/issues/444).

### Évolutions techniques
- Optimisation du backend pour la synchronisation d'un grand nombre de carcasses [#512](https://github.com/betagouv/zacharie/issues/512).
- Compression des données pour accélérer la transmission [#485](https://github.com/betagouv/zacharie/issues/485).
- Suppression des champs dépréciés de la FEI [#521](https://github.com/betagouv/zacharie/issues/521).
- Amélioration de la gestion des transmissions entre les différents acteurs, avec une séparation des étapes et des tests associés [#463](https://github.com/betagouv/zacharie/issues/463).
- Correction de problèmes liés à la pagination des chasseurs [#486](https://github.com/betagouv/zacharie/issues/486).
- Optimisation de la récupération des entités par carcasses au lieu des fiches [#465](https://github.com/betagouv/zacharie/issues/465).
- Suppression de la vérification de la connectivité réseau (utilisation du store à la place) [#449](https://github.com/betagouv/zacharie/issues/449).
- Amélioration de la gestion des carcasses orphelines (sans FEI) [#479](https://github.com/betagouv/zacharie/issues/479).

### Autres changements
- Correction de plusieurs problèmes d'UI/UX, notamment sur la landing page et le panel d'administration.
- Mise à jour du wording sur plusieurs parties de l'application [#515](https://github.com/betagouv/zacharie/issues/515), [#524](https://github.com/betagouv/zacharie/issues/524), [#3b34fe3](https://github.com/betagouv/zacharie/commit/3b34fe3).
- Ajout de tracking Matomo pour les événements [#503](https://github.com/betagouv/zacharie/issues/503) et [#513](https://github.com/betagouv/zacharie/issues/513).
- Masquage des outils de débogage en environnement de staging.
- Correction de tests et ajout de nouveaux tests.
- Suppression de fichiers FEI inutiles [#491](https://github.com/betagouv/zacharie/issues/491).
- Correction de bugs divers liés à l'affichage et au fonctionnement de l'application.
