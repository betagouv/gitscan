## Changelog : zacharie (30 derniers jours, au 21 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur autour de la gestion des carcasses et des fiches, avec un accent particulier sur la navigation et l'affichage des données. Des corrections importantes ont été apportées pour assurer la stabilité et la fiabilité de l'application, notamment en lien avec les tests et la gestion des erreurs. Des améliorations techniques ont également été réalisées pour optimiser le code et préparer de futures fonctionnalités.

### Évolutions fonctionnelles
- Possibilité de modifier le numéro de bracelet ou d'ajouter une carcasse à un examen initial [#383](https://github.com/betagouv/zacharie/issues/383).
- Ajout d'une page 404 pour une meilleure gestion des erreurs de navigation [#394](https://github.com/betagouv/zacharie/issues/394).
- Amélioration de l'interface utilisateur pour les carcasses [#373](https://github.com/betagouv/zacharie/issues/373).
- Ajout de la possibilité de voir les destinataires des fiches de son association pour les chasseurs [#378](https://github.com/betagouv/zacharie/issues/378).
- Suppression du bouton de création de fiche pour les simples chasseurs [#375](https://github.com/betagouv/zacharie/issues/375).
- Ajout d'une page dédiée aux carcasses [#353](https://github.com/betagouv/zacharie/issues/353).
- Ajout de la liste des lésions [#331](https://github.com/betagouv/zacharie/issues/331).
- Amélioration des headers pour les SVI, FEI et ETG [#319](https://github.com/betagouv/zacharie/issues/319), [#322](https://github.com/betagouv/zacharie/issues/322), [#323](https://github.com/betagouv/zacharie/issues/323).
- Amélioration de l'affichage de la carte des carcasses [#312](https://github.com/betagouv/zacharie/issues/312).
- Ajout d'un quiz pour le prélèvement et l'assiette [#361](https://github.com/betagouv/zacharie/issues/361).

### Évolutions techniques
- Refactorisation des contrôleurs pour une meilleure organisation du code [#382](https://github.com/betagouv/zacharie/issues/382), [#364](https://github.com/betagouv/zacharie/issues/364), [#371](https://github.com/betagouv/zacharie/issues/371).
- Préparation du renversement du GET fei vers GET carcasses avec des tests de non régression [#384](https://github.com/betagouv/zacharie/issues/384).
- Ajout de Prettier dans le workflow CI/CD pour garantir la cohérence du code [#393](https://github.com/betagouv/zacharie/issues/393).
- Optimisation des appels et gestion des filtres [#390](https://github.com/betagouv/zacharie/issues/390).
- Suppression de code mort lié à l'ancien tableau de bord [#391](https://github.com/betagouv/zacharie/issues/391).
- Simplification de la pagination des carcasses pour améliorer les performances [#329](https://github.com/betagouv/zacharie/issues/329).
- Ajout de tests E2E pour améliorer la couverture et la fiabilité [#315](https://github.com/betagouv/zacharie/issues/315), [#340](https://github.com/betagouv/zacharie/issues/340).
- Mise en place d'un système de bearer token pour les appels API [#336](https://github.com/betagouv/zacharie/issues/336).

### Autres changements
- Correction du label du bouton "date du jour" [#396](https://github.com/betagouv/zacharie/issues/396).
- Amélioration de la transmission de la timeline [#397](https://github.com/betagouv/zacharie/issues/397).
- Chargement de Zacharie par les carcasses au lieu des fiches, avec protection des routes [#392](https://github.com/betagouv/zacharie/issues/392).
- Correction du reset du store à la déconnexion [#385](https://github.com/betagouv/zacharie/issues/385).
- Correction de l'UI pour la création d'associations de chasse [#380](https://github.com/betagouv/zacharie/issues/380).
- Ajout de scripts de démo pour simuler l'activité ETG [#388](https://github.com/betagouv/zacharie/issues/388).
- Correction du timeout pour le clear cache [#379](https://github.com/betagouv/zacharie/issues/379).
- Correction d'un bug empêchant l'invitation des chasseurs [#377](https://github.com/betagouv/zacharie/issues/377).
- Correction du toggle admin [#376](https://github.com/betagouv/zacharie/issues/376).
- Nettoyage des vieux liens du backend [#372](https://github.com/betagouv/zacharie/issues/372).
- Correction de l'affichage des commentaires des intermédiaires [#358](https://github.com/betagouv/zacharie/issues/358).
- Correction des filtres collecteurs [#357](https://github.com/betagouv/zacharie/issues/357).
- Correction de l'initialisation du path [#338](https://github.com/betagouv/zacharie/issues/338).
- Correction d'un problème de chargement Expo [#337](https://github.com/betagouv/zacharie/issues/337).
- Correction de messages d'erreur [#341](https://github.com/betagouv/zacharie/issues/341).
- Correction du calcul BPH [#326](https://github.com/betagouv/zacharie/issues/326).
- Correction du wording des motifs [#342](https://github.com/betagouv/zacharie/issues/342).
- Correction du header fiche chasseur [#325](https://github.com/betagouv/zacharie/issues/325).
- Correction de la pagination des carcasses [#329](https://github.com/betagouv/zacharie/issues/329).
- Mise à jour des dépendances (fast-uri, ip-address, express-rate-limit, postcss) - ces mises à jour automatiques sont gérées par Dependabot et ne sont pas détaillées ici.
