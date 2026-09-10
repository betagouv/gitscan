## Changelog : mobilic-metabase (30 derniers jours, au 09/09/2026)

### Résumé
Ce mois-ci a été consacré au lancement du projet et à la mise en place d'une infrastructure de déploiement sécurisée pour Metabase. L'objectif principal a été de garantir que l'accès aux outils de visualisation de données soit protégé par un système d'authentification robuste.

### Évolutions fonctionnelles
- Sécurisation de l'accès à l'interface Metabase via l'intégration de `oauth2-proxy` [#1](https://github.com/MTES-MCT/mobilic-metabase/pull/1).

### Évolutions techniques
- Renforcement de la sécurité du déploiement de l'instance Metabase.
- Sécurisation des scripts d'infrastructure et verrouillage des versions des buildpacks (*pinning*) pour garantir la stabilité et la reproductibilité des environnements.
