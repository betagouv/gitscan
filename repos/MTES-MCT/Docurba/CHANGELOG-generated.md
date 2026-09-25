## Changelog : Docurba (30 derniers jours, au 24 septembre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur le renforcement de la sécurité et la fiabilisation de la gestion des utilisateurs. La plateforme a bénéficié de nouvelles mesures de protection des données (mots de passe, accès API) et d'une meilleure maîtrise administrative, notamment sur les inscriptions et les communications par email.

### Évolutions fonctionnelles
- **Gestion des accès et sécurité** : 
    - Mise en place d'un nouveau processus de réinitialisation de mot de passe avec validation renforcée selon les recommandations de la CNIL.
    - Amélioration de la gestion des sessions pour éviter les durées de connexion infinies.
    - Amélioration de l'expérience utilisateur via des messages d'erreur plus explicites lors de la connexion et de l'inscription.
- **Administration** : 
    - Possibilité pour les administrateurs de désactiver les inscriptions d'utilisateurs.
    - Amélioration de la visibilité des profils et du suivi des changements de mots de passe dans l'interface d'administration.
- **Règles métier** : 
    - Ajout de restrictions sur la création de procédures pour empêcher les erreurs de saisie liées au contexte territorial (communes et EPCI).

### Évolutions techniques
- **Sécurité et API** : 
    - Migration des API vers Django Rest Framework (DRF) et application du principe de "privé par défaut".
    - Renforcement de la sécurité de la base de données via l'optimisation des politiques de sécurité (RLS).
    - Réorganisation structurelle du backend pour mieux isoler les API publiques des API internes.
- **Système d'emailing** : 
    - Migration de la logique d'envoi d'emails du frontend (Nuxt) vers le backend (Django) avec intégration de Sendgrid pour une meilleure fiabilité.
- **Optimisation et Maintenance** : 
    - Nettoyage important du code avec la suppression de nombreux points de terminaison (endpoints) API et de fonctions inutilisés.
    - Optimisation des performances via une configuration ajustée de Nginx.
- **Infrastructure et CI/CD** : 
    - Mise à jour des outils de déploiement et de gestion de base de données (Supabase, Scalingo, GitHub Actions).

### Autres changements
- **Sécurité** : Ajout d'un fichier `security.txt` pour faciliter le signalement de vulnérabilités par les chercheurs en sécurité.
