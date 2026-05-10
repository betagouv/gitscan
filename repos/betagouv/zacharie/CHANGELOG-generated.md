## Changelog : zacharie (30 derniers jours, au 8 mai 2026)

### Résumé
Ce mois-ci, l'application Zacharie a bénéficié d'une série d'améliorations axées sur l'interface utilisateur, la gestion des fiches et des carcasses, ainsi que des corrections de bugs pour une meilleure stabilité. Des fonctionnalités ont été ajoutées pour faciliter le travail des utilisateurs, notamment dans la gestion des SVI et des FDC. Des optimisations ont également été apportées pour améliorer l'expérience utilisateur sur le terrain, notamment en mode hors ligne.

### Évolutions fonctionnelles
- Ajout de la liste des lésions sur les fiches. [#331](https://github.com/betagouv/zacharie/issues/331)
- Amélioration de l'affichage des commentaires des intermédiaires dans les modales. [#358](https://github.com/betagouv/zacharie/issues/358)
- Ajout d'un tableau de bord FND/FDC. [#330](https://github.com/betagouv/zacharie/issues/330)
- Ajout des headers SVI/FEI. [#323](https://github.com/betagouv/zacharie/issues/323) et [#319](https://github.com/betagouv/zacharie/issues/319)
- Amélioration de l'affichage des fiches chasseur dans la sidebar. [#345](https://github.com/betagouv/zacharie/issues/345)
- Ajout d'un bouton pour se déconnecter. [#341](https://github.com/betagouv/zacharie/issues/341)
- Amélioration du calcul du BPH. [#326](https://github.com/betagouv/zacharie/issues/326)
- Amélioration de l'interface utilisateur pour la création de fiches. [#311](https://github.com/betagouv/zacharie/issues/311)
- Amélioration de l'interface utilisateur pour la liste des fiches. [#302](https://github.com/betagouv/zacharie/issues/302)
- Ajout du routing SVI. [#296](https://github.com/betagouv/zacharie/issues/296)
- Amélioration de l'interface utilisateur des fiches envoyées. [#306](https://github.com/betagouv/zacharie/issues/306)
- Amélioration de l'interface utilisateur des fiches examinateur. [#305](https://github.com/betagouv/zacharie/issues/305)

### Évolutions techniques
- Passage à `zacharie.incubateur.net`. [#350](https://github.com/betagouv/zacharie/issues/350)
- Correction de tests instables. [#352](https://github.com/betagouv/zacharie/issues/352)
- Mise en place d'un bearer token pour les appels API. [#336](https://github.com/betagouv/zacharie/issues/336)
- Ajout du support du mode hors ligne avec Expo. [#327](https://github.com/betagouv/zacharie/issues/327)
- Pagination des carcasses pour éviter la limite de 100 lignes. [#329](https://github.com/betagouv/zacharie/issues/329)
- Correction de problèmes liés aux cookies en environnement de staging et production.
- Ajout de tests E2E. [#340](https://github.com/betagouv/zacharie/issues/340) et [#315](https://github.com/betagouv/zacharie/issues/315)
- Refonte du routing collecteur et ajout du routing circuit court. [#308](https://github.com/betagouv/zacharie/issues/308) et [#310](https://github.com/betagouv/zacharie/issues/310)

### Autres changements
- Correction de l'affichage du picto dans l'header des fiches. [#348](https://github.com/betagouv/zacharie/issues/348)
- Correction de bugs mineurs liés aux filtres collecteurs. [#357](https://github.com/betagouv/zacharie/issues/357)
- Correction de l'affichage du nombre total de carcasses. [#344](https://github.com/betagouv/zacharie/issues/344)
- Correction de l'auto-clôture des circuits courts. [#343](https://github.com/betagouv/zacharie/issues/343)
- Correction de la gestion des motifs. [#342](https://github.com/betagouv/zacharie/issues/342)
- Correction de l'affichage de l'header des fiches chasseur. [#325](https://github.com/betagouv/zacharie/issues/325)
- Correction de l'URL initiale pour Expo. [#337](https://github.com/betagouv/zacharie/issues/337) et [#338](https://github.com/betagouv/zacharie/issues/338)
- Correction de l'état "désactivé" du SVI. [#335](https://github.com/betagouv/zacharie/issues/335)
- Correction de l'affichage de la carte des carcasses. [#312](https://github.com/betagouv/zacharie/issues/312)
- Suppression d'images volumineuses.
- Mise à jour de la documentation E2E. [#351](https://github.com/betagouv/zacharie/issues/351) et [#4957faf]
- Nettoyage des logs.
- Amélioration de la gestion des erreurs.
- Ajout de prettier pour uniformiser le code. [#320](https://github.com/betagouv/zacharie/issues/320)
