## Changelog : charon (30 derniers jours)

### Résumé
Cette version apporte des améliorations à la gestion des fournisseurs d'authentification, notamment l'ajout du provider Proconnect. Des corrections ont également été apportées pour assurer le bon fonctionnement des tests et du pipeline de déploiement. Enfin, des optimisations ont été réalisées sur le processus de publication des images Docker.

### Évolutions fonctionnelles
- Ajout du support du provider Proconnect (#8)
- Correction de l'URL de test pour le provider Proconnect (#9, #11)

### Évolutions techniques
- Modification du workflow de CI/CD pour publier les images Docker sur GitHub Container Registry (GHCR) (#8)
- Suppression de la planification, des tags et exécution uniquement sur la branche `main` dans le workflow de CI/CD (#8)
- Ajout du SHA à l'image Docker pour une meilleure traçabilité (#10)

### Autres changements
- Correction de l'URL du bac à sable pour le provider Proconnect (#11)
