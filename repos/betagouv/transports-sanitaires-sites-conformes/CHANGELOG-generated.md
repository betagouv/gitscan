## Changelog : transports-sanitaires-sites-conformes (30 derniers jours, au 22 septembre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur le renforcement de la sécurité des accès, notamment via l'amélioration de l'authentification à deux facteurs (2FA). L'expérience utilisateur a été optimisée par une meilleure visibilité de la FAQ et une recherche plus exhaustive, tandis que la robustesse du projet a été accrue par l'ajout de nouveaux contrôles automatiques de sécurité et de qualité dans le processus de développement.

### Évolutions fonctionnelles
- **Sécurité** : Amélioration de l'authentification à deux facteurs (2FA) [#592](https://github.com/betagouv/transports-sanitaires-sites-conformes/issues/592) et ajout d'une notification dans l'interface d'administration pour encourager les utilisateurs à l'activer.
- **Navigation** : Mise en avant de la FAQ en haut de page pour un accès plus rapide.
- **Interface** : Ajustements mineurs de la mise en page et de la rédaction de certains textes.

### Évolutions techniques
- **Sécurité et CI/CD** : 
    - Renforcement des droits d'accès pour les processus de CI [#584](https://github.com/betagouv/transports-sanitaires-sites-conformes/issues/584).
    - Mise en place d'un contrôle automatique des vulnérabilités (CVE) lors des changements de dépendances.
    - Intégration de l'outil de sécurité Bandit [#583](https://github.com/betagouv/transports-sanitaires-sites-conformes/issues/583).
- **Recherche** : Optimisation de l'indexation pour inclure le composant "hero" dans les résultats de recherche.
- **Qualité logicielle** : Ajout de `deptry` pour garantir la cohérence et la propreté des dépendances du projet [#582](https://github.com/betagouv/transports-sanitaires-sites-conformes/issues/582).

### Autres changements
- **Documentation** : Mise à jour de la documentation concernant les notifications et retrait du guide technique obsolète.
