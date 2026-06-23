## Changelog : zacharie (30 derniers jours, au 22 juin 2026)

### Résumé
Ce mois-ci, l'équipe de développement s'est concentrée sur l'amélioration de la gestion des transmissions de fiches de gibier, en particulier pour les différents acteurs (chasseurs, collecteurs, ETG). Des corrections et améliorations ont été apportées pour fluidifier le processus, notamment en gérant mieux les cas particuliers et en affichant des informations plus pertinentes. L'interface utilisateur a également été améliorée, avec des ajustements pour l'administration et l'onboarding.

### Évolutions fonctionnelles
- Les chasseurs ayant un CFEI peuvent désormais créer une fiche sans la transmettre immédiatement [#469](https://github.com/betagouv/zacharie/issues/469).
- Amélioration de l'affichage des informations sur les fiches, notamment le dernier intermédiaire avant l'ETG [#433](https://github.com/betagouv/zacharie/issues/433).
- Ajout d'un filtre "Saison" (1er juin - 31 mai) sur les pages de gestion des fiches [#427](https://github.com/betagouv/zacharie/issues/427).
- Possibilité d'exporter les fiches de manière modulaire [#445](https://github.com/betagouv/zacharie/issues/445).
- Affichage des carcasses groupées par destinataire pour les chasseurs [#409](https://github.com/betagouv/zacharie/issues/409).
- Ajout d'un bouton pour supprimer un utilisateur depuis l'interface d'administration [#429](https://github.com/betagouv/zacharie/issues/429).
- Amélioration de l'onboarding, avec la prise en compte obligatoire de la formation initiale [#422](https://github.com/betagouv/zacharie/issues/422).
- Gestion du statut "clôturée" d'une FEI via ses carcasses [#414](https://github.com/betagouv/zacharie/issues/414).
- Page listant les utilisateurs ayant interagi avec un ETG [#415](https://github.com/betagouv/zacharie/issues/415).

### Évolutions techniques
- Corrections liées à la gestion des transmissions pour les chasseurs, collecteurs et ETG [#474](https://github.com/betagouv/zacharie/issues/474), [#466](https://github.com/betagouv/zacharie/issues/466), [#452](https://github.com/betagouv/zacharie/issues/452).
- Amélioration de la recherche, qui se base désormais sur les données locales [#473](https://github.com/betagouv/zacharie/issues/473).
- Refactorisation du code lié aux carcasses et aux intermédiaires [#464](https://github.com/betagouv/zacharie/issues/464), [#451](https://github.com/betagouv/zacharie/issues/451).
- Optimisation du chargement des données et gestion du cache pour améliorer la performance [#402](https://github.com/betagouv/zacharie/issues/402).
- Simplification du calcul du BPH et de ses constantes [#456](https://github.com/betagouv/zacharie/issues/456).
- Suppression de code legacy lié à Tipimail [#425](https://github.com/betagouv/zacharie/issues/425).

### Autres changements
- Améliorations de l'interface utilisateur du panel d'administration [#460](https://github.com/betagouv/zacharie/issues/460), [#430](https://github.com/betagouv/zacharie/issues/430).
- Ajout de la documentation pour les emails [#426](https://github.com/betagouv/zacharie/issues/426).
- Mise à jour des scopes de départements pour les utilisateurs [#411](https://github.com/betagouv/zacharie/issues/411).
- Ajout d'un tracker pour les erreurs 404 [#420](https://github.com/betagouv/zacharie/issues/420).
- Corrections de bugs et améliorations diverses de l'expérience utilisateur [#479](https://github.com/betagouv/zacharie/issues/479), [#480](https://github.com/betagouv/zacharie/issues/480).
- Amélioration de la gestion des erreurs Sentry et correction de faux positifs [#416](https://github.com/betagouv/zacharie/issues/416), [#417](https://github.com/betagouv/zacharie/issues/417).
