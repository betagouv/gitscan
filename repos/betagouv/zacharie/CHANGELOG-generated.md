## Changelog : zacharie (30 derniers jours, au 28 juillet 2026)

### Résumé
Ce mois-ci, l'application Zacharie a bénéficié d'améliorations significatives pour les utilisateurs SVI (Suivi Sanitaire des Gibiers), notamment un tableau de bord dédié et une simplification de l'acceptation des données. Des optimisations ont été apportées à la synchronisation des données et à la gestion des carcasses, améliorant la performance et la fiabilité de l'application. Plusieurs corrections de bugs ont également été implémentées pour améliorer l'expérience utilisateur globale.

### Évolutions fonctionnelles
- Ajout d'un tableau de bord dédié aux SVI, offrant une vue d'ensemble des données pertinentes. [#514](https://github.com/betagouv/zacharie/issues/514)
- Simplification de l'acceptation SVI en un seul clic. [#534](https://github.com/betagouv/zacharie/issues/534)
- Possibilité de choisir une association de chasse lors de la création d'une fiche.
- Notification de l'expéditeur lorsqu'un destinataire renvoie une fiche. [#508](https://github.com/betagouv/zacharie/issues/508)
- Amélioration de l'interface utilisateur pour les filtres SVI en mode sidebar. [#510](https://github.com/betagouv/zacharie/issues/510)
- Correction de la redirection vers la page de réinitialisation du mot de passe sur l'application iOS/Android. [#543](https://github.com/betagouv/zacharie/issues/543)
- Correction d'un bug où un examinateur voyait toujours une fiche supprimée dans la liste.
- Ajout d'une interface pour les laboratoires. [#435](https://github.com/betagouv/zacharie/issues/435)
- Affichage du statut "Transmise" en vert pour les carcasses transmises en circuit court. [#505](https://github.com/betagouv/zacharie/issues/505)

### Évolutions techniques
- Ajout de crons pour des vérifications de santé (health check). [#540](https://github.com/betagouv/zacharie/issues/540)
- Capture des erreurs "request aborted" pour une meilleure analyse avec Sentry. [#541](https://github.com/betagouv/zacharie/issues/541)
- Optimisation de l'endpoint `/sync` pour une meilleure performance. [#529](https://github.com/betagouv/zacharie/issues/529)
- Optimisation du backend pour la synchronisation d'un grand nombre de carcasses. [#512](https://github.com/betagouv/zacharie/issues/512)
- Compression des données pour accélérer la transmission. [#485](https://github.com/betagouv/zacharie/issues/485)
- Ajout d'un dossier pour les scripts internes.
- Masquage des outils de débogage en environnement de staging.

### Autres changements
- Amélioration du wording sur différents écrans (bannières, heures FEI, etc.). [#524](https://github.com/betagouv/zacharie/issues/524), [#530](https://github.com/betagouv/zacharie/issues/530)
- Suppression des champs dépréciés de la FEI. [#521](https://github.com/betagouv/zacharie/issues/521)
- Amélioration de la gestion de la transmission des données pour assurer la cohérence. [#519](https://github.com/betagouv/zacharie/issues/519)
- Correction de la gestion des partenaires et suppression d'informations techniques inutiles. [#517](https://github.com/betagouv/zacharie/issues/517)
- Amélioration du message d'accueil pour les premiers détenteurs non activés. [#518](https://github.com/betagouv/zacharie/issues/518)
- Ajout de tracking Matomo pour les événements. [#503](https://github.com/betagouv/zacharie/issues/503)
- Ajout de tracking sur la page d'atterrissage. [#513](https://github.com/betagouv/zacharie/issues/513)
- Optimisation de l'espace pour afficher le certificat sur une seule page si possible. [#441](https://github.com/betagouv/zacharie/issues/441)
- Masquage des statistiques pour les utilisateurs SVI.
- Correction de la création de fiches et limitation du nombre de dispatchs. [#515](https://github.com/betagouv/zacharie/issues/515)
- Correction de l'affichage des carcasses pour les collecteurs. [#528](https://github.com/betagouv/zacharie/issues/528)
- Correction de la pagination sur les fiches collecteurs.
- Amélioration de l'UX générale. [#531](https://github.com/betagouv/zacharie/issues/531)
