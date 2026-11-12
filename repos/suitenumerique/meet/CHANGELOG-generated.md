## Changelog : meet (30 derniers jours, au 07 novembre 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape majeure en matière de sécurité et de confidentialité. Une refonte complète du système de journalisation d'audit a été déployée, accompagnée de mesures strictes pour protéger les données sensibles dans les logs et les outils de diagnostic. Parallèlement, l'expérience utilisateur a été fluidifiée grâce à une meilleure gestion des erreurs de connexion et des améliorations notables en matière d'accessibilité.

### Évolutions fonctionnelles
- **Expérience utilisateur et fiabilité** :
    - Amélioration de la clarté lors des erreurs de connexion (affichage explicite au lieu d'une attente silencieuse dans le lobby).
    - Mise en place d'une politique de reconnexion automatique plus intelligente (exponential backoff) pour stabiliser les sessions.
    - Affichage d'une page dédiée en cas de déconnexion inattendue.
    - Notification des participants lorsqu'un enregistrement est interrompu.
- **Accessibilité** :
    - Possibilité de fermer la boîte de dialogue d'invitation avec la touche `Échap`.
    - Annonces sonores/visuelles lors de la coupure du micro via des raccourcis.
- **Gestion des réunions et confidentialité** :
    - Introduction de la suppression logique (*soft delete*) des salles et de leur purge automatique après une période de rétention.
    - Protection de la vie privée : les salles de réunion sont désormais masquées des moteurs de recherche et des indexeurs d'IA.
- **Support** : Remplacement du chat Crisp par le formulaire de support officiel de La Suite.

### Évolutions techniques
- **Sécurité et Confidentialité (Renforcement majeur)** :
    - Implémentation d'un système de journalisation d'audit structuré pour tracer les actions sur les enregistrements, les transcriptions, les résumés et les opérations API.
    - Anonymisation massive des données sensibles : masquage des URLs signées, des erreurs de validation et des données sensibles dans les logs sources, les événements Sentry et les outils d'analyse.
    - Sécurisation des endpoints (limitation du débit sur l'enregistrement, authentification renforcée via échange de tokens).
    - Correction de nombreuses vulnérabilités (CVE) sur les composants critiques (Python, Nginx, Django, musl-utils, etc.).
- **Infrastructure et Backend** :
    - Mise à jour majeure de l'infrastructure LiveKit (serveur et egress).
    - Optimisation des performances via l'ajout d'un pool de connexions pour la base de données et d'index pour la recherche d'utilisateurs par email.
    - Amélioration de la robustesse du backend avec une gestion systématique des timeouts sur les appels API LiveKit.
    - Optimisation Docker : build natif des assets frontend pour les images arm64.

### Autres changements
- **Documentation** : Ajout de la documentation concernant les nouvelles fonctionnalités de journalisation d'audit et les améliorations de confidentialité.
- **Développement** : Intégration de `gitlint` comme hook de commit pour améliorer la qualité du code.
