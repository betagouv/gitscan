## Changelog : zacharie (30 derniers jours, au 04 juillet 2026)

### Résumé
Ce mois-ci, l'équipe a continué d'améliorer l'application Zacharie, avec un focus particulier sur la transmission des données, l'expérience utilisateur pour les différents types d'utilisateurs (chasseurs, ETG, laboratoires) et la correction de bugs pour assurer une meilleure stabilité. Des améliorations ont également été apportées à l'interface d'administration et à la gestion des fiches.

### Évolutions fonctionnelles
- Ajout d'une interface pour les laboratoires [#435](https://github.com/betagouv/zacharie/issues/435).
- Possibilité pour un chasseur avec CFEI de créer une fiche sans la transmettre immédiatement [#469](https://github.com/betagouv/zacharie/issues/469).
- Notification de l'expéditeur lorsqu'un destinataire renvoie une fiche [#508](https://github.com/betagouv/zacharie/issues/508).
- Amélioration de l'affichage des statistiques pour les SVI (Suivi Vie Indépendante) [#502](https://github.com/betagouv/zacharie/issues/502).
- Affichage du dernier intermédiaire avant l'ETG sur la FEI [#433](https://github.com/betagouv/zacharie/issues/433).
- Possibilité d'exporter les fiches de manière modulaire [#445](https://github.com/betagouv/zacharie/issues/445).
- Amélioration de l'interface de création de fiches et de demande de modifications [#444](https://github.com/betagouv/zacharie/issues/444).
- Refonte des statistiques SVI sur la page utilisateur ETG [#502](https://github.com/betagouv/zacharie/issues/502).
- Amélioration du parcours d'onboarding pour les ETG, collecteurs, SVI et circuit-court [#458](https://github.com/betagouv/zacharie/issues/458).

### Évolutions techniques
- Compression des données pour accélérer la transmission [#485](https://github.com/betagouv/zacharie/issues/485).
- Optimisation de la gestion des carcasses et des fiches pour améliorer les performances.
- Suppression de code déprécié lié à la FEI [#521](https://github.com/betagouv/zacharie/issues/521).
- Refactoring de la gestion des transmissions pour les chasseurs, ETG et collecteurs [#474](https://github.com/betagouv/zacharie/issues/474), [#452](https://github.com/betagouv/zacharie/issues/452), [#466](https://github.com/betagouv/zacharie/issues/466).
- Amélioration de la gestion de la connectivité réseau.

### Autres changements
- Mise à jour du wording sur la landing page et dans l'application.
- Amélioration de l'interface d'administration (panel admin) [#460](https://github.com/betagouv/zacharie/issues/460).
- Ajout de documentation pour les emails.
- Correction de divers bugs et améliorations de l'expérience utilisateur mineures.
- Ajout de la gestion de la trichine et début du backend associé [#434](https://github.com/betagouv/zacharie/issues/434).
- Mise à jour des constantes et des configurations.
- Ajout de tracking Matomo pour l'analyse des événements [#503](https://github.com/betagouv/zacharie/issues/503) et [#513](https://github.com/betagouv/zacharie/issues/513).
