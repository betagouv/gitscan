## Changelog : transfers (30 derniers jours, au 30 septembre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur la fiabilité des transferts de fichiers volumineux et la sécurisation de l'application. Les utilisateurs bénéficieront d'une meilleure gestion des téléchargements chiffrés (reprise après interruption) et d'une interface plus claire pour les transferts confidentiels. La sécurité globale a également été renforcée, tant au niveau de l'infrastructure que de l'accès à l'administration.

### Évolutions fonctionnelles
- **Amélioration des téléchargements :**
    - Gestion de la reprise des téléchargements volumineux et chiffrés en cas d'interruption (notamment sur Firefox).
    - Ajout d'un suivi de progression et d'une meilleure gestion des erreurs de téléchargement.
- **Expérience de transfert :**
    - Meilleure visibilité sur l'état de livraison pour chaque destinataire.
    - Optimisation de l'interface des transferts confidentiels pour une lecture plus simple et une gestion facilitée du partage de clés.
- **Interface utilisateur (UI) :**
    - Harmonisation du sélecteur d'applications avec le reste de la Suite.
    - Suppression des temps d'attente inutiles lors du rechargement de la page.
    - Amélioration des retours visuels lors des processus de scan de fichiers.

### Évolutions techniques
- **Sécurité :**
    - Restriction de l'accès à l'administration Django via une liste blanche d'adresses IP.
    - Renforcement de la sécurité de la chaîne d'approvisionnement (supply chain) du frontend.
    - Implémentation de capacités signées pour sécuriser la reprise des téléchargements.
- **Optimisation et Backend :**
    - Optimisation du processus de scan de fichiers (gestion des budgets d'attente et évitement des scans redondants).
    - Amélioration de la fiabilité de la mise à jour du registre de clés.
- **Infrastructure et CI/CD :**
    - Passage à des images backend "distroless" pour réduire la surface d'attaque.

### Autres changements
- **Communication :** Correction des modèles d'emails pour éviter de promettre des délais de traitement irréalistes.
- **Observabilité :** Ajout de logs pour le serveur Caddy.
