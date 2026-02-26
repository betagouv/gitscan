## Changelog : partaj (30 derniers jours)

### Résumé
Cette version apporte des améliorations significatives à la gestion des pièces jointes et des versions de documents, ainsi que des corrections pour assurer la stabilité et la conformité du système. Des mises à jour techniques ont été effectuées pour moderniser l'infrastructure et améliorer les performances.

### Évolutions fonctionnelles
- Ajout d'une modal pour la validation des pièces jointes (#253fa4d).
- Ajout de modales de version (#253fa4d).
- Correction d'un cas particulier concernant les "particuliers" (#7ae0fd4).
- Suppression de la modal de confirmation de division et sauvegarde en cas de problème réseau (#2fe1f57).

### Évolutions techniques
- Mise à jour de la gestion du stockage pour supprimer Whitenoise et utiliser `partaj.core.storage.RelaxedCompressedStaticFilesStorage` (#f3650e9, #751c129, #1ef3958).
- Migration vers `django_cas_ng` pour l'authentification (#8457c3b).
- Mise à jour de la version de Django (#c391ee4).
- Correction de problèmes liés aux UUID dans les tests (#8fafae9).
- Amélioration de la gestion des permissions, remplacement de `has_permission` par `has_object_permission` (#27b8767).
- Rafraîchissement des données depuis la base de données avant l'assignation de la date de création (#f37ddda).

### Autres changements
- Corrections diverses et améliorations suite aux revues de code (#a842265).
- Corrections de tests pour résoudre des problèmes de clés primaires manquantes et de récursion (#ebc732c, #5428b7e).
- Corrections de style avec Black et Pylint (#5e402f1, #2bfdd87).
- Mise à jour du stockage (#a053547, #9508206).
