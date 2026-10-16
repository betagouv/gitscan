## Changelog : complements-alimentaires (30 derniers jours, au 15/10/2026)

### Résumé
Les récentes évolutions se concentrent sur la fiabilité de l'identification des entreprises et la qualité des données collectées. Le système de vérification des SIRET a été modernisé pour mieux gérer les entreprises fermées ou introuvables, et certains champs de saisie sont désormais obligatoires pour garantir la complétude des dossiers. Enfin, la précision des exports de données publiques a été renforcée.

### Évolutions fonctionnelles
- **Amélioration de l'identification des entreprises** : passage à l'API "Recherche Entreprises", gestion des cas d'entreprises fermées et introduction de nouveaux statuts pour les SIRET ne retournant aucun résultat.
- **Validation du SIRET** : ajout d'une vérification locale du numéro SIRET avant l'appel aux services externes [#3153](https://github.com/betagouv/complements-alimentaires/issues/3153).
- **Optimisation des formulaires** : les champs "populations" et "effets" sont désormais obligatoires pour la soumission, avec une indication visuelle pour l'utilisateur.
- **Qualité des données** : ajout de la colonne "date de création" pour les sous-domaines et correction du vocabulaire utilisé dans les exports Open Data.

### Évolutions techniques
- **Sécurité** : renforcement de la protection contre les injections de logs et assainissement des données saisies par les utilisateurs.
- **Fiabilité et corrections** : 
    - Résolution de bugs sur la gestion des champs multi-valeurs [#3125](https://github.com/betagouv/complements-alimentaires/issues/3125) et sur les données de rapport Matomo [#3152](https://github.com/betagouv/complements-alimentaires/issues/3152).
    - Amélioration de la gestion des erreurs pour permettre une remontée dans les logs sans perturber l'expérience de l'utilisateur.
- **Traitement de données (ETL)** : mises à jour des processus de traitement concernant les décisions et les délais de visa [#3105](https://github.com/betagouv/complements-alimentaires/issues/3105).

### Autres changements
- Correction de l'interface de l'outil de pré-commit [#3126](https://github.com/betagouv/complements-alimentaires/issues/3126).
