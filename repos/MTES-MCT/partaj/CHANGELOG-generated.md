## Changelog : partaj (30 derniers jours)

### Résumé
Les dernières mises à jour de Partaj se concentrent sur l'amélioration de la gestion des cas, notamment la correction de problèmes spécifiques liés aux cas particuliers et à l'intégration avec TIEPS. Des optimisations ont également été apportées au stockage des fichiers et à la configuration de l'application, ainsi que des corrections de tests et des mises à jour de dépendances.

### Évolutions fonctionnelles
- Correction d'un problème spécifique aux cas particuliers. (#7ae0fd4)
- Intégration avec TIEPS. (#9508206)

### Évolutions techniques
- Mise à jour de la gestion du stockage des fichiers pour supprimer Whitenoise et utiliser `partaj.core.storage.RelaxedCompressedStaticFilesStorage`. (#f3650e9, #751c129, #1ef3958)
- Migration vers `django_cas_ng`. (#8457c3b)
- Mise à jour de la version de Django. (#c391ee4)
- Modification de la méthode `has_permission` en `has_object_permission`. (#27b8767)
- Corrections de tests pour résoudre des problèmes liés aux clés primaires manquantes, aux UUID invalides et aux problèmes récursifs. (#ebc732c, #8fafae9, #5428b7e)

### Autres changements
- Corrections de style avec Black et Pylint. (#5e402f1, #2bfdd87)
- Travaux en cours (WIP) pour diverses améliorations. (#da6f3e2)
