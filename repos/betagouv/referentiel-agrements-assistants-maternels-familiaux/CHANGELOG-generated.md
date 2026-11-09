## Changelog : referentiel-agrements-assistants-maternels-familiaux (30 derniers jours, au 06 novembre 2026)

### Résumé
Cette période a été marquée par un renforcement significatif de la sécurité et de la précision des données. Le système permet désormais une meilleure distinction entre les agréments d'assistants maternels et familiaux, tout en intégrant des contrôles d'identité plus robustes et une traçabilité accrue des consultations.

### Évolutions fonctionnelles
- **Sécurisation et identité** : Mise en place de la vérification de l'identité via le RNIPP et renforcement des contrôles d'autorisation sur les routes de l'API.
- **Gestion des agréments** : 
    - Distinction claire et séparation des flux pour les agréments d'assistants maternels et familiaux.
    - Ajout de fonctionnalités de recherche dans les agréments.
    - Intégration du département de délivrance dans l'historique des assistants familiaux.
- **Précision des données** : Amélioration de la gestion des dates de délivrance avec la prise en compte des fuseaux horaires et l'utilisation de formats timestamp.
- **Traçabilité** : Implémentation d'un suivi détaillé des consultations de l'historique (incluant la date de consultation).
- **Organisation** : Liaison des utilisateurs à un département spécifique.

### Évolutions techniques
- **Infrastructure et sécurité** : 
    - Mise à jour des environnements vers Node.js 26 et PostgreSQL 18.
    - Correction de vulnérabilités de sécurité (CVE).
- **Optimisation de la CI/CD** : 
    - Amélioration des processus d'automatisation (configuration de la *merge queue*, automerge pour les dépendances, limitation des permissions de la CI).
    - Optimisation de l'exécution des tests (tests de bout-en-bout exécutés en série).
- **Architecture et code** : 
    - Refactorisation pour séparer les dépôts de données (agréments et traces).
    - Alignement des mocks (Pajemploi) sur l'implémentation réelle.
    - Mise à jour de la syntaxe Knex pour respecter les recommandations.

### Autres changements
- **Documentation** : 
    - Amélioration de la documentation Swagger (masquage des modèles).
    - Ajout de documentation sur la création du schéma de base de données et la structure des tests.
    - Clarification des standards de développement (langue, nommage des branches, tests manuels).
