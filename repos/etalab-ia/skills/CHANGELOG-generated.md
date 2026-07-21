## Changelog : skills (30 derniers jours, au 16 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la synchronisation des données avec datagouv, la correction de problèmes liés au workflow de synchronisation, et des refactorings pour améliorer la gestion de la sécurité et du développement.

### Évolutions fonctionnelles
- Amélioration de la gestion des références et ajout de validations pour la fonctionnalité de sécurité du développement. L'exploitabilité est également prise en compte et la sortie est désormais au format JSON. [#27](https://github.com/etalab-ia/skills/pull/27)
- Renommage de la fonctionnalité "sécurité-anssi" en "sécurité-developpement" pour plus de clarté. [#25](https://github.com/etalab-ia/skills/pull/25)

### Évolutions techniques
- Correction du workflow de synchronisation avec datagouv : suppression des pull requests vides et réparation du corps des pull requests. [#31](https://github.com/etalab-ia/skills/pull/31)
- Correction de la documentation concernant l'horaire du workflow de synchronisation.
- Ajout d'un fichier `.gitignore` pour exclure les fichiers temporaires et spécifiques à l'environnement de développement (.DS_Store, .claude/). [#30](https://github.com/etalab-ia/skills/pull/30)

### Autres changements
- Synchronisation des changements en provenance de datagouv. [#29](https://github.com/etalab-ia/skills/pull/29)
- Synchronisation automatique des changements upstream via le bot github-actions.
