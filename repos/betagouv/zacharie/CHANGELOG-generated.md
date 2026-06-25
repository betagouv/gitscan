## Changelog : zacharie (30 derniers jours, au 24 juin 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de la gestion des transmissions de données, notamment pour les chasseurs, les ETG et les collecteurs. De nombreuses corrections ont été apportées pour fluidifier le processus de suivi du gibier, de la chasse à la consommation, et améliorer l'expérience utilisateur, en particulier dans l'interface d'administration. Des fonctionnalités d'export de données et de gestion des utilisateurs ont également été ajoutées.

### Évolutions fonctionnelles
- Possibilité pour un chasseur avec un CFEI de créer une fiche sans la transmettre immédiatement [#469](https://github.com/betagouv/zacharie/issues/469).
- Ajout d'un filtre "Saison" (1er juin - 31 mai) sur les pages de gestion des fiches [#427](https://github.com/betagouv/zacharie/issues/427).
- Implémentation de l'export modulaire des fiches [#445](https://github.com/betagouv/zacharie/issues/445).
- Affichage du dernier intermédiaire avant l'ETG sur la fiche de l'animal [#433](https://github.com/betagouv/zacharie/issues/433).
- Amélioration de l'interface utilisateur et de l'expérience utilisateur pour la création de fiches et les demandes de modifications [#444](https://github.com/betagouv/zacharie/issues/444).
- Affichage des sous-totaux de carcasses par espèce [#424](https://github.com/betagouv/zacharie/issues/424).
- Ajout d'un bouton pour supprimer un utilisateur depuis l'interface d'administration [#429](https://github.com/betagouv/zacharie/issues/429).
- Possibilité de gérer le statut "clôturée" d'une fiche via ses carcasses [#414](https://github.com/betagouv/zacharie/issues/414).
- Page listant les utilisateurs ayant interagi avec un ETG [#415](https://github.com/betagouv/zacharie/issues/415).

### Évolutions techniques
- Refonte de la gestion des transmissions pour les chasseurs, les ETG et les collecteurs [#474](https://github.com/betagouv/zacharie/issues/474), [#466](https://github.com/betagouv/zacharie/issues/466), [#452](https://github.com/betagouv/zacharie/issues/452).
- Optimisation de la recherche qui se base désormais sur les données locales [#473](https://github.com/betagouv/zacharie/issues/473).
- Amélioration de la gestion des carcasses et de leur indexation dans la base de données [#482](https://github.com/betagouv/zacharie/issues/482).
- Simplification du calcul du BPH et de ses constantes [#456](https://github.com/betagouv/zacharie/issues/456).
- Suppression de code legacy lié à tipimail [#425](https://github.com/betagouv/zacharie/issues/425).
- Mise à jour des scopes des départements pour les utilisateurs [#411](https://github.com/betagouv/zacharie/issues/411).

### Autres changements
- Corrections de bugs concernant l'affichage des carcasses en cours de traitement [#495](https://github.com/betagouv/zacharie/issues/495), les pages blanches après renvoi ou sous-traitance [#494](https://github.com/betagouv/zacharie/issues/494), l'usage domestique [#406](https://github.com/betagouv/zacharie/issues/406), et le bouton manquant pour la consommation domestique.
- Corrections diverses concernant la pagination, la gestion des fiches splittées et réunies, et la transmission des données [#486](https://github.com/betagouv/zacharie/issues/486), [#489](https://github.com/betagouv/zacharie/issues/489), [#488](https://github.com/betagouv/zacharie/issues/488).
- Suppression des fichiers FEI inutiles [#491](https://github.com/betagouv/zacharie/issues/491).
- Améliorations continues du panel d'administration [#460](https://github.com/betagouv/zacharie/issues/460).
- Ajout de la documentation pour les emails.
- Ajout d'un tracker pour les pages 404.
- Mise à jour des tests et correction de faux positifs dans Sentry.
