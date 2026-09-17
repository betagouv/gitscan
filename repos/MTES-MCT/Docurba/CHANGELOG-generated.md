## Changelog : Docurba (30 derniers jours, au 15 septembre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur le renforcement de la sécurité des accès et la fiabilisation des communications. Les utilisateurs bénéficient d'un système de gestion des mots de passe plus robuste et conforme aux recommandations de la CNIL, ainsi que d'un service d'envoi d'emails plus stable. En parallèle, l'architecture technique a été restructurée pour mieux isoler les données sensibles et optimiser les performances de l'infrastructure.

### Évolutions fonctionnelles
- **Gestion des mots de passe** : Mise en place d'un cycle complet de sécurité incluant la validation des mots de passe (normes CNIL), la réinitialisation globale, et la gestion des mises à jour obligatoires pour les utilisateurs.
- **Expérience d'authentification** : Amélioration des messages d'erreur lors de la connexion et de l'inscription pour plus de clarté, et meilleure gestion des cas de doublons d'emails.
- **Communications** : Intégration de Sendgrid pour garantir la délivrabilité des emails et personnalisation des messages selon l'environnement utilisé.

### Évolutions techniques
- **Sécurité et protection des données** : 
    - Renforcement des politiques de sécurité de la base de données via l'activation et la correction des permissions RLS (Row Level Security).
    - Ajout d'un fichier `security.txt` pour faciliter le signalement de vulnérabilités.
    - Isolation des API : Restructuration de l'architecture Django pour séparer strictement les API publiques des API internes et migration vers Django Rest Framework (DRF).
- **Infrastructure et CI/CD** :
    - Optimisation des environnements de test et de revue (mise à jour des configurations Supabase et Scalingo).
    - Amélioration de la configuration Nginx pour augmenter les limites de débit (rate limiting).
    - Mise à jour des actions GitHub pour une meilleure intégration de Supabase.
- **Optimisation des performances** : Refonte du script de sauvegarde pour réduire la consommation de mémoire vive (RAM) et d'espace disque.

### Autres changements
- **Outils de développement** : Ajout de commandes Makefile pour accélérer les tests et mise à jour des règles de formatage du code (Ruff).
- **Maintenance** : Nettoyage de fonctions inutilisées et harmonisation des configurations de l'application.
