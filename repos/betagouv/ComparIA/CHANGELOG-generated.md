## Changelog : ComparIA (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, ComparIA a connu une refonte majeure de son infrastructure de base de données et de son architecture backend, visant à améliorer la robustesse, la scalabilité et la maintenance du projet.  De nombreuses améliorations ont été apportées à la gestion des données, notamment la migration des données existantes et l'ajout de nouvelles fonctionnalités pour l'analyse et la validation des données. L'interface utilisateur a également été améliorée avec de nouvelles animations et des corrections de bugs.

### Évolutions fonctionnelles
- Ajout de nouveaux modèles de langage : Gemini 3.5 Flash et Grok 4.3 sont désormais disponibles sur la plateforme. [#480](https://github.com/betagouv/ComparIA/pull/480)
- Amélioration de la détection et du blocage des tentatives de "jailbreak" et de "roleplay" dans les interactions avec les modèles de langage. [#481](https://github.com/betagouv/ComparIA/pull/481)
- Ajout de traductions en danois pour certains modèles et descriptions. [#478](https://github.com/betagouv/ComparIA/pull/478)
- Amélioration de l'expérience utilisateur avec de nouvelles animations pour les votes et les révélations.
- Ajout d'un indicateur visuel pour confirmer la sélection d'un choix lors du vote.
- Amélioration de la réactivité de l'interface utilisateur sur mobile.
- Ajout de la possibilité de soumettre des votes via un bouton dédié.
- Mise à jour des traductions italiennes via Weblate.

### Évolutions techniques
- Refonte complète de la base de données : migration vers de nouvelles tables et modèles pour une meilleure organisation et performance.
- Utilisation de SQLModel pour la définition des modèles de données.
- Ajout d'un système de gestion de migrations de base de données avec Alembic.
- Implémentation d'un système de streaming de données plus efficace pour les comparaisons.
- Amélioration de la gestion des erreurs et de la journalisation.
- Refactorisation du code backend pour une meilleure modularité et maintenabilité.
- Ajout de tests unitaires et d'intégration.
- Mise à jour des dépendances (litellm, typescript).
- Simplification de la configuration de l'environnement de développement et de production.
- Utilisation de UUID pour les identifiants des enregistrements dans la base de données.
- Ajout d'un gestionnaire de contexte pour les sessions de base de données.
- Amélioration de la validation des données.

### Autres changements
- Documentation mise à jour pour refléter les changements de l'infrastructure.
- Nettoyage du code et suppression de code obsolète.
- Mise à jour des fichiers de configuration.
- Correction de bugs mineurs.
- Suppression de modèles de langage obsolètes.
- Ajout d'un script pour générer des jeux de données.
- Amélioration de la gestion des traductions via Weblate.
