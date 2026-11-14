## Changelog : meet (30 derniers jours, au 14 novembre 2026)

### Résumé
Ce mois-ci, les développements se sont concentrés sur trois axes majeurs : le renforcement massif de la sécurité et de la confidentialité des données, l'amélioration de l'accessibilité pour tous les utilisateurs, et l'extension du support linguistique avec l'ajout du portugais. L'expérience de réunion est également devenue plus robuste grâce à une meilleure gestion des erreurs de connexion et des interruptions.

### Évolutions fonctionnelles
- **Accessibilité (♿️) :** Amélioration globale de l'interface pour les lecteurs d'écran, optimisation des contrastes de couleurs, ajout de la navigation au clavier (touche Échap) et meilleure signalisation des changements d'état (micro, paramètres).
- **Internationalisation (🌐) :** Ajout complet du support de la langue portugaise (interface et polices de caractères).
- **Expérience utilisateur (UX) :** 
    - Optimisation du carrousel des participants (mise en avant des nouveaux intervenants et des mains levées).
    - Amélioration de la gestion des erreurs (affichage des erreurs de connexion au lieu d'une attente infinie, page dédiée en cas de déconnexion inattendue).
    - Notifications en cas d'interruption d'un enregistrement.
    - Remplacement du chat Crisp par le formulaire de support La Suite.
- **Nouvelles capacités :** Autorisation pour tout utilisateur authentifié de lancer un enregistrement.

### Évolutions techniques
- **Sécurité et Confidentialité (🔒️) :** 
    - Mise en place d'un système d'audit complet et structuré (logs pour les enregistrements, les résumés, les opérations API et les actions via l'administration Django).
    - Durcissement de la protection des données sensibles (redaction des URLs signées dans les logs, protection des champs de modèles et nettoyage des erreurs de validation).
    - Sécurisation de l'accès aux salles et des échanges de jetons.
- **Infrastructure et DevOps (⚡️/🔒️) :** 
    - Optimisation des images Docker (support natif pour arm64, passage à une image Nginx non-privilégiée).
    - Mise à jour de l'infrastructure LiveKit (serveur et egress).
    - Correction de nombreuses vulnérabilités (CVE) sur les dépendances critiques (Python, Node, Nginx, Brotli, Pillow, etc.).
- **Fiabilité et Performance :** 
    - Amélioration de la gestion des timeouts et des erreurs lors des appels à l'API LiveKit.
    - Implémentation d'une politique de reconnexion exponentielle pour plus de stabilité.
    - Ajout d'un pool de connexions psycopg optionnel pour le backend.

### Autres changements
- **Documentation (📝) :** Documentation du nouveau système d'audit et incitation à soutenir le projet sur GitHub.
- **Releases :** Publication des versions 1.37.0, 1.36.3, 1.36.2 et 1.35.1.
