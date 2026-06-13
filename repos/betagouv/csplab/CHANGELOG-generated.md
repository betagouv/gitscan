## Changelog : csplab (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'ingestion des offres d'emploi, l'ajout de fonctionnalités pour la gestion des utilisateurs et des candidatures, ainsi que sur la mise en place d'une architecture frontend plus robuste. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- **Ingestion :**
    - Agrégation et purge quotidienne des logs API pour une meilleure surveillance et maintenance. [#743](https://github.com/betagouv/csplab/issues/743)
    - Sauvegarde des offres Talensoft archivées avec la date d'archivage. [#697](https://github.com/betagouv/csplab/issues/697)
    - Mise en place d'un endpoint pour la soumission de candidatures. [#729](https://github.com/betagouv/csplab/issues/729)
    - Publication des offres sur le web. [#692](https://github.com/betagouv/csplab/issues/692)
    - Ajout de la gestion des statuts des offres Talensoft. [#627](https://github.com/betagouv/csplab/issues/627)
    - Mise en place d'un mécanisme de logging pour l'ingestion. [#578](https://github.com/betagouv/csplab/issues/578)
- **Utilisateurs :**
    - Création d'utilisateurs avec les profils "agent" et "candidat". [#735](https://github.com/betagouv/csplab/issues/735), [#744](https://github.com/betagouv/csplab/issues/744)
    - Liaison des utilisateurs aux sources de données. [#742](https://github.com/betagouv/csplab/issues/742)
    - Authentification à deux facteurs (2FA) ajoutée pour l'accès à l'administration Django. [#699](https://github.com/betagouv/csplab/issues/699)
    - Authentification par email/mot de passe mise en place. [#639](https://github.com/betagouv/csplab/issues/639)
- **Frontend :**
    - Création d'une base de layout et d'une barre latérale pour l'interface utilisateur. [#701](https://github.com/betagouv/csplab/issues/701)
    - Amélioration de l'affichage des polices dans Storybook et en développement local. [#740](https://github.com/betagouv/csplab/issues/740)
    - Composants de base (badges, avatars, conteneurs de contenu) ajoutés pour le frontend ATS. [#682](https://github.com/betagouv/csplab/issues/682), [#683](https://github.com/betagouv/csplab/issues/683), [#687](https://github.com/betagouv/csplab/issues/687)
    - Affichage des offres d'emploi dans un tiroir (drawer). [#550](https://github.com/betagouv/csplab/issues/550)
    - Gestion des erreurs frontend avec interception et affichage. [#629](https://github.com/betagouv/csplab/issues/629)

### Évolutions techniques
- **Architecture :**
    - Refactorisation de la couche de présentation pour l'identité, regroupant les composants liés aux utilisateurs. [#728](https://github.com/betagouv/csplab/issues/728)
    - Organisation des tests par couche et contexte. [#673](https://github.com/betagouv/csplab/issues/673)
    - Déplacement des objets DDD (Domain-Driven Design) dans une librairie distincte au sein du monorepo. [#663](https://github.com/betagouv/csplab/issues/663)
- **Infrastructure :**
    - Configuration de GitHub Pages pour gérer un nom de domaine personnalisé. [#727](https://github.com/betagouv/csplab/issues/727)
    - Ajout d'un fichier `security.txt` pour la divulgation responsable des vulnérabilités. [#695](https://github.com/betagouv/csplab/issues/695)
    - Mise en place de workflows GitHub Actions pour l'automatisation des tâches (lint, tests, publication). [#718](https://github.com/betagouv/csplab/issues/718), [#719](https://github.com/betagouv/csplab/issues/719), [#658](https://github.com/betagouv/csplab/issues/658)
    - Amélioration de la gestion des variables d'environnement pour Talensoft. [#600](https://github.com/betagouv/csplab/issues/600)
- **Base de données :**
    - Ajout d'une clé étrangère pour `source_id` dans la table `offers`. [#651](https://github.com/betagouv/csplab/issues/651)
    - Création d'une table `Source` pour gérer les sources de données. [#574](https://github.com/betagouv/csplab/issues/574)
    - Backfill de la colonne `source_id` pour les offres existantes. [#642](https://github.com/betagouv/csplab/issues/642)
- **Divers :**
    - Refactorisation des fixtures de test pour l'ingestion. [#726](https://github.com/betagouv/csplab/issues/726)
    - Amélioration de la lisibilité du code et des noms de méthodes. [#568](https://github.com/betagouv/csplab/issues/568)

### Autres changements
- Ajout de scripts pour la souscription et la suppression des webhooks Talensoft. [#721](https://github.com/betagouv/csplab/issues/721)
- Traduction du modèle de PR en français. [#619](https://github.com/betagouv/csplab/issues/619)
- Correction de l'affichage de `!N!` dans les conditions particulières et la description. [#739](https://github.com/betagouv/csplab/issues/739)
- Correction d'un problème de concurrence avec GitHub Pages. [#724](https://github.com/betagouv/csplab/issues/724)
- Correction de bugs liés à la configuration de Storybook. [#749](https://github.com/betagouv/csplab/issues/749), [#649](https://github.com/betagouv/csplab/issues/649)
- Suppression de la déclaration du manager par défaut. [#749](https://github.com/betagouv/csplab/issues/749)
- Ajustement des `entity_id` dans le domaine ingestion. [#746](https://github.com/betagouv/csplab/issues/746)
