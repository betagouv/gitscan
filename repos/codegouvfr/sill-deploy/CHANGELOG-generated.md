## Changelog : sill-deploy (30 derniers jours, au 19 septembre 2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de l'administration et de la performance du système. Les administrateurs disposent désormais de nouveaux outils pour configurer l'interface utilisateur plus facilement, tandis que les processus d'importation de données ont été optimisés pour gagner en efficacité, notamment pour les sources externes.

### Évolutions fonctionnelles
- **Administration de l'interface** : Ajout d'un éditeur de configuration de l'interface utilisateur (UI) permettant de modifier les paramètres via l'API d'administration.
- **Optimisation des imports** : Amélioration significative des performances lors des importations massives de données, incluant des optimisations spécifiques pour la source Zenodo [#516](https://github.com/codegouvfr/sill-deploy/issues/516).
- **Traçabilité** : Ajout de la gestion de la date de dernière importation (`lastimport`) sur les sources de données.
- **Documentation API** : Mise à disposition d'une interface Swagger UI dédiée pour documenter l'export public v2.

### Évolutions techniques
- **CI/CD** : Mise en place de nouveaux workflows de déploiement et de configurations permettant la personnalisation du déploiement SILL.
- **Gestion des données** : Migration de la configuration de l'interface utilisateur vers PostgreSQL pour permettre une gestion dynamique et persistante.
- **API & Sécurité** : 
    - Correction de la gestion des préfixes de documentation lors de l'utilisation de proxys.
    - Renforcement de la validation des schémas publics par rapport aux types de logiciels originaux.
    - Correction de la gestion des URLs d'instance et des déclarations exécutables.
- **Tests** : Amélioration de la robustesse de la suite de tests API (vérification des schémas sans serveur HTTP, isolation des données de test et des migrations).

### Autres changements
- Réorganisation et nettoyage des migrations de base de données.
- Corrections diverses liées au build et au nommage du projet.
