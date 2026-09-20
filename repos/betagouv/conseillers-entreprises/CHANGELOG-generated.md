## Changelog : conseillers-entreprises (30 derniers jours, au 15 septembre 2026)

### Résumé
Ce mois-ci, les développements ont porté sur l'amélioration de l'interface d'administration (suivi d'activité), l'optimisation des performances (mise en cache et statistiques) et le renforcement de la gestion des données (anonymisation et pseudonymisation).

### Évolutions fonctionnelles
- **Administration** : Ajout du suivi de l'activité des utilisateurs (date de dernière connexion) dans l'interface d'administration [#4682](https://github.com/betagouv/conseillers-entreprises/pull/4682).
- **Gestion des utilisateurs** : Amélioration de la fonction de duplication d'experts, incluant la reprise des zones territoriales et la possibilité de réattribuer des dossiers (matches) en cours [#4651](https://github.com/betagouv/conseillers-entreprises/pull/4651).
- **Exports** : Enrichissement des exports Excel (XLSX) avec l'ajout de données sur les taux de réponse à cinq jours [#4666](https://github.com/betagouv/conseillers-entreprises/pull/4666).
- **Interface (Landing Page)** : Refonte et personnalisation des éléments de mise en avant (emphasis items) sur la page d'accueil [#4687](https://github.com/betagouv/conseillers-entreprises/pull/4687).

### Évolutions techniques
- **Performance** : Optimisation des temps de réponse via l'implémentation du cache de fragments (landings, footer) et l'optimisation de requêtes SQL complexes [#4657](https://github.com/betagouv/conseillers-entreprises/pull/4657).
- **Données & Sécurité** : Accélération du processus d'anonymisation des données avec ajout d'une barre de progression [#4655](https://github.com/betagouv/conseillers-entreprises/pull/4655) et mise en place de la pseudonymisation des données pour les environnements de développement [#4656](https://github.com/betagouv/conseillers-entreprises/pull/4656).
- **Statistiques** : Sécurisation des calculs statistiques (protection contre les injections SQL via les wildcards) et refactorisation du moteur de statistiques d'acquisition pour plus d'efficacité [#4667](https://github.com/betagouv/conseillers-entreprises/pull/4667).
- **Infrastructure** : Activation du stockage de fichiers (`file_store`) en production [#4675](https://github.com/betagouv/conseillers-entreprises/pull/4675).

### Autres changements
- **Nettoyage** : Suppression de code mort et de fonctionnalités obsolètes (SoftDeletable, intelligent retention) [#4652](https://github.com/betagouv/conseillers-entreprises/pull/4652).
- **Migration** : Conversion des templates HAML vers ERB pour uniformiser le projet [#4673](https://github.com/betagouv/conseillers-entreprises/pull/4673).
