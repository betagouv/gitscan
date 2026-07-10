## Changelog : Docurba (30 derniers jours, au 09 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de la gestion des événements et des collectivités, ainsi que par des corrections et des optimisations techniques. L'application a bénéficié de l'ajout de nouvelles fonctionnalités pour le suivi des procédures et l'accès aux données, tout en renforçant la sécurité et la fiabilité du système.

### Évolutions fonctionnelles
- Ajout de l'ID de la procédure dans l'onglet Procédures et Validations pour une meilleure identification.
- Amélioration de la détection des événements de lancement et de l'application de la loi Huwart à toutes les procédures dans l'interface Nuxt.
- Ajout de la date des procédures sur les pages procédures et collectivités dans l'interface Nuxt.
- Possibilité de rechercher des événements de prescription plus précisément dans l'interface Nuxt.
- Historisation de toutes les modifications d'événements, permettant un suivi précis des changements.
- Ajout de la possibilité de lister les procédures dont le périmètre inclut une commune dans l'administration Django.
- Ajout de la gestion des catégories PAC et d'une nouvelle catégorie d'événements dans l'API Django.
- Amélioration de l'affichage des événements et de la gestion des dates associées.
- Ajout de la possibilité de modifier les événements dans l'administration Django.
- Ajout de la recherche d'utilisateurs par email dans l'administration Django.
- Ajout de la possibilité de modifier le mot de passe des utilisateurs dans l'administration Django.

### Évolutions techniques
- Mise à jour de plusieurs dépendances : Django, Django Debug Toolbar, Django Environ, Pytest, Ruff, Cryptography, PyJWT, Supabase.
- Refonte de la gestion des types d'événements, avec l'ajout de nouveaux types et une configuration améliorée.
- Amélioration de l'API interne Django pour exposer des informations supplémentaires sur les collectivités (SIREN, groupes, membres).
- Suppression de composants et d'assets inutilisés dans l'interface Nuxt, allégeant le code et améliorant les performances.
- Suppression de vues publiques obsolètes et de commandes de gestion inutilisées.
- Amélioration de l'intégration de pg_history pour un suivi plus précis des modifications de données.
- Correction de bugs et d'anomalies dans l'interface Nuxt et l'API Django.
- Amélioration de la configuration des templates.
- Restriction de l'accès aux tables de versements aux utilisateurs vérifiés pour renforcer la sécurité.
- Ajout de tests unitaires et d'intégration pour améliorer la qualité du code et la couverture des tests.
- Utilisation de Syrupy pour les tests de l'API interne Django.
- Mise à jour de la configuration de l'environnement Django.

### Autres changements
- Ajout d'une variable d'environnement `DEBUG_SQL` pour faciliter le débogage des requêtes SQL.
- Suppression temporaire du fichier `.gitignore` puis restauration pour corriger un problème de configuration.
- Documentation mise à jour pour refléter les changements apportés.
- Correction de petites anomalies et améliorations de la lisibilité du code.
