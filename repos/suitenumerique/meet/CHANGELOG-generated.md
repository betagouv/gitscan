## Changelog : meet (30 derniers jours, au 16 novembre 2026)

### Résumé
Ce mois a été marqué par un effort majeur sur l'accessibilité et la sécurité. L'application est désormais plus inclusive grâce à de nombreuses améliorations pour les utilisateurs de lecteurs d'écran et une meilleure gestion des contrastes. La sécurité a été considérablement renforcée par la mise en place de journaux d'audit détaillés et une protection accrue des données sensibles dans les logs. Enfin, le support de la langue portugaise a été intégré.

### Évolutions fonctionnelles
- **Accessibilité (♿️) :** Amélioration massive de l'expérience pour les utilisateurs de technologies d'assistance (gestion des titres, des listes, des contrastes de couleurs, des focus rings et des étiquettes de boutons).
- **Internationalisation (🌐) :** Ajout du support complet de la langue portugaise, incluant les glyphes nécessaires pour les polices Marianne.
- **Expérience utilisateur (UX) :**
    - Amélioration du carrousel de participants pour mieux mettre en évidence les nouveaux intervenants et les mains levées.
    - Meilleure visibilité des erreurs (notifications en cas de déconnexion inattendue ou d'échec de jonction à une réunion).
    - Information des participants en cas d'interruption d'un enregistrement.
    - Remplacement du chat Crisp par le formulaire de support La Suite.

### Évolutions techniques
- **Sécurité (🔒️) :**
    - Mise en place d'un système d'audit structuré pour tracer les actions sensibles (enregistrements, transcriptions, appels API, modifications via l'administration Django).
    - Protection des données sensibles par l'anonymisation des logs, des erreurs de validation et des métadonnées d'analyse (URLs signées, détails des tâches Celery, logs LLM).
    - Durcissement de l'accès aux salles (utilisation de requêtes POST pour la jonction et restriction des slugs de salles).
    - Correction de plusieurs vulnérabilités (CVE) sur les composants critiques (Python, Nginx, Node, etc.).
- **Stabilité et Performance :**
    - Amélioration de la résilience des connexions grâce à une politique de reconnexion exponentielle (LiveKit).
    - Optimisation des builds Docker pour l'architecture arm64.
    - Introduction d'un pool de connexions optionnel pour PostgreSQL (psycopg).
- **Infrastructure :** Mise à jour majeure des serveurs et clients LiveKit (v1.13.11 / v2.23.0).

### Autres changements
- Mise à jour de la documentation concernant le système d'audit et l'invitation à soutenir le projet.
- Optimisation de la configuration CI/CD (gestion des alertes de sécurité Trivy).
