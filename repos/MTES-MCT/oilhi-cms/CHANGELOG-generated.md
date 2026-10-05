## Changelog : oilhi-cms (30 derniers jours, au 1er octobre 2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de la recherche de contenu, le renforcement de la sécurité des accès (notamment via la double authentification) et l'optimisation de la robustesse et des performances de l'infrastructure de déploiement.

### Évolutions fonctionnelles
- **Amélioration de la recherche** : indexation des dates des articles de blog et des éléments "hero" pour des résultats plus pertinents.
- **Sécurité et expérience utilisateur** : renforcement de l'authentification à deux facteurs (2FA) et ajout de notifications dans l'interface d'administration pour encourager son activation [#592](https://github.com/MTES-MCT/oilhi-cms/issues/592).
- **Navigation** : mise en avant de la FAQ dans la structure de navigation principale.

### Évolutions techniques
- **Performance** : optimisation de la configuration du serveur Gunicorn (gestion des workers, threads et préchargement) pour une meilleure stabilité [#596](https://github.com/MTES-MCT/oilhi-cms/issues/596).
- **Sécurité et CI/CD** :
    - Mise en place d'un contrôle automatique des vulnérabilités (CVE) lors des changements de dépendances.
    - Renforcement des droits d'accès pour les processus d'intégration continue (CI) [#584](https://github.com/MTES-MCT/oilhi-cms/issues/584).
    - Introduction d'une période de "cooldown" pour la gestion des dépendances Python et NPM [#588](https://github.com/MTES-MCT/oilhi-cms/issues/588).
- **Tests** : ajustement des tests de recherche pour isoler les comportements personnalisés.

### Autres changements
- **Documentation** : mise à jour de la documentation concernant les notifications et la FAQ.
