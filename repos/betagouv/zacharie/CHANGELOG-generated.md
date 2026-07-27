## Changelog : zacharie (30 derniers jours, au 23 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur pour les collecteurs et les SVI (Suivi Vie Individuelle), notamment au niveau des interfaces et des flux de transmission des données. Des optimisations de performance ont également été réalisées, en particulier pour la synchronisation des carcasses. Enfin, des corrections de bugs et des améliorations de la robustesse de l'application ont été implémentées.

### Évolutions fonctionnelles
- Possibilité de choisir une association de chasse lors de la création d'une fiche.
- Acceptation SVI en un clic [#534](https://github.com/betagouv/zacharie/issues/534).
- Ajout d'un tableau de bord pour les SVI [#514](https://github.com/betagouv/zacharie/issues/514).
- Interface pour les laboratoires [#435](https://github.com/betagouv/zacharie/issues/435).
- Notification de l'expéditeur lorsqu'un destinataire renvoie une fiche [#508](https://github.com/betagouv/zacharie/issues/508).
- Affichage du statut "Transmise" (en vert) pour les carcasses transmises en circuit court [#505](https://github.com/betagouv/zacharie/issues/505).
- Amélioration de l'UX générale, notamment sur les fiches collecteurs [#531](https://github.com/betagouv/zacharie/issues/531).
- Affichage conditionnel du bouton "prendre en charge" en fonction du destinataire [#537](https://github.com/betagouv/zacharie/issues/537).
- Correction d'un bug où un examinateur voyait toujours une fiche supprimée dans la liste [#8cf0cf0](https://github.com/betagouv/zacharie/commit/8cf0cf0).

### Évolutions techniques
- Ajout de crons pour le health check de l'application [#540](https://github.com/betagouv/zacharie/issues/540).
- Capture des erreurs "request aborted" pour une meilleure analyse avec Sentry [#541](https://github.com/betagouv/zacharie/issues/541).
- Optimisation de l'endpoint `/sync` pour une meilleure performance [#529](https://github.com/betagouv/zacharie/issues/529).
- Optimisation du backend pour la synchronisation d'un grand nombre de carcasses [#512](https://github.com/betagouv/zacharie/issues/512).
- Compression des données pour accélérer la transmission [#485](https://github.com/betagouv/zacharie/issues/485).
- Suppression des champs dépréciés de la FEI [#521](https://github.com/betagouv/zacharie/issues/521).
- Amélioration de la cohérence de la transmission des données [#519](https://github.com/betagouv/zacharie/issues/519).

### Autres changements
- Ajout d'un dossier pour les scripts internes.
- Masquage des outils de débogage en environnement de staging.
- Amélioration du wording sur plusieurs interfaces (bannières, heures FEI, etc.) [#530](https://github.com/betagouv/zacharie/issues/530), [#524](https://github.com/betagouv/zacharie/issues/524), [#3b34fe3](https://github.com/betagouv/zacharie/commit/3b34fe3).
- Ajout de tracking Matomo sur la page d'accueil [#513](https://github.com/betagouv/zacharie/issues/513) et pour les événements [#503](https://github.com/betagouv/zacharie/issues/503).
- Correction de l'affichage des statistiques pour les utilisateurs SVI.
- Nettoyage des partenaires et suppression d'informations techniques inutiles [#517](https://github.com/betagouv/zacharie/issues/517).
- Adaptation du message d'accueil pour les premiers détenteurs non activés [#518](https://github.com/betagouv/zacharie/issues/518).
- Amélioration de l'affichage du certificat pour qu'il tienne sur une seule page [#441](https://github.com/betagouv/zacharie/issues/441).
- Correction de l'affichage des filtres en mode sidebar pour les SVI [#510](https://github.com/betagouv/zacharie/issues/510).
- Correction de l'affichage des blocs "sous-traitance" et "prise en charge collecteur" après transmission [#507](https://github.com/betagouv/zacharie/issues/507), [#506](https://github.com/betagouv/zacharie/issues/506).
