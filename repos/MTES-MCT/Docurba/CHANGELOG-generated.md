## Changelog : Docurba (30 derniers jours, au 24 septembre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur le renforcement de la sécurité de la plateforme et la fiabilisation des communications. Une refonte importante de la gestion des mots de passe et des processus d'inscription a été réalisée pour répondre aux standards de sécurité. Parallèlement, une phase de nettoyage approfondie a permis de supprimer des fonctionnalités obsolètes et de restructurer l'architecture des API pour gagner en robustesse et en clarté.

### Évolutions fonctionnelles
- **Gestion des accès et sécurité :**
  - Amélioration complète du cycle de vie des mots de passe (réinitialisation, mise à jour et validation renforcée selon les recommandations de la CNIL).
  - Mise en place de messages d'erreur de connexion plus génériques pour éviter de divulguer des informations sensibles.
  - Possibilité pour l'administrateur de désactiver l'inscription libre des nouveaux utilisateurs.
- **Gestion métier :**
  - Ajout de règles de validation pour la création de procédures : blocage automatique si aucune commune n'est sélectionnée ou si une seule commune est présente sur un EPCI.

### Évolutions techniques
- **Sécurité et conformité :**
  - Implémentation d'un fichier `security.txt` pour faciliter le signalement de vulnérabilités par les chercheurs.
  - Renforcement des politiques de sécurité de la base de données (RLS) et gestion plus stricte des sessions utilisateurs.
  - Migration de la logique d'envoi d'emails vers le backend via l'intégration de Sendgrid pour une meilleure fiabilité.
- **Architecture API et Backend :**
  - Restructuration majeure des API : migration vers Django Rest Framework (DRF) et application du principe de "privé par défaut".
  - Nettoyage massif des points d'accès (endpoints) inutilisés sur le frontend (Nuxt).
  - Réorganisation de l'arborescence du projet Django pour une meilleure séparation entre les API publiques et internes.
- **Infrastructure et DevOps :**
  - Optimisation de la configuration Nginx (gestion des taux de requêtes).
  - Mise à jour des outils de CI/CD (Supabase CLI) et de l'infrastructure d'hébergement (Scalingo).
  - Nettoyage du code mort et des fonctions non utilisées dans l'application Nuxt.

### Autres changements
- **Administration :**
  - Amélioration de l'interface d'administration Django avec l'ajout de colonnes de suivi (dates de création) pour les profils et les procédures.
- **Développement :**
  - Optimisation du Makefile pour accélérer la mise à jour des snapshots de tests.
