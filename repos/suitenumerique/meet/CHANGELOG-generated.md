## Changelog : meet (30 derniers jours, au 07 novembre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur le renforcement de la sécurité et de la confidentialité des données, notamment via l'implémentation d'un système d'audit complet et une meilleure protection des informations sensibles dans les journaux système. Les utilisateurs bénéficieront également d'une plus grande stabilité lors des appels grâce à une gestion améliorée des reconnexions et d'une expérience utilisateur plus fluide et accessible.

### Évolutions fonctionnelles
- **Gestion des enregistrements :** Les utilisateurs peuvent désormais choisir l'encodage de leurs enregistrements. Tout utilisateur authentifié est autorisé à lancer un enregistrement, et des notifications par email sont envoyées pour confirmer la disponibilité.
- **Stabilité et connectivité :** Introduction d'une politique de reconnexion automatique plus intelligente (exponential backoff) pour stabiliser les appels vidéo. Des messages clairs informent désormais les participants en cas d'interruption d'un enregistrement ou de perte de connexion.
- **Accessibilité et UX :** Amélioration de l'accessibilité (navigation au clavier via la touche Échap, indicateurs de focus visibles, annonces de changement d'état du micro) et meilleure gestion des erreurs (affichage explicite des erreurs de connexion dans le lobby).
- **Support :** Le chat Crisp est remplacé par le formulaire de support officiel de La Suite.

### Évolutions techniques
- **Sécurité et Confidentialité :** 
    - Mise en place d'un système d'audit structuré pour tracer les enregistrements, les transcriptions, les résumés et les actions administratives.
    - Protection massive des données sensibles : masquage des URLs signées, des détails des tâches Celery et des erreurs de validation dans les logs, les outils d'analyse et Sentry.
    - Durcissement de l'accès aux salles (utilisation de endpoints POST pour les jetons d'accès, restriction des slugs de salles).
- **Infrastructure et Performance :** 
    - Optimisation de la base de données (indexation des emails pour des recherches sans casse, ajout d'un pool de connexions psycopg).
    - Support natif des images Docker pour l'architecture arm64.
    - Mise à jour majeure des composants d'infrastructure (LiveKit, Docker, Helm).
- **Backend & API :** 
    - Introduction de l'échange de jetons pour permettre l'intégration de Meet via des iframes.
    - Gestion du cycle de vie des salles avec suppression logique (soft delete) et purge automatique après une période de rétention.
- **Maintenance de sécurité :** Correction de nombreuses vulnérabilités (CVE) sur l'ensemble de la stack (Python, Nginx, Node, Django, etc.).

### Autres changements
- **Documentation :** Mise à jour de la documentation relative au système d'audit et du changelog.
- **CI/CD :** Optimisation des scans de sécurité (Trivy) et des processus de build.
