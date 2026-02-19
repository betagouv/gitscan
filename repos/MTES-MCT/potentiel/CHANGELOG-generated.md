## Changelog : potentiel (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées au service Potentiel au cours des 30 derniers jours. Les modifications incluent des corrections de bugs, des améliorations de l'interface utilisateur, l'ajout de nouvelles fonctionnalités comme l'export de données enrichies et la traçabilité des actions, ainsi que des optimisations techniques importantes, notamment la migration vers le format ESM pour une meilleure performance et maintenabilité du code.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter les données des fournisseurs à la candidature (#3856).
- Amélioration de l'export global des projets avec l'ajout des champs AOS (#3970).
- Ajout de filtres sur la page d'export (#3927).
- Affichage des filtres actifs lors de l'export CSV (#3937).
- Ajout de la possibilité d'exporter les projets éliminés (#3918).
- Ajout des acteurs manquants dans la frise de raccordement (#4005).
- Affichage de la demande en cours si modification par un administrateur (#4006).
- Mise à jour de l'autorité compétente abandon (#4002).
- Ajout de la mise en service du raccordement d'un projet (#3984).
- Ajout de la mise en service du raccordement dans les étapes projet (#3994).
- Ajout de la puissance initiale dans le schema (#4011).

### Évolutions techniques
- Migration de nombreux packages vers le format ESM pour améliorer la performance et la compatibilité avec les dernières versions de Node.js (#3905, #3906, #3908, #3909, #3910, #3911, #3966, #3972, #3973, #3978).
- Suppression du package `scheduled-tasks` et réorganisation des scripts pour simplifier la gestion des tâches planifiées (#3975).
- Mise à jour de Typespec (#3941).
- Migration des templates de mail pour les délais, recours et abandon (#3958, #3956, #3951).
- Refactorisation et migration du schéma de référence (DépôtSchéma) (#3981).
- Ajout d'un index sur le champ `identifiantProjet` pour optimiser les requêtes en base de données (#3968).
- Suppression de Redis et des variables legacy (#3955).
- Suppression de la variable `MAINTENANCE_MODE` et documentation associée (#3999, #4000).

### Autres changements
- Amélioration de la traçabilité des actions : transmission de la PTF (#3914), modification du GRD (#3922), suppression du dossier de raccordement (#3925).
- Correction de bugs mineurs liés à l'affichage, la sélection et la modification de données (#3916, #3923, #3926, #3929, #3938, #3947, #3953, #3957, #3988, #3991, #4003, #4016, #4017).
- Amélioration des logs pour les résultats des requêtes Liste (#4010).
- Mise à jour des abonnés (#4001).
- Correction de la technologie des projets PV - Eolien (#3980).
- Ajout de la mise en service à l'export global lauréat (#3997).
- Correction de l'ordre des achèvements et des exports (#3969).
- Ajout de la référence dans l'ordre des achèvements (#3971).
- Correction du format dans les emails fournisseur (#3930).
- Suppression du FF export (#3936).
- Suppression de la génération de fichier détail lors de l'import/correction de candidature (#3934).
- Nettoyage des clés des détails candidatures (#3907).
- Ajout de stats d'utilisation et export (#3939).
- Correction de l'accès admin à la page lister périodes (#3991).
- Correction de l'affichage des filtres appel offres (#3901).
- Correction de l'impossibilité de corriger une demande de délai sans modification (#3929).
- Correction de l'impossibilité de corriger une demande représentant légal sans modification (#3923).
- Correction de l'impossibilité de corriger une demande de délai sans modification (#3938).
- Amélioration de la gestion des permissions pour les modifications de données (#3943, #3944, #3948).
- Ajout de la possibilité de ne pas pouvoir corriger une demande de délai sans modification (#3916).
- Correction de l'affichage des filtres appel offres en multi select (#3901).
- Correction de l'accès admin à la page lister périodes (#3991).
