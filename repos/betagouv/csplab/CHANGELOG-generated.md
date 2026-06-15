## Changelog : csplab (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'ingestion et de la gestion des offres d'emploi, ainsi que sur la mise en place des fondations pour l'interface utilisateur et l'authentification des utilisateurs. Des améliorations ont également été apportées à l'infrastructure et aux outils de développement.

### Évolutions fonctionnelles
- **Ingestion :**
    - Agrégation et purge quotidienne des logs de l'API pour une meilleure gestion et performance.
    - Sauvegarde des offres Talensoft archivées avec la date d'archivage.
    - Implémentation de l'ingestion d'offres via des webhooks Talensoft.
    - Ajout d'un endpoint pour lister les sources d'offres.
    - Possibilité de mettre à jour les offres via l'API avec authentification par token.
- **Utilisateurs :**
    - Création d'utilisateurs avec les profils "agent" et "candidat".
    - Mise en place de l'authentification à deux facteurs (2FA) pour l'accès à l'administration Django.
    - Authentification par email et mot de passe implémentée.
- **Candidatures :**
    - Soumission de candidatures implémentée.
- **Interface utilisateur :**
    - Création d'une base de layout et d'une barre latérale pour l'interface utilisateur.
    - Composants de base (badges, avatars, conteneurs de contenu) ajoutés pour l'interface utilisateur.
    - Gestion des erreurs frontend implémentée.
    - Mise en place d'une structure de tests pour le frontend.
- **Recherche :**
    - Ajout de la vectorisation pour les métiers, améliorant potentiellement la recherche sémantique.

### Évolutions techniques
- **Infrastructure :**
    - Configuration de GitHub Pages pour gérer un nom de domaine personnalisé.
    - Amélioration de la gestion des workflows GitHub Actions (auto-assignation, exécution des tests, etc.).
    - Mise à jour des dépendances pour plusieurs composants (web, ingestion, ocr, notebook).
    - Refactorisation de l'architecture pour séparer les couches de présentation et de domaine.
    - Utilisation de composants Storybook pour le développement de l'interface utilisateur.
    - Migration vers un modèle d'utilisateur personnalisé dans Django.
    - Ajout d'un système de logging plus robuste.
- **Code :**
    - Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
    - Ajout de tests unitaires et d'intégration.
    - Amélioration de la gestion des erreurs et des exceptions.
    - Standardisation des noms de méthodes.
    - Ajout de documentation pour certains composants.

### Autres changements
- Ajout d'un fichier `security.txt` pour la divulgation responsable des vulnérabilités.
- Ajout d'un script pour s'abonner et se désabonner aux webhooks Talensoft.
- Traduction du template de PR en français.
- Organisation des tests web par couche et contexte.
- Ajout d'un fichier `CHANGELOG.md` pour la version 0.1.10 et 0.1.9.
- Ajout d'un système de gestion des sources d'offres.
- Ajout de la gestion des organismes pour les recruteurs.
- Ajout d'un endpoint pour lister les métiers.
- Correction de bugs divers liés à l'affichage, aux migrations de base de données et à la configuration de l'environnement.
