## Changelog : zacharie (30 derniers jours, au 15 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'interface utilisateur, notamment pour la gestion des fiches, des carcasses et des tableaux de bord. Des corrections de bugs ont été apportées pour améliorer la stabilité et l'expérience utilisateur, en particulier concernant les accès, les filtres et les circuits courts. Des optimisations techniques ont également été réalisées, notamment sur les tests et le code backend.

### Évolutions fonctionnelles
- Ajout d'une page carcasse [#353](https://github.com/betagouv/zacharie/issues/353).
- Implémentation d'un quiz pour le prélèvement et l'assiette [#361](https://github.com/betagouv/zacharie/issues/361).
- Affichage des commentaires des intermédiaires dans la modale de fiche [#358](https://github.com/betagouv/zacharie/issues/358).
- Amélioration des filtres pour les collecteurs [#357](https://github.com/betagouv/zacharie/issues/357).
- Ajout d'une liste de lésions [#331](https://github.com/betagouv/zacharie/issues/331).
- Ajout de headers spécifiques pour les fiches SVI/FEI [#323](https://github.com/betagouv/zacharie/issues/323) et ETG [#319](https://github.com/betagouv/zacharie/issues/319).
- Amélioration de l'interface utilisateur pour la carte des carcasses [#312](https://github.com/betagouv/zacharie/issues/312).
- Correction du calcul du BPH [#326](https://github.com/betagouv/zacharie/issues/326).
- Correction de l'affichage du nombre total de carcasses [#344](https://github.com/betagouv/zacharie/issues/344).
- Correction de l'accès aux destinataires des fiches pour les chasseurs [#378](https://github.com/betagouv/zacharie/issues/378).
- Correction du bouton de création de fiche pour les chasseurs [#375](https://github.com/betagouv/zacharie/issues/375).
- Correction de l'invitation pour les chasseurs [#377](https://github.com/betagouv/zacharie/issues/377).
- Correction du toggle admin [#376](https://github.com/betagouv/zacharie/issues/376).
- Correction du déconnexion [#341](https://github.com/betagouv/zacharie/issues/341).
- Correction de la cloture automatique des circuits courts [#343](https://github.com/betagouv/zacharie/issues/343).

### Évolutions techniques
- Nettoyage des vieux liens du backend [#372](https://github.com/betagouv/zacharie/issues/372).
- Nettoyage des controllers et des fonctions de synchronisation [#371](https://github.com/betagouv/zacharie/issues/371).
- Simplification du controller utilisateur [#364](https://github.com/betagouv/zacharie/issues/364).
- Split du controller admin [#369](https://github.com/betagouv/zacharie/issues/369).
- Suppression de code legacy [#368](https://github.com/betagouv/zacharie/issues/368).
- Ajout de tests E2E [#315](https://github.com/betagouv/zacharie/issues/315) et [#340](https://github.com/betagouv/zacharie/issues/340).
- Correction de tests flaky [#352](https://github.com/betagouv/zacharie/issues/352).
- Mise en place d'un timeout plus robuste pour le clear cache [#379](https://github.com/betagouv/zacharie/issues/379).
- Implémentation d'un système de bearer token pour les appels API [#336](https://github.com/betagouv/zacharie/issues/336).
- Optimisation des images [#334](https://github.com/betagouv/zacharie/issues/334) et [#327](https://github.com/betagouv/zacharie/issues/327).
- Amélioration de la gestion des erreurs et des logs.

### Autres changements
- Correction de l'affichage des dates dans les filtres [#367](https://github.com/betagouv/zacharie/issues/367).
- Correction d'un bug lié au scroll-to-top de la navbar [#322](https://github.com/betagouv/zacharie/issues/322).
- Correction de l'affichage du header pour les chasseurs [#325](https://github.com/betagouv/zacharie/issues/325).
- Correction de l'UI pour la création de fiches [#311](https://github.com/betagouv/zacharie/issues/311).
- Correction de l'UI pour la liste des fiches [#302](https://github.com/betagouv/zacharie/issues/302).
- Correction du layout admin [#313](https://github.com/betagouv/zacharie/issues/313).
- Mise à jour des dépendances (fast-uri, ip-address, express-rate-limit, postcss) (ignorées car mises à jour de routine).
- Correction de messages d'erreur [#365](https://github.com/betagouv/zacharie/issues/365), [#335](https://github.com/betagouv/zacharie/issues/335) et autres.
