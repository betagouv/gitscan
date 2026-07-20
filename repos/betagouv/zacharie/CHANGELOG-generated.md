## Changelog : zacharie (30 derniers jours, au 16 juillet 2026)

### Résumé
Ce mois-ci, l'application Zacharie a bénéficié d'améliorations significatives pour les utilisateurs SVI (Suivi Vie Individuelle) et ETG (Établissement de Transformation du Gibier), notamment un nouveau tableau de bord SVI, une refonte des statistiques pour les ETG, et des corrections pour améliorer la transmission et la gestion des carcasses. Des améliorations de l'interface utilisateur et de l'expérience utilisateur ont également été apportées, ainsi que des optimisations des performances.

### Évolutions fonctionnelles
- Ajout d'un tableau de bord SVI pour une meilleure vue d'ensemble des données. [#514](https://github.com/betagouv/zacharie/issues/514)
- Acceptation SVI en un clic pour simplifier le processus. [#534](https://github.com/betagouv/zacharie/issues/534)
- Refonte des statistiques pour les ETG, incluant les détails du chasseur. [#470](https://github.com/betagouv/zacharie/issues/470) et [#502](https://github.com/betagouv/zacharie/issues/502)
- Possibilité pour les chasseurs avec CFEI de créer une fiche sans la transmettre immédiatement. [#469](https://github.com/betagouv/zacharie/issues/469)
- Notification à l'expéditeur lorsqu'un destinataire renvoie une fiche. [#508](https://github.com/betagouv/zacharie/issues/508)
- Amélioration de l'affichage des carcasses transmises en circuit court (statut "Transmise" en vert). [#505](https://github.com/betagouv/zacharie/issues/505)
- Ajout d'une interface pour les laboratoires. [#435](https://github.com/betagouv/zacharie/issues/435)
- Amélioration de la gestion des fiches et des carcasses pour les collecteurs. [#528](https://github.com/betagouv/zacharie/issues/528) et [#525](https://github.com/betagouv/zacharie/issues/525)
- Correction de l'affichage des statuts des carcasses après renvoi par l'ETG. [#495](https://github.com/betagouv/zacharie/issues/495)
- Correction d'une page blanche après renvoi ou sous-traitance par l'ETG. [#494](https://github.com/betagouv/zacharie/issues/494)

### Évolutions techniques
- Optimisation de l'endpoint `/sync` pour une meilleure performance avec un grand nombre de carcasses. [#529](https://github.com/betagouv/zacharie/issues/529)
- Compression des données pour accélérer la transmission. [#485](https://github.com/betagouv/zacharie/issues/485)
- Optimisation de la base de données (indexation des carcasses). [#482](https://github.com/betagouv/zacharie/issues/482)
- Suppression des champs dépréciés de la FEI. [#521](https://github.com/betagouv/zacharie/issues/521)
- Suppression de code obsolète lié à la FEI. [#483](https://github.com/betagouv/zacharie/issues/483) et [#484](https://github.com/betagouv/zacharie/issues/484)
- Amélioration de la gestion des erreurs et de la cohérence des données lors de la transmission. [#519](https://github.com/betagouv/zacharie/issues/519)

### Autres changements
- Améliorations de l'interface utilisateur (wording, design, filtres) pour les SVI et les ETG. [#530](https://github.com/betagouv/zacharie/issues/530), [#510](https://github.com/betagouv/zacharie/issues/510), [#503](https://github.com/betagouv/zacharie/issues/503), [#499](https://github.com/betagouv/zacharie/issues/499), [#496](https://github.com/betagouv/zacharie/issues/496)
- Ajout d'un dossier pour les scripts internes.
- Masquage des outils de débogage en environnement de staging.
- Ajout de tracking Matomo sur la landing page. [#513](https://github.com/betagouv/zacharie/issues/513)
- Amélioration du wording sur la landing page.
- Correction de bugs divers et amélioration de la stabilité de l'application. [#531](https://github.com/betagouv/zacharie/issues/531), [#527](https://github.com/betagouv/zacharie/issues/527), [#524](https://github.com/betagouv/zacharie/issues/524), [#517](https://github.com/betagouv/zacharie/issues/517), [#518](https://github.com/betagouv/zacharie/issues/518), [#515](https://github.com/betagouv/zacharie/issues/515), [#507](https://github.com/betagouv/zacharie/issues/507), [#506](https://github.com/betagouv/zacharie/issues/506), [#501](https://github.com/betagouv/zacharie/issues/501), [#491](https://github.com/betagouv/zacharie/issues/491), [#488](https://github.com/betagouv/zacharie/issues/488), [#487](https://github.com/betagouv/zacharie/issues/487), [#480](https://github.com/betagouv/zacharie/issues/480), [#479](https://github.com/betagouv/zacharie/issues/479), [#476](https://github.com/betagouv/zacharie/issues/476), [#462](https://github.com/betagouv/zacharie/issues/462), [#441](https://github.com/betagouv/zacharie/issues/441), [#406](https://github.com/betagouv/zacharie/issues/406), [#489](https://github.com/betagouv/zacharie/issues/489)
