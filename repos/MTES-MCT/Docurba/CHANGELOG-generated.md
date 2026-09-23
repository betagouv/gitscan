## Changelog : Docurba (30 derniers jours, au 22 septembre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur le renforcement de la sécurité et de la conformité, notamment via une gestion plus stricte des mots de passe et des accès. Des contrôles supplémentaires ont été ajoutés pour sécuriser la création de procédures administratives, et l'infrastructure a été optimisée pour une meilleure gestion des communications (emails) et des performances.

### Évolutions fonctionnelles
- **Gestion des mots de passe** : Mise en place d'un système de réinitialisation globale, validation des mots de passe selon les recommandations de la CNIL et nouveau processus de mise à jour avec confirmation par email.
- **Contrôle des procédures** : Blocage de la création de procédures en l'absence de commune ou dans certains cas spécifiques de communes uniques sur un EPCI.
- **Administration et utilisateurs** : 
    - Possibilité de désactiver les inscriptions d'utilisateurs.
    - Amélioration de l'interface d'administration Django avec l'affichage des dates de création pour les profils et les procédures.
    - Amélioration de la clarté des messages d'erreur lors de la connexion.

### Évolutions techniques
- **Sécurité et Authentification** : 
    - Renforcement des politiques d'accès (RLS) et sécurisation des APIs par défaut.
    - Gestion de la durée des sessions utilisateurs pour éviter les sessions infinies.
    - Amélioration de la gestion des erreurs d'inscription (emails existants, validation des champs).
- **Architecture et API** : 
    - Migration de l'envoi d'emails vers Sendgrid, désormais centralisé côté Django.
    - Réorganisation des applications API et migration vers Django Rest Framework (DRF).
    - Nettoyage du code : suppression de fonctions, de dépendances et d'endpoints API inutilisés.
- **Infrastructure et DevOps** : 
    - Optimisation des performances via Nginx (augmentation du rate limit).
    - Mise à jour et harmonisation des configurations Supabase.
    - Amélioration des workflows CI/CD (mise à jour de la CLI Supabase dans GitHub Actions).

### Autres changements
- **Sécurité** : Ajout d'un fichier `security.txt` pour faciliter le signalement de vulnérabilités par les chercheurs.
- **Maintenance** : Ajustements de la configuration de l'outil de linting Ruff et optimisation de la vitesse de mise à jour des snapshots via le Makefile.
