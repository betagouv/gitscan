## Changelog : francetransfert (30 derniers jours, au 10 septembre 2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de l'expérience utilisateur sur mobile et la fiabilisation de l'infrastructure. Un effort particulier a été porté sur l'observabilité du système afin de faciliter le diagnostic technique et la maintenance.

### Évolutions fonctionnelles
- **Compatibilité mobile :** Amélioration de la détection et de la compatibilité avec les appareils iOS (iPhone).
- **Expérience d'envoi :** Optimisation du processus d'envoi de fichiers grâce à l'introduction d'un délai de grâce lors de l'upload.

### Évolutions techniques
- **Observabilité :** Renforcement de la traçabilité via l'ajout de logs contextuels et de journaux détaillés pour les composants clés (Redis, Dex, gestion des erreurs).
- **Infrastructure & Déploiement :** 
    - Mise à jour des images de conteneurs.
    - Gestion des versions de Redis et ajustements de la passerelle (gateway).
    - Ajustement des seuils de réussite (success threshold).
- **Sécurité :** Mise à jour et gestion des secrets et des configurations réseau.
- **Gestion de version :** Préparation et mise à jour des versions pour le prochain cycle de déploiement.
