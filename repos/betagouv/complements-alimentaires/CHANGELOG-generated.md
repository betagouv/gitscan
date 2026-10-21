## Changelog : complements-alimentaires (30 derniers jours, au 20 octobre 2026)

### Résumé
Les récentes mises à jour renforcent la fiabilité des données saisies, notamment via une meilleure validation des entreprises (SIRET) et l'obligation de certains champs de déclaration. L'administration bénéficie également de nouveaux outils de suivi et de modification pour une gestion plus précise des dossiers.

### Évolutions fonctionnelles
- **Amélioration de la validation des entreprises** : remplacement de l'API INSEE par l'API "Recherche Entreprises", gestion des entreprises fermées et introduction d'un statut spécifique pour les SIRET ne renvoyant aucun résultat.
- **Sécurisation des formulaires de déclaration** : les champs "populations" et "effets" sont désormais obligatoires pour la soumission, avec l'ajout d'indicateurs visuels pour guider l'utilisateur.
- **Évolutions de l'interface d'administration** : possibilité de modifier la date de retrait des déclarations [#3175](https://github.com/betagouv/complements-alimentaires/pull/3175) et ajout de la colonne "date de création" pour les sous-déclarations [#3127](https://github.com/betagouv/complements-alimentaires/pull/3127).

### Évolutions techniques
- **Sécurité** : assainissement des données saisies par les utilisateurs et correction de vulnérabilités potentielles liées aux injections de logs (CodeQL).
- **Observabilité** : amélioration de la gestion des erreurs dans les journaux (logs) afin de remonter des informations utiles sans impacter l'expérience de l'utilisateur.

### Autres changements
- Correction d'un bug concernant les données de rapport Matomo [#3152](https://github.com/betagouv/complements-alimentaires/pull/3152).
- Ajustement de l'interface utilisateur lié aux outils de pré-validation (precommit) [#3126](https://github.com/betagouv/complements-alimentaires/pull/3126).
