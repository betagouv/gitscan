## Changelog : zacharie (30 derniers jours, au 01 juillet 2026)

### Résumé
Ce mois-ci, l'équipe de développement s'est concentrée sur l'amélioration de l'expérience utilisateur, notamment pour les utilisateurs ETG (Établissement de Transformation du Gibier) et les chasseurs. Des corrections de bugs ont été apportées pour fluidifier les parcours, et de nouvelles fonctionnalités ont été implémentées, comme l'ajout d'une interface pour les laboratoires et la gestion du statut "clôturée" pour les fiches. Des améliorations ont également été apportées à l'administration et au suivi des données.

### Évolutions fonctionnelles
- Ajout d'une interface pour les laboratoires [#435](https://github.com/betagouv/zacharie/issues/435).
- Les carcasses transmises en circuit court s'affichent maintenant en vert avec le statut "Transmise" [#505](https://github.com/betagouv/zacharie/issues/505).
- Refonte des statistiques SVI (Suivi Vie et Itinéraire) sur la page utilisateur ETG [#502](https://github.com/betagouv/zacharie/issues/502).
- Les chasseurs avec un CFEI (Code d'Établissement du Fournisseur Étranger) peuvent maintenant créer une fiche sans la transmettre immédiatement [#469](https://github.com/betagouv/zacharie/issues/469).
- Ajout d'un filtre "Saison" (1er juin - 31 mai) sur les pages de gestion des fiches [#427](https://github.com/betagouv/zacharie/issues/427).
- Possibilité d'exporter les fiches de manière modulaire [#445](https://github.com/betagouv/zacharie/issues/445).
- Ajout d'un bouton pour supprimer un utilisateur depuis l'interface d'administration [#429](https://github.com/betagouv/zacharie/issues/429).
- Amélioration de l'affichage du destinataire choisi par le premier détenteur [#423](https://github.com/betagouv/zacharie/issues/423).
- Ajout d'une page listant les utilisateurs ayant interagi avec un ETG [#415](https://github.com/betagouv/zacharie/issues/415).
- Gestion du statut "clôturée" d'une fiche via ses carcasses [#414](https://github.com/betagouv/zacharie/issues/414).
- Ajout de détails sur le chasseur pour les ETG [#470](https://github.com/betagouv/zacharie/issues/470).

### Évolutions techniques
- Suppression des fichiers FEI obsolètes [#491](https://github.com/betagouv/zacharie/issues/491).
- Suppression de la colonne `svi_assigned_to_fei_at` de la base de données [#484](https://github.com/betagouv/zacharie/issues/484).
- Amélioration de l'indexation des carcasses dans la base de données [#482](https://github.com/betagouv/zacharie/issues/482).
- Refactorisation de la gestion des transmissions pour les chasseurs, ETG et collecteurs [#474](https://github.com/betagouv/zacharie/issues/474), [#466](https://github.com/betagouv/zacharie/issues/466), [#452](https://github.com/betagouv/zacharie/issues/452).
- Suppression du code legacy Tipimail [#425](https://github.com/betagouv/zacharie/issues/425).
- Mise en place de specs pour la gestion de la trichine [#389](https://github.com/betagouv/zacharie/issues/389).

### Autres changements
- Corrections de divers bugs d'affichage et de comportement sur l'interface utilisateur (ETG, SVI, landing page, etc.) [#518](https://github.com/betagouv/zacharie/issues/518), [#510](https://github.com/betagouv/zacharie/issues/510), [#507](https://github.com/betagouv/zacharie/issues/507), [#506](https://github.com/betagouv/zacharie/issues/506), [#504](https://github.com/betagouv/zacharie/issues/504), [#499](https://github.com/betagouv/zacharie/issues/499), [#496](https://github.com/betagouv/zacharie/issues/496), [#495](https://github.com/betagouv/zacharie/issues/495), [#494](https://github.com/betagouv/zacharie/issues/494), [#459](https://github.com/betagouv/zacharie/issues/459), [#457](https://github.com/betagouv/zacharie/issues/457), [#456](https://github.com/betagouv/zacharie/issues/456), [#444](https://github.com/betagouv/zacharie/issues/444), [#443](https://github.com/betagouv/zacharie/issues/443), [#442](https://github.com/betagouv/zacharie/issues/442), [#441](https://github.com/betagouv/zacharie/issues/441), [#437](https://github.com/betagouv/zacharie/issues/437), [#433](https://github.com/betagouv/zacharie/issues/433), [#432](https://github.com/betagouv/zacharie/issues/432), [#431](https://github.com/betagouv/zacharie/issues/431), [#430](https://github.com/betagouv/zacharie/issues/430), [#428](https://github.com/betagouv/zacharie/issues/428), [#422](https://github.com/betagouv/zacharie/issues/422), [#421](https://github.com/betagouv/zacharie/issues/421), [#420](https://github.com/betagouv/zacharie/issues/420), [#415](https://github.com/betagouv/zacharie/issues/415).
- Améliorations du panel d'administration [#460](https://github.com/betagouv/zacharie/issues/460).
- Ajout d'un tracker Matomo pour les événements [#503](https://github.com/betagouv/zacharie/issues/503).
- Mise à jour du wording sur la landing page et dans diverses parties de l'application.
- Corrections liées à l'onboarding des utilisateurs ETG, collecteurs et SVI [#458](https://github.com/betagouv/zacharie/issues/458).
- Ajout d'un bandeau pour le Gamefair [#453](https://github.com/betagouv/zacharie/issues/453).
- Amélioration de la gestion des erreurs et des redirects.
- Ajout de documentation pour les emails.
- Diverses corrections et améliorations de l'UI/UX.
- Suppression du bouton disparu pour la consommation domestique [#489](https://github.com/betagouv/zacharie/issues/489).
- Correction de l'affichage des carcasses renvoyées par l'ETG [#495](https://github.com/betagouv/zacharie/issues/495).
- Correction de la page blanche affichée après un renvoi ou une sous-traitance par l'ETG [#494](https://github.com/betagouv/zacharie/issues/494).
- Correction de l'usage domestique [#406](https://github.com/betagouv/zacharie/issues/406).
- Correction de la pagination des chasseurs [#486](https://github.com/betagouv/zacharie/issues/486).
- Correction du tri des carcasses [#487](https://github.com/betagouv/zacharie/issues/487).
- Correction de la transmission SVI [#476](https://github.com/betagouv/zacharie/issues/476).
- Correction de la recherche [#473](https://github.com/betagouv/zacharie/issues/473).
- Correction de la transmission pour les collecteurs [#466](https://github.com/betagouv/zacharie/issues/466).
- Correction de l'affichage des carcasses indexées [#482](https://github.com/betagouv/zacharie/issues/482).
- Correction de l'affichage du dernier intermédiaire avant l'ETG sur la FEI [#433](https://github.com/betagouv/zacharie/issues/433).
- Correction de l'onboarding, le choix de la formation à l'examen initial est maintenant obligatoire [#422](https://github.com/betagouv/zacharie/issues/422).
- Correction de l'affichage des villes les plus récentes en premières [#461](https://github.com/betagouv/zacharie/issues/461).
- Correction de l'affichage du premier détenteur [#442](https://github.com/betagouv/zacharie/issues/442).
- Correction de la non comparaison des metadatas des carcasses d'une transmission [#480](https://github.com/betagouv/zacharie/issues/480).
- Correction de l'affichage des carcasses orphelines [#479](https://github.com/betagouv/zacharie/issues/479).
- Correction de la transmission pour les chasseurs [#474](https://github.com/betagouv/zacharie/issues/474).
- Correction de la transmission basée sur le numéro de FEI et l'ID du détenteur [#471](https://github.com/betagouv/zacharie/issues/471).
- Correction de la suppression d'un utilisateur lors de la suppression de sa relation avec un ETG [#450](https://github.com/betagouv/zacharie/issues/450).
- Correction de l'arrêt du check de la connectivité réseau [#449](https://github.com/betagouv/zacharie/issues/449).
- Correction de l'affichage du message d'accueil pour les premiers détenteurs non activés [#518](https://github.com/betagouv/zacharie/issues/518).
- Correction du nettoyage des partenaires [#517](https://github.com/betagouv/zacharie/issues/517).
