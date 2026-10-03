## Changelog : transfers (30 derniers jours, au 02/10/2026)

### Résumé
Les récentes évolutions se sont concentrées sur la fiabilité des téléchargements de fichiers volumineux et la sécurisation des transferts confidentiels. L'expérience utilisateur a été fluidifiée, notamment grâce à une meilleure gestion des reprises de téléchargement et un suivi plus précis de la livraison des fichiers auprès des destinataires.

### Évolutions fonctionnelles
- **Amélioration de l'expérience de téléchargement** : les téléchargements de gros fichiers chiffrés sont désormais plus robustes (notamment sur Firefox), supportent la reprise après une interruption et affichent un meilleur suivi de l'état et des erreurs.
- **Optimisation des transferts confidentiels** : l'interface est plus claire, l'accès est mieux contrôlé et les instructions pour le partage des clés de déchiffrement ont été améliorées.
- **Suivi de livraison** : affichage de l'état de réception pour chaque destinataire, permettant de ne plus rester en attente d'une confirmation globale lors de l'envoi.
- **Améliorations de l'interface (UI)** : l'application est plus fluide lors des rechargements de page, l'affichage des délais dans les emails est plus réaliste, et le sélecteur d'applications est désormais plus cohérent avec le reste de la Suite.

### Évolutions techniques
- **Renforcement de la sécurité** : restriction de l'accès à l'administration Django par une liste blanche d'IP, sécurisation de la chaîne d'approvisionnement (supply chain) du frontend et utilisation de capacités signées pour la reprise des téléchargements.
- **Fiabilité du traitement des fichiers** : optimisation de la gestion des scans de fichiers pour éviter les doublons et amélioration de la gestion des Service Workers pour garantir la continuité des téléchargements.
- **Infrastructure et CI/CD** : publication d'images backend "distroless" pour réduire la surface d'attaque et amélioration des logs du serveur Caddy.

### Autres changements
- **Uniformisation de la nomenclature** : renommage systématique de "transferts" en "transfers" dans l'ensemble du projet pour harmoniser le code et les identifiants.
