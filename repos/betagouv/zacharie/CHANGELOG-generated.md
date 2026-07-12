## Changelog : zacharie (30 derniers jours, au 10 juillet 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur pour les différents acteurs (chasseurs, collecteurs, ETG, laboratoires) avec une attention particulière portée à la transmission et à la gestion des fiches de gibier. Des optimisations ont été apportées pour améliorer la performance et la fiabilité de l'application, notamment au niveau de la synchronisation des données et de la gestion des carcasses. L'interface utilisateur a également été revue et corrigée sur plusieurs points.

### Évolutions fonctionnelles
- Ajout d'un tableau de bord SVI pour les collecteurs [#514](https://github.com/betagouv/zacharie/issues/514).
- Possibilité pour un chasseur avec CFEI de créer une fiche sans la transmettre immédiatement [#469](https://github.com/betagouv/zacharie/issues/469).
- Notification de l'expéditeur lorsqu'un destinataire renvoie une fiche [#508](https://github.com/betagouv/zacharie/issues/508).
- Ajout d'une interface pour les laboratoires [#435](https://github.com/betagouv/zacharie/issues/435).
- Refonte des statistiques SVI sur la page utilisateur ETG.
- Amélioration de l'affichage des carcasses transmises en circuit court (statut "Transmise" en vert) [#505](https://github.com/betagouv/zacharie/issues/505).
- Amélioration de la gestion des fiches et des carcasses pour les ETG, notamment en cas de division et de regroupement de carcasses [#489](https://github.com/betagouv/zacharie/issues/489).
- Possibilité d'exporter les fiches de manière modulaire [#445](https://github.com/betagouv/zacharie/issues/445).
- Amélioration de l'onboarding pour les ETG, collecteurs, SVI et circuit-court, en supprimant la dépendance à la page "notifications" [#458](https://github.com/betagouv/zacharie/issues/458).
- Affichage du dernier intermédiaire avant l'ETG sur la FEI [#433](https://github.com/betagouv/zacharie/issues/433).

### Évolutions techniques
- Optimisation du backend pour la synchronisation d'un grand nombre de carcasses [#512](https://github.com/betagouv/zacharie/issues/512).
- Compression des données pour accélérer la transmission [#485](https://github.com/betagouv/zacharie/issues/485).
- Suppression des champs dépréciés de la FEI [#521](https://github.com/betagouv/zacharie/issues/521).
- Amélioration de la gestion des erreurs et de la cohérence des données lors de la transmission [#519](https://github.com/betagouv/zacharie/issues/519).
- Refactorisation du code lié à la transmission des données pour les ETG et les collecteurs [#466](https://github.com/betagouv/zacharie/issues/466).
- Suppression de code obsolète et nettoyage du code.
- Ajout de scripts internes pour faciliter le développement [#526](https://github.com/betagouv/zacharie/issues/526).

### Autres changements
- Corrections de wording et d'UI sur diverses pages (onboarding, fiches, filtres, etc.) [#530](https://github.com/betagouv/zacharie/issues/530), [#524](https://github.com/betagouv/zacharie/issues/524), [#515](https://github.com/betagouv/zacharie/issues/515), [#3b34fe3](https://github.com/betagouv/zacharie/commit/3b34fe3).
- Corrections de bugs et améliorations de la stabilité de l'application.
- Mise à jour des tests et correction de tests défaillants.
- Ajout de tracking Matomo pour suivre les événements utilisateurs [#503](https://github.com/betagouv/zacharie/issues/503), [#513](https://github.com/betagouv/zacharie/issues/513).
- Amélioration de la pagination sur les fiches collecteurs.
- Masquage des statistiques pour les utilisateurs SVI.
- Diverses corrections de bugs liés à l'affichage et au comportement de l'application.
