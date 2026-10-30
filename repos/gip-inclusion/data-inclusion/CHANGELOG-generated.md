## Changelog : data-inclusion (30 derniers jours, au 29/10/2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur le renforcement de la sécurité et l'optimisation des processus de traitement de données. Le projet a gagné en fiabilité grâce à la suppression de flux de données obsolètes et à une meilleure validation des fichiers, tout en enrichissant les capacités de recherche pour les utilisateurs.

### Évolutions fonctionnelles
- **Recherche améliorée** : La recherche sémantique inclut désormais l'affichage des services à distance.
- **Export de données** : Rétablissement de la fonctionnalité d'exportation des statistiques.
- **Validation des imports** : Renforcement du contrôle des formats et de la taille des fichiers lors des téléchargements.

### Évolutions techniques
- **Sécurité & Authentification** : 
    - Amélioration de la gestion des jetons (expiration systématique et format basé sur les scopes).
    - Protection des données sensibles en retirant les jetons des liens de feedback et des événements de suivi (Sentry).
    - Durcissement des contrôles d'accès (validation des hôtes autorisés et des tailles de fichiers côté serveur).
- **Pipelines de données** : 
    - Optimisation des flux par la suppression de processus obsolètes (ingestion "monenfant") et de champs inutilisés (carif-oref, champs DORA).
    - Amélioration de la robustesse de l'ingestion DORA et de la validation des archives avant extraction.
- **Infrastructure & Déploiement** : 
    - Sécurisation de l'accès à MLflow en le routant exclusivement via Traefik.
    - Affinement des permissions de stockage (scopes de lecture/écriture sur les buckets).
    - Mise à jour de l'infrastructure réseau (Traefik).
- **CI/CD & Build** : 
    - Optimisation des processus de construction (utilisation de digests pour les images internes et suppression de la construction d'images inutilisées).
    - Intégration d'un rôle de "relecteur" dans les workflows de développement.

### Autres changements
- Renommage de certaines politiques de bucket pour une meilleure cohérence (de `autometa` vers `pilotage-inclusion`).
