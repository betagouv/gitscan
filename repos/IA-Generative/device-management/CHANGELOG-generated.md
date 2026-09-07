## Changelog : device-management (30 derniers jours, au 06/09/2026)

### Résumé
Cette période a été marquée par un renforcement significatif de la fiabilité du système de distribution des fichiers et une amélioration des outils d'administration. Les utilisateurs bénéficieront de nouvelles capacités d'exportation de données pour le suivi de parc, tandis que la stabilité technique a été consolidée par une meilleure gestion des caches et une sécurisation des processus de déploiement.

### Évolutions fonctionnelles
- **Gestion du parc et suivi** : Introduction d'une nouvelle fonctionnalité d'exportation des agrégats d'usage vers le bus de suivi (version bêta), incluant des exports manuels et une section dédiée dans l'interface d'administration [#29](https://github.com/IA-Generative/device-management/pull/29).
- **Interface d'administration** : 
    - Amélioration de la visibilité de la version du système dans l'interface [#33](https://github.com/IA-Generative/device-management/pull/33).
    - Correction d'un bug d'affichage dans l'activité des appareils lié à une colonne inexistante.
- **Résolution de catalogue** : Amélioration de la recherche de catalogue qui accepte désormais la résolution par nom d'export et par slug.

### Évolutions techniques
- **Intégrité des données et cache** : Correction d'un problème critique de vérification des sommes de contrôle (checksum) : le système vérifie désormais l'intégrité des fichiers binaires et du catalogue stockés en cache avant de les servir, garantissant qu'aucun fichier corrompu n'est distribué [#5](https://github.com/IA-Generative/device-management/issues/5).
- **Sécurité et Authentification** : 
    - Renforcement de la sécurité des sessions en excluant le `id_token` des cookies de session.
    - Correction de la gestion des cookies d'état OIDC lors de l'expiration des appels API.
- **Déploiement et CI/CD** : 
    - Optimisation du processus de build pour que les images Docker déclarent automatiquement leur version au lieu d'utiliser des valeurs fixes.
    - Amélioration de la propagation des tags d'image lors des déploiements en cluster.
- **Infrastructure et Base de données** : 
    - Passage en mode "opt-in" pour la création automatique des rôles, bases de données et schémas au démarrage afin de mieux contrôler l'initialisation.
    - Amélioration de l'extraction de la version via le manifeste `dm-manifest.json`.
- **Télémétrie** : Mise en place d'attributs typés pour les données de télémétrie [#34](https://github.com/IA-Generative/device-management/pull/34).

### Autres changements
- **Documentation** : Clarification des procédures concernant la cohabitation entre le déploiement général (rollout) et les branches d'expérimentation.
- **Qualité du code** : Diverses corrections de tests et nettoyage de la syntaxe (linting) pour améliorer la maintenabilité.
