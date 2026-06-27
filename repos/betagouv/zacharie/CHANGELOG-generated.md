## Changelog : zacharie (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, l'application Zacharie a bénéficié d'une multitude d'améliorations, notamment au niveau de la gestion des ETG (Établissements de Transformation du Gibier), des transmissions de données, et de l'expérience utilisateur. Des corrections de bugs ont été apportées pour améliorer la stabilité et la fiabilité de l'application, et de nouvelles fonctionnalités ont été implémentées pour faciliter le travail des utilisateurs, notamment dans le cadre de la traçabilité de la trichine. L'interface utilisateur a également été améliorée, en particulier pour l'administration et la gestion des fiches.

### Évolutions fonctionnelles
- Possibilité pour un chasseur avec CFEI de créer une fiche sans la transmettre immédiatement [#469](https://github.com/betagouv/zacharie/issues/469).
- Refonte de la page des statistiques SVI pour les utilisateurs ETG [#502](https://github.com/betagouv/zacharie/issues/502).
- Ajout d'un filtre "Saison" (1er juin - 31 mai) sur les pages de gestion des fiches [#427](https://github.com/betagouv/zacharie/issues/427).
- Ajout d'un bouton pour supprimer un utilisateur depuis l'interface d'administration [#429](https://github.com/betagouv/zacharie/issues/429).
- Amélioration de l'affichage du destinataire choisi par le premier détenteur [#423](https://github.com/betagouv/zacharie/issues/423).
- Ajout d'une page listant les utilisateurs ayant interagi avec un ETG [#415](https://github.com/betagouv/zacharie/issues/415).
- Possibilité de gérer le statut "clôturée" d'une FEI via ses carcasses [#414](https://github.com/betagouv/zacharie/issues/414).
- Ajout de détails sur le chasseur pour les ETG [#470](https://github.com/betagouv/zacharie/issues/470).
- Amélioration de l'affichage des sous-totaux de carcasses par espèce [#424](https://github.com/betagouv/zacharie/issues/424).
- Ajout d'une fonctionnalité d'export modulaire des fiches [#445](https://github.com/betagouv/zacharie/issues/445).
- Masquage du bloc destinataire lorsque toutes les carcasses sont assignées [#501](https://github.com/betagouv/zacharie/issues/501).
- Ajout du collecteur dans la liste des utilisateurs d'un ETG [#504](https://github.com/betagouv/zacharie/issues/504).
- Refonte du contenu de la landing page [#500](https://github.com/betagouv/zacharie/issues/500).

### Évolutions techniques
- Suppression des fichiers FEI obsolètes [#491](https://github.com/betagouv/zacharie/issues/491).
- Suppression du champ `svi_assigned_to_fei_at` dans la base de données [#484](https://github.com/betagouv/zacharie/issues/484).
- Amélioration de la gestion des carcasses et des fiches pour optimiser les performances [#465](https://github.com/betagouv/zacharie/issues/465).
- Refactorisation du code lié aux transmissions pour les ETG et les collecteurs [#463](https://github.com/betagouv/zacharie/issues/463), [#452](https://github.com/betagouv/zacharie/issues/452).
- Amélioration de la gestion des utilisateurs et des rôles, notamment pour les administrateurs [#450](https://github.com/betagouv/zacharie/issues/450).
- Mise à jour des scopes de département pour les utilisateurs [#411](https://github.com/betagouv/zacharie/issues/411).
- Suppression du code legacy lié à Tipimail [#425](https://github.com/betagouv/zacharie/issues/425).
- Amélioration de la gestion des erreurs et de la surveillance avec Sentry.

### Autres changements
- Améliorations de l'interface utilisateur et de l'expérience utilisateur sur diverses pages, notamment la création de fiches, les pages d'administration et la gestion des détails [#444](https://github.com/betagouv/zacharie/issues/444), [#430](https://github.com/betagouv/zacharie/issues/430).
- Ajout de documentation pour les emails.
- Ajout de specs pour la gestion de la trichine [#389](https://github.com/betagouv/zacharie/issues/389).
- Corrections de bugs mineurs et améliorations de la stabilité de l'application.
- Ajout d'un tracker pour les erreurs 404.
- Amélioration du panel d'administration [#460](https://github.com/betagouv/zacharie/issues/460).
- Amélioration de l'affichage des villes les plus récentes [#461](https://github.com/betagouv/zacharie/issues/461).
- Correction de problèmes liés à l'onboarding et à l'examen initial obligatoire [#422](https://github.com/betagouv/zacharie/issues/422).
- Ajout d'un bandeau pour le Gamefair.
- Diverses corrections de bugs et améliorations de l'interface utilisateur.
