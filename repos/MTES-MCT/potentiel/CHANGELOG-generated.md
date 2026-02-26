## Changelog : potentiel (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur, notamment en corrigeant des bugs liés à la modification de documents et à l'affichage d'informations. Des améliorations significatives ont également été apportées aux exports de données, avec l'ajout de filtres et de nouvelles colonnes. Enfin, une migration vers ESM (ECMAScript Modules) est en cours pour moderniser le code et améliorer les performances.

### Évolutions fonctionnelles
- Possibilité de filtrer les données lors de l'export CSV (#3937).
- Affichage des filtres actifs lors de l'export CSV (#3937).
- Ajout de la puissance à l'API Achèvement (#3912).
- Amélioration de l'affichage des étapes du projet avec la mise en service du raccordement (#3994).
- Ajout d'un bouton pour supprimer une date de mise en service d'un dossier de raccordement pour les administrateurs (#4008).
- Ajout d'un rôle "Visiteur" (#4030).
- Correction de l'affichage du lien vers le détail du raccordement (#4043).
- Correction de l'import des dates de mise en service (GRD) (#4024).
- Correction de l'affichage de la typologie de projet (#3988, #4016).
- Amélioration de la page des documents, notamment pour la modification des attestations et des demandes de délai (#3923, #3938, #3945).
- Ajout d'un événement pour le statut "Lauréat modifié" (#3917).
- Amélioration de l'UX de la page d'export (#4014).
- Ajout de la référence dans l'ordre des achèvements (#3969).
- Correction du format des emails envoyés aux fournisseurs (#3930).

### Évolutions techniques
- Migration progressive du code vers ESM (ECMAScript Modules) pour les packages Bootstrap, Routes, Infrastructure, ds-api-client, request-context et Librairies/Domaine (#3952, #3960, #3966, #3972, #3973, #3978, #3964).
- Suppression du package `scheduled-tasks` et réorganisation des scripts (#3975).
- Suppression de l'application legacy et configuration du nouveau serveur (#3955).
- Mise à jour de Typespec (#3941).
- Suppression des utilisations de la variable legacy `MAINTENANCE_MODE` (#3999).
- Suppression du FF (Feature Flag) export (#3936).
- Ajout d'un index sur le champ `identifiantProjet` (#3968).
- Amélioration de la tracabilité de la suppression d'un dossier de raccordement (#3925).
- Amélioration de la tracabilité de la modification du GRD d'un projet (#3922).
- Simplification des schémas de correction de candidature (#4045).
- Ajout d'un usecase dédié à la modification d'une date de mise en service (#4007).

### Autres changements
- Documentation sur le mode maintenance (#3999).
- Mise à jour des abonnés (#4001).
- Correction de la configuration de Mailjet (#4038).
- Correction du type de la date de MES dans la vue stats (#4037).
- Suppression de permissions inutilisées (#4026).
- Suppression de l'adapter legacy aBénéficiéCDC2022 (#4023).
- Harmonisation de la redirection des mails pour les domaines migrés (#4027, #3934).
- Ajout de logs pour les requêtes HTTP (#3965).
- Mise à jour des stats Utilisateur pour supprimer l'usage des tables legacy (#4022).
- Ajout de la mise en service du raccordement dans les étapes projet (#3994).
- Ajout des champs AOS dans l'export global des projets (#3970).
- Correction d'une typo dans l'invitation d'utilisateur (#3929).
- Ajout de templates pour les producteurs (#3985).
- Migration des templates de mail pour les délais (#3958) et les recours (#3956).
- Ajout de la section document (#3954).
- Correction de bugs mineurs et améliorations de la qualité du code.
