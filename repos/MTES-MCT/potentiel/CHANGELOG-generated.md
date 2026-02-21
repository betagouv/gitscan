## Changelog : potentiel (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur, notamment en ajoutant de nouvelles fonctionnalités d'export de données, en affinant les permissions d'accès et en corrigeant des bugs. Des efforts importants ont également été déployés pour moderniser l'architecture du projet en migrant vers le format ESM et en optimisant les performances.

### Évolutions fonctionnelles

- Ajout d'un bouton administrateur pour supprimer une date de mise en service d'un dossier de raccordement (#4008).
- Nouveau rôle "Visiteur" implémenté (#4030).
- Amélioration de l'UX sur la page des exports, la rendant plus intuitive (#4014).
- Correction du lien vers le modèle de courrier de recours (#4021).
- Ajout des acteurs manquants dans la frise de raccordement (#4005).
- Possibilité d'exporter les fournisseurs associés à une candidature (#3856, #3918).
- Ajout de filtres sur la page d'export et harmonisation des colonnes retournées (#3927).
- Affichage des filtres actifs lors de l'export CSV (#3937).
- Ajout de la puissance à l'API Achèvement (#3912).
- Ajout de la traçabilité de la transmission de la PTF (#3914).
- Affichage des filtres Appel d'Offres en mode multi-sélection (#3901).
- Mise à jour de l'autorité compétente abandon (#4002).
- Amélioration de l'affichage de la demande en cours lors de modifications administratives (#4006).
- Ajout de la date de mise en service aux exports globaux des lauréats (#3997).
- Utilisation de la mise en service du raccordement dans les étapes du projet (#3994).
- Ajout de la possibilité de modifier la date de mise en service d'un dossier de raccordement via un usecase dédié (#4007).
- Correction d'un bug empêchant la modification de DCR ou PTF sans changement (#4012).
- Correction d'un bug empêchant la modification d'une demande de délai sans modification (#3938).
- Correction d'un bug empêchant la modification d'une attestation sans changement (#3923).
- Correction d'un bug lié à l'ordre alphabétique des menus (#3957).

### Évolutions techniques

- Passage de plusieurs packages (Librairies, Domaine, Infrastructure, Routes, Bootstrap, CLI, Projectors, Statistiques Publiques, ds-api-client, request-context) au format ESM pour une meilleure compatibilité et performance (#3900, #3908, #3909, #3910, #3911, #3960, #3966, #3972, #3973, #3978).
- Suppression du package `scheduled-tasks` et réorganisation des scripts (#3975).
- Suppression des utilisations de la variable legacy `MAINTENANCE_MODE` (#4000).
- Mise à jour de Typespec (#3941).
- Suppression de l'adapter legacy aBénéficiéCDC2022 (#4023).
- Suppression de permissions inutilisées (#4026).
- Migration des templates de mail (délai, recours) (#3956, #3958).
- Migration des templates nature de l'exploitation et actionnaire (#3954, #3963, #3989).
- Migration des notifications domaine installation (#4009).
- Mise à jour des stats Utilisateur pour supprimer l'usage des tables legacy (#4022).
- Mise en place d'une vérification des permissions d'exécution des usecases (#3993).
- DépôtSchéma devient le schéma de référence (#3981).
- Ajout d'un index sur le champ identifiantProjet (#3968).
- Réduction de la verbosité des logs pour les résultats des requêtes Liste (#4010).

### Autres changements

- Documentation sur le mode maintenance ajoutée (#3999).
- Suppression du FF export (#3936).
- Suppression de la génération de fichier détail lors de l'import / correction de candidature (#3934).
- Mise à jour des subscribers (#4001).
- Correction de la technologie des projets PV - Eolien (#3980).
- Correction d'un bug dans l'ordre des achèvements (#3969).
- Correction d'un bug lié à l'affichage du coefficient K pour les AOs concernés (#3920).
- Correction d'un bug lié à l'accès à la page "éliminés" (#3926).
- Correction d'un bug lié au comportement lors de la sélection d'un cycle sans AO sélectionné (#3916).
- Correction d'un bug lié à l'import des dates de mise en service (GRD) (#4024).
- Intégration des modifications de la release 3.70, 3.71, 3.72 et 3.73 (#3921, #3932, #3964, #4013, #4018, #4025).
