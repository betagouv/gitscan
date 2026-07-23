## Changelog : zacharie (30 derniers jours, au 22 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur, notamment pour les SVI (Suivi Vie Individuelle) et les ETG (Établissements de Transformation du Gibier). Des optimisations de performance ont été réalisées, en particulier pour la synchronisation des carcasses et la transmission de données. De nouvelles fonctionnalités ont été ajoutées, comme l'acceptation SVI en un clic et un tableau de bord dédié aux SVI.

### Évolutions fonctionnelles
- Ajout d'un tableau de bord dédié aux SVI [#514](https://github.com/betagouv/zacharie/issues/514).
- Acceptation SVI en un clic pour simplifier le processus [#534](https://github.com/betagouv/zacharie/issues/534).
- Amélioration de l'interface utilisateur pour les collecteurs, notamment l'affichage de "prendre en charge" uniquement si le collecteur est le prochain destinataire [#537](https://github.com/betagouv/zacharie/issues/537).
- Refonte des statistiques SVI sur la page utilisateur ETG [#502](https://github.com/betagouv/zacharie/issues/502).
- Ajout d'une interface pour les laboratoires [#435](https://github.com/betagouv/zacharie/issues/435).
- Notification de l'expéditeur lorsqu'un destinataire renvoie une fiche [#508](https://github.com/betagouv/zacharie/issues/508).
- Amélioration de l'affichage des carcasses transmises en circuit court (passage au vert) [#505](https://github.com/betagouv/zacharie/issues/505).
- Affichage correct des carcasses renvoyées par l'ETG, ne les affichant plus "en cours de traitement" [#495](https://github.com/betagouv/zacharie/issues/495).
- Correction de la page blanche affichée après un renvoi ou une sous-traitance par l'ETG [#494](https://github.com/betagouv/zacharie/issues/494).
- Amélioration de l'affichage des détails du chasseur pour les ETG [#470](https://github.com/betagouv/zacharie/issues/470).
- Correction de l'affichage du bouton pour l'usage domestique [#406](https://github.com/betagouv/zacharie/issues/406).
- Amélioration de la gestion des fiches splittées et réunies au sein d'un même ETG [#489](https://github.com/betagouv/zacharie/issues/489).

### Évolutions techniques
- Ajout de crons pour des vérifications de santé (health check) [#540](https://github.com/betagouv/zacharie/issues/540).
- Capture des erreurs "request aborted" en tant qu'informations (info) plutôt qu'erreurs dans Sentry [#541](https://github.com/betagouv/zacharie/issues/541).
- Optimisation de l'endpoint `/sync` pour une meilleure performance avec un grand nombre de carcasses [#529](https://github.com/betagouv/zacharie/issues/529).
- Optimisation de la compression des données pour accélérer la transmission [#485](https://github.com/betagouv/zacharie/issues/485).
- Optimisation de l'indexation des carcasses dans la base de données [#482](https://github.com/betagouv/zacharie/issues/482).
- Suppression de champs dépréciés de la FEI [#521](https://github.com/betagouv/zacharie/issues/521).
- Suppression de code lié à la mise à jour de la FEI [#483](https://github.com/betagouv/zacharie/issues/483).

### Autres changements
- Ajout d'un dossier pour les scripts internes [#526](https://github.com/betagouv/zacharie/issues/526).
- Masquage des outils de débogage en environnement de staging [#525](https://github.com/betagouv/zacharie/issues/525).
- Amélioration du wording de certains éléments de l'interface utilisateur (bannière d'onboarding, heures FEI, etc.) [#530](https://github.com/betagouv/zacharie/issues/530), [#524](https://github.com/betagouv/zacharie/issues/524).
- Amélioration du tracking Matomo [#503](https://github.com/betagouv/zacharie/issues/503) et ajout de tracking sur la landing [#513](https://github.com/betagouv/zacharie/issues/513).
- Ajustements de design et de wording sur la landing page [#500](https://github.com/betagouv/zacharie/issues/500).
- Correction de petites améliorations et corrections diverses [#531](https://github.com/betagouv/zacharie/issues/531), [#515](https://github.com/betagouv/zacharie/issues/515), [#527](https://github.com/betagouv/zacharie/issues/527), [#499](https://github.com/betagouv/zacharie/issues/499).
