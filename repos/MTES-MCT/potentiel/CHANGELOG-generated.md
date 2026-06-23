## Changelog : potentiel (30 derniers jours, au 22 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau des formulaires, de la gestion des erreurs et de la navigation. Des corrections de bugs ont été apportées pour améliorer la stabilité et la fiabilité de la plateforme. Des améliorations techniques ont également été réalisées pour optimiser les performances et la maintenance du code.

### Évolutions fonctionnelles
- Amélioration de la gestion des coordonnées géodésiques, désormais formatées en français. [#4363](https://github.com/MTES-MCT/potentiel/issues/4363)
- Correction du comportement de la pagination à la page 4. [#4374](https://github.com/MTES-MCT/potentiel/issues/4374)
- Redirection après invitation à un projet éliminé. [#4357](https://github.com/MTES-MCT/potentiel/issues/4357)
- Redirection GF après achèvement pour les projets non soumis. [#4364](https://github.com/MTES-MCT/potentiel/issues/4364)
- Possibilité pour les agents de l'administration (DREAL) de modifier les Garanties Financières (GF) en cours si une demande de mainlevée est en cours. [#4345](https://github.com/MTES-MCT/potentiel/issues/4345)
- Ajout de la possibilité d'enregistrer le rapport associé lorsqu'une attestation de conformité existe déjà. [#4360](https://github.com/MTES-MCT/potentiel/issues/4360)
- Ajout de la possibilité pour le porteur de projet de corriger son numéro SIRET/SIREN. [#4322](https://github.com/MTES-MCT/potentiel/issues/4322)
- Ajout de la description de l'AO/famille dans la section CDC. [#4282](https://github.com/MTES-MCT/potentiel/issues/4282)
- Amélioration de la navigation au clavier du composant Multiselect. [#4346](https://github.com/MTES-MCT/potentiel/issues/4346)
- Ajout de la technologie aux exports lauréat et éliminés. [#4323](https://github.com/MTES-MCT/potentiel/issues/4323)
- Ajout d'un indicateur visuel pour les dossiers DCR manquants sur la page projet. [#4315](https://github.com/MTES-MCT/potentiel/issues/4315) et [#4316](https://github.com/MTES-MCT/potentiel/issues/4316)
- Possibilité d'ouvrir un document directement sans le télécharger. [#4068](https://github.com/MTES-MCT/potentiel/issues/4068)
- Ajout d'une instruction pour l'abandon de projet avec choix de l'option PPA. [#4260](https://github.com/MTES-MCT/potentiel/issues/4260)
- Amélioration de l'affichage des badges dans les listes. [#4277](https://github.com/MTES-MCT/potentiel/issues/4277)
- Ajout de la possibilité pour le porteur de projet de modifier l'attestation de conformité avec son rapport associé. [#4264](https://github.com/MTES-MCT/potentiel/issues/4264)

### Évolutions techniques
- Simplification des readable streams. [#4321](https://github.com/MTES-MCT/potentiel/issues/4321)
- Suppression de l'adapter projets éligibles recandidature. [#4354](https://github.com/MTES-MCT/potentiel/issues/4354)
- Suppression du script de migration des détails de candidature. [#4337](https://github.com/MTES-MCT/potentiel/issues/4337)
- Suppression des schémas inutiles dans la base de données PostgreSQL. [#4294](https://github.com/MTES-MCT/potentiel/issues/4294)
- Utilisation des SHA1 des GitHub Actions plutôt que des tags pour la construction. [#4310](https://github.com/MTES-MCT/potentiel/issues/4310)
- Correction du proxy withAuth. [#4283](https://github.com/MTES-MCT/potentiel/issues/4283)
- Forcer l'usage de Proconnect pour CRE et ADEME. [#4327](https://github.com/MTES-MCT/potentiel/issues/4327)
- Suppression de l'adapter `getIdentifiantProjetFromLegacyId` et de la page de redirection legacy. [#4338](https://github.com/MTES-MCT/potentiel/issues/4338)
- Ajout de l'opérateur `BETWEEN` pour les requêtes. [#4349](https://github.com/MTES-MCT/potentiel/issues/4349)
- Mise à jour de la librairie `better-auth`. [#4284](https://github.com/MTES-MCT/potentiel/issues/4284)

### Autres changements
- Amélioration de l'accessibilité : liens d'évitement et hiérarchie des titres. [#4350](https://github.com/MTES-MCT/potentiel/issues/4350) et [#4348](https://github.com/MTES-MCT/potentiel/issues/4348)
- Corrections de typos et améliorations de la formulation.
- Amélioration de la gestion des erreurs et des validations de formulaires.
- Corrections de bugs mineurs et améliorations de la stabilité.
- Ajout de types pour le fournisseur PV. [#4290](https://github.com/MTES-MCT/potentiel/issues/4290)
- Ajout d'une tâche à la notification si le numéro d'identification est vide. [#4332](https://github.com/MTES-MCT/potentiel/issues/4332)
- Ajout d'AO Petit PV. [#4329](https://github.com/MTES-MCT/potentiel/issues/4329)
- Correction d'un flaky test dans `corrigerCandidature`. [#4319](https://github.com/MTES-MCT/potentiel/issues/4319)
- Correction d'un flaky test pour la génération d'un SIRET aléatoire. [#4328](https://github.com/MTES-MCT/potentiel/issues/4328)
- Amélioration de l'affichage des projections GFS. [#4351](https://github.com/MTES-MCT/potentiel/issues/4351)
- Correction de l'affichage du raccordement PTF. [#4359](https://github.com/MTES-MCT/potentiel/issues/4359)
- Correction de l'affichage des garanties financières. [#4356](https://github.com/MTES-MCT/potentiel/issues/4356)
- Correction de la valeur "false" dans les filtres. [#4355](https://github.com/MTES-MCT/potentiel/issues/4355)
- Correction du lien détail éliminé post recours et amélioration du typage des helpers lauréat. [#4325](https://github.com/MTES-MCT/potentiel/issues/4325)
- Correction de l'affichage des alertes GF en attente. [#4320](https://github.com/MTES-MCT/potentiel/issues/4320)
- Correction des backups S3. [#4370](https://github.com/MTES-MCT/potentiel/issues/4370)
