## Changelog : potentiel (30 derniers jours)

### Résumé
Ce changelog résume les améliorations et corrections apportées à l'application Potentiel au cours des 30 derniers jours. Les modifications incluent des mises à jour de sécurité, des améliorations de l'interface utilisateur, des corrections de bugs, des migrations de templates de mail et de code vers des standards plus récents (ESM), et des ajustements des permissions d'accès pour renforcer la sécurité.

### Évolutions fonctionnelles

- Ajout d'un bouton administrateur pour supprimer une date de mise en service d'un dossier de raccordement. [#4008](https://github.com/MTES-MCT/potentiel/issues/4008)
- Ajout d'un rôle "Visiteur" avec des permissions spécifiques. [#4030](https://github.com/MTES-MCT/potentiel/issues/4030)
- Amélioration de l'affichage des liens de détails de raccordement. [#4043](https://github.com/MTES-MCT/potentiel/issues/4043)
- Ajout de la vérification des colonnes lors de l'import d'un CSV de candidats. [#3962](https://github.com/MTES-MCT/potentiel/issues/3962)
- Ajout de la possibilité d'exporter les statistiques des projets. [#4028](https://github.com/MTES-MCT/potentiel/issues/4028)
- Ajout de la date de mise en service du raccordement dans les étapes du projet. [#3994](https://github.com/MTES-MCT/potentiel/issues/3994)
- Ajout des champs AOS dans l'export global des projets. [#3970](https://github.com/MTES-MCT/potentiel/issues/3970)
- Ajout d'une nouvelle section "document" dans l'application. [#3954](https://github.com/MTES-MCT/potentiel/issues/3954)
- Ajout de la possibilité de filtrer les fournisseurs lors de l'export. [#3986](https://github.com/MTES-MCT/potentiel/issues/3986)
- Ajout d'un utilitaire pour identifier le projet dans les requêtes. [#4041](https://github.com/MTES-MCT/potentiel/issues/4041)
- Ajout du type de terrain d'implantation dans l'export des lauréats. [#4050](https://github.com/MTES-MCT/potentiel/issues/4050)

### Évolutions techniques

- Migration de plusieurs packages vers ESM (EcmaScript Modules) : Routes, Bootstrap, Infrastructure, request-context, ds-api-client, Domaine, Librairies. [#3966](https://github.com/MTES-MCT/potentiel/issues/3966), [#3972](https://github.com/MTES-MCT/potentiel/issues/3972), [#3978](https://github.com/MTES-MCT/potentiel/issues/3978), [#3960](https://github.com/MTES-MCT/potentiel/issues/3960), [#3952](https://github.com/MTES-MCT/potentiel/issues/3952)
- Mise à jour de Typespec. [#3941](https://github.com/MTES-MCT/potentiel/issues/3941)
- Suppression de Redis et des variables d'environnement legacy. [#3955](https://github.com/MTES-MCT/potentiel/issues/3955)
- Suppression du package `scheduled-tasks` et réorganisation des scripts. [#3975](https://github.com/MTES-MCT/potentiel/issues/3975)
- Migration des templates de mail pour les délais, recours et abandon. [#3958](https://github.com/MTES-MCT/potentiel/issues/3958), [#3956](https://github.com/MTES-MCT/potentiel/issues/3956), [#3949](https://github.com/MTES-MCT/potentiel/issues/3949)
- Migration des schémas de correction de candidature, d'achèvement et d'accès. [#4045](https://github.com/MTES-MCT/potentiel/issues/4045), [#4048](https://github.com/MTES-MCT/potentiel/issues/4048), [#4046](https://github.com/MTES-MCT/potentiel/issues/4046)
- Simplification de la logique de vérification d'accès aux requêtes.
- Ajout d'un index sur le champ `identifiantProjet` dans la base de données. [#3968](https://github.com/MTES-MCT/potentiel/issues/3968)

### Autres changements

- Mises à jour de sécurité. [#4047](https://github.com/MTES-MCT/potentiel/issues/4047)
- Amélioration de la documentation.
- Ajustements des permissions d'accès pour empêcher la modification de données en cas de projet achevé. [#3948](https://github.com/MTES-MCT/potentiel/issues/3948), [#3944](https://github.com/MTES-MCT/potentiel/issues/3944)
- Corrections de bugs mineurs et améliorations de la qualité du code.
- Harmonisation des redirections de mails pour les domaines migrés. [#4027](https://github.com/MTES-MCT/potentiel/issues/4027)
- Amélioration de l'UX sur la page des exports. [#4014](https://github.com/MTES-MCT/potentiel/issues/4014)
