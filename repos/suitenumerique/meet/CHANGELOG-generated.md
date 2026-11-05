## Changelog : meet (30 derniers jours, au 03/11/2026)

### Résumé
Ce mois-ci, Meet a franchi une étape importante en renforçant sa sécurité et sa traçabilité grâce à l'introduction d'un système d'audit complet. Les améliorations se sont également concentrées sur la fiabilité des appels vidéo (meilleure gestion des reconnexions) et sur l'expérience utilisateur, notamment via de nouvelles options pour les enregistrements et une meilleure accessibilité.

### Évolutions fonctionnelles
- **Enregistrements** : 
    - Possibilité pour les utilisateurs de choisir l'encodage de leurs enregistrements.
    - Envoi automatique de notifications par email à la fin d'un enregistrement.
    - Information des participants en cas d'interruption d'un enregistrement en cours.
    - Autorisation pour tout utilisateur authentifié de lancer un enregistrement.
- **Expérience utilisateur et Accessibilité** :
    - Amélioration de la gestion des déconnexions imprévues avec l'affichage d'une page dédiée.
    - Ajout d'annonces vocales lors de la coupure du micro via les raccourcis clavier.
    - Amélioration de la visibilité des éléments de menu (outline de focus) et des indicateurs de micro.
    - Ajout d'un test de haut-parleur automatique si aucun périphérique de sortie n'est sélectionné.
- **Confidentialité et Accès** :
    - Protection des salles de réunion contre l'indexation par les moteurs de recherche et l'IA.
    - Support de l'authentification via les fragments d'URL et intégration facilitée via iframe (échange de jetons).
    - Remplacement du chat Crisp par le formulaire de support La Suite.
- **Gestion des données** : Mise en place de la suppression logique ("soft delete") des salles, avec un nettoyage automatique après une période de rétention.

### Évolutions techniques
- **Sécurité et Audit** :
    - Implémentation d'un système d'audit structuré pour tracer les actions sensibles (création d'utilisateurs, échanges de jetons, opérations sur les salles, enregistrements et résumés).
    - Correction de nombreuses vulnérabilités de sécurité (CVE) sur plusieurs composants : Nginx, Django Rest Framework, Pillow, Brotli, Aiohttp, Libx11 et Tiff.
    - Sécurisation des secrets d'application via hachage SHA-256 et restriction de l'édition des identifiants clients dans l'administration.
- **Fiabilité et Performance** :
    - Amélioration de la robustesse des appels avec une politique de reconnexion par "backoff exponentiel" et une meilleure gestion des timeouts LiveKit.
    - Optimisation des performances via l'ajout d'un pool de connexions PostgreSQL (psycopg) et d'index pour les recherches d'utilisateurs par email.
    - Mise à jour majeure de l'infrastructure LiveKit (serveur et egress).
- **Infrastructure et CI/CD** :
    - Support natif de l'architecture arm64 pour la construction des assets frontend dans Docker.
    - Mise à jour des outils de scan de sécurité (Trivy) et des charts Helm.
    - Optimisation des processus de build et de déploiement.

### Autres changements
- **Documentation** : Mise à jour de la documentation concernant le nouveau système d'audit et les processus de migration.
- **Maintenance** : Nettoyage des logs de console et mise à jour de diverses dépendances de développement.
