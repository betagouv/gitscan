## Changelog : Docurba (30 derniers jours, au 07/10/2026)

### Résumé
Ce mois-ci, Docurba a bénéficié d'améliorations significatives concernant la gestion des utilisateurs, notamment via un nouveau système de vérification par email et une gestion plus fluide des inscriptions. L'interface d'administration a été enrichie pour offrir un meilleur contrôle sur les procédures et le partage de projets. Parallèlement, un important travail de nettoyage et de restructuration technique a été mené pour renforcer la sécurité de l'API et optimiser les performances globales de la plateforme.

### Évolutions fonctionnelles
- **Gestion des utilisateurs** : Réactivation de la création de comptes utilisateurs avec un nouveau flux de vérification par email et des messages d'erreur plus explicites lors de la connexion.
- **Administration renforcée** : 
    - Ajout de filtres par type de procédure dans l'interface d'administration Django.
    - Amélioration de la gestion du partage de projets (affichage et suppression facilités).
    - Possibilité de vérifier les profils directement depuis l'administration.
- **Suivi et traçabilité** : 
    - Meilleure visibilité sur l'historique des modifications (affichage de l'auteur de la dernière édition et du créateur des sections dans l'interface Nuxt).
    - Affichage des dates d'approbation des procédures parentes dans les formulaires de procédures secondaires.
- **Données métier** : Ajout d'un champ "complément de nom" pour les procédures.
- **Contrôles de saisie** : Mise en place de règles de blocage pour la création de procédures dans certains contextes de communes ou d'EPCI.

### Évolutions techniques
- **Architecture et API** : 
    - Migration de plusieurs vues vers Django Rest Framework (DRF) et sécurisation des API par défaut.
    - Nettoyage important de l'API avec la suppression de nombreux points de terminaison (endpoints) inutilisés.
    - Réorganisation de la structure des dossiers du projet (regroupement des applications API).
- **Intégrations tierces** : 
    - Implémentation d'un client Pipedrive pour automatiser la vérification des utilisateurs.
    - Refonte complète du système d'envoi d'emails via l'intégration de Sendgrid.
- **Sécurité et Performance** : 
    - Renforcement du *rate limiting* via Nginx.
    - Sécurisation des sessions utilisateurs (suppression des sessions à durée infinie) et ajustement des permissions de base de données (RLS).
- **Maintenance et Refactoring** : 
    - Transition d'une logique de suppression vers une logique d'archivage pour les événements afin de préserver l'intégrité des données.
    - Suppression des résidus de Nuxt3 et nettoyage du code mort.

### Autres changements
- **Sécurité** : Ajout d'un fichier `security.txt` pour faciliter le signalement de vulnérabilités.
- **Infrastructure** : Mise à jour du plan Scalingo.
