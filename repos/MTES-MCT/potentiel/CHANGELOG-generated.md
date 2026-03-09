## Changelog : potentiel (30 derniers jours)

### Résumé
Ce changelog résume les évolutions apportées à Potentiel au cours des 30 derniers jours. Les mises à jour incluent des améliorations de l'interface utilisateur, des corrections de bugs, des migrations techniques importantes pour moderniser le code et l'infrastructure, ainsi que des ajustements de données et de permissions. Ces changements visent à améliorer la performance, la sécurité et l'expérience utilisateur de la plateforme.

### Évolutions fonctionnelles
- Ajout de la possibilité pour les administrateurs de supprimer une date de mise en service d'un dossier de raccordement. [#4008](https://github.com/MTES-MCT/potentiel/issues/4008)
- Amélioration de l'affichage des liens de détails de raccordement. [#4043](https://github.com/MTES-MCT/potentiel/issues/4043)
- Ajout de la vérification des colonnes lors de l'import d'un CSV de candidats. [#3962](https://github.com/MTES-MCT/potentiel/issues/3962)
- Ajout d'un bouton administrateur pour supprimer une date de mise en service. [#4008](https://github.com/MTES-MCT/potentiel/issues/4008)
- Ajout de la possibilité de filtrer les projets notifiés dans l'export des fournisseurs. [#3986](https://github.com/MTES-MCT/potentiel/issues/3986)
- Ajout d'un nouveau rôle "Visiteur". [#4030](https://github.com/MTES-MCT/potentiel/issues/4030)
- Amélioration de l'affichage de la demande en cours lors de modifications administratives. [#4006](https://github.com/MTES-MCT/potentiel/issues/4006)
- Ajout de la mise en service du raccordement d'un projet et dans les étapes projet. [#3994](https://github.com/MTES-MCT/potentiel/issues/3994) et [#3984](https://github.com/MTES-MCT/potentiel/issues/3984)
- Ajout des champs AOS dans l'export global des projets. [#3970](https://github.com/MTES-MCT/potentiel/issues/3970)
- Amélioration de l'UX de la page d'export. [#4014](https://github.com/MTES-MCT/potentiel/issues/4014)
- Ajout d'une fonctionnalité pour lister les utilisateurs éliminés. [#4017](https://github.com/MTES-MCT/potentiel/issues/4017)
- Amélioration des statistiques d'export CSV. [#4028](https://github.com/MTES-MCT/potentiel/issues/4028)

### Évolutions techniques
- Migration vers better-auth pour l'authentification. [#4044](https://github.com/MTES-MCT/potentiel/issues/4044)
- Passage de plusieurs packages (Librairies, Domaine, ds-api-client, document-builder) en ESM (EcmaScript Modules). [#3964](https://github.com/MTES-MCT/potentiel/issues/3964), [#3973](https://github.com/MTES-MCT/potentiel/issues/3973), [#3978](https://github.com/MTES-MCT/potentiel/issues/3978)
- Suppression du package `scheduled-tasks` et réorganisation des scripts. [#3975](https://github.com/MTES-MCT/potentiel/issues/3975)
- Suppression des utilisations de la variable legacy `MAINTENANCE_MODE`. [#3999](https://github.com/MTES-MCT/potentiel/issues/3999)
- Suppression de l'adapter legacy `aBénéficiéCDC2022`. [#4023](https://github.com/MTES-MCT/potentiel/issues/4023)
- Suppression de permissions inutilisées. [#4026](https://github.com/MTES-MCT/potentiel/issues/4026)
- Simplification des schémas de correction de candidature. [#4045](https://github.com/MTES-MCT/potentiel/issues/4045)
- Migration des templates pour représentant légal, garanties financières, accès, puissance, achèvement et tâches planifiées. [#4054](https://github.com/MTES-MCT/potentiel/issues/4054), [#4056](https://github.com/MTES-MCT/potentiel/issues/4056), [#4046](https://github.com/MTES-MCT/potentiel/issues/4046), [#4053](https://github.com/MTES-MCT/potentiel/issues/4053), [#4042](https://github.com/MTES-MCT/potentiel/issues/4042)
- Correction de bugs liés à la transmission de dates MES et à la configuration du timeout de `waitForExpect`. [#4064](https://github.com/MTES-MCT/potentiel/issues/4064), [#4065](https://github.com/MTES-MCT/potentiel/issues/4065)
- Correction des logs de connexion par lien magique. [#4057](https://github.com/MTES-MCT/potentiel/issues/4057)
- Correction de la mise à jour des `userInfo` au signin. [#4058](https://github.com/MTES-MCT/potentiel/issues/4058)

### Autres changements
- Mise à jour des dépendances de sécurité. [#4047](https://github.com/MTES-MCT/potentiel/issues/4047)
- Correction de typos et amélioration de la terminologie. [#4059](https://github.com/MTES-MCT/potentiel/issues/4059)
- Mise à jour du dump de la base de données. [#4055](https://github.com/MTES-MCT/potentiel/issues/4055)
- Ajout d'un utilitaire pour identifier les projets dans les requêtes. [#4041](https://github.com/MTES-MCT/potentiel/issues/4041)
- Correction d'un bug empêchant la modification d'une DCR ou PTF sans changement. [#4012](https://github.com/MTES-MCT/potentiel/issues/4012)
- Suppression d'un motif "inconnu" pour le type de demande de GF, remplacé par "non déposé". [#4052](https://github.com/MTES-MCT/potentiel/issues/4052)
- Ajout d'un event legacy `DateMiseEnServiceModifiée-V1`. [#4035](https://github.com/MTES-MCT/potentiel/issues/4035)
- Correction d'un bug lié à la puissance des projets PV - Eolien. [#3980](https://github.com/MTES-MCT/potentiel/issues/3980)
- Correction d'un bug lié à l'affichage du lien détail raccordement. [#4043](https://github.com/MTES-MCT/potentiel/issues/4043)
- Correction d'un bug lié à l'import des dates de mise en service (GRD). [#4024](https://github.com/MTES-MCT/potentiel/issues/4024)
- Correction d'un bug lié à l'accès admin à la page lister périodes. [#3991](https://github.com/MTES-MCT/potentiel/issues/3991)
- Correction d'un bug lié à la correction de candidature puissance. [#4029](https://github.com/MTES-MCT/potentiel/issues/4029)
- Correction d'un bug lié à la configuration de Mailjet. [#4038](https://github.com/MTES-MCT/potentiel/issues/4038)
- Correction du type de la date de MES dans la vue stats. [#4037](https://github.com/MTES-MCT/potentiel/issues/4037)
- Suppression de l'utilisation du LOGGER LEVEL dans les specs. [#3977](https://github.com/MTES-MCT/potentiel/issues/3977)
- Mise à jour des abonnés. [#4001](https://github.com/MTES-MCT/potentiel/issues/4001)
