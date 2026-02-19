## Changelog : charon (30 derniers jours)

### Résumé
Cette mise à jour apporte l'ajout du fournisseur d'authentification ProConnect, permettant aux utilisateurs de se connecter via ce service.  Des améliorations ont également été apportées au processus de publication des images Docker sur le GitHub Container Registry (ghcr) et à la configuration des workflows de CI/CD.

### Évolutions fonctionnelles
- Ajout du support du fournisseur d'authentification ProConnect. (#8)

### Évolutions techniques
- Modification du workflow de CI/CD pour publier les images Docker directement sur le GitHub Container Registry (ghcr). (#8)
- Suppression de la planification, des tags et exécution uniquement sur la branche principale pour le workflow de CI/CD.
