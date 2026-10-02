## Changelog : sites-conformes (30 derniers jours, au 1er octobre 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'amélioration de l'expérience de recherche, le renforcement de la sécurité (notamment via la double authentification) et l'optimisation des performances et de la sécurité de la chaîne de déploiement.

### Évolutions fonctionnelles
- **Amélioration de la recherche** : ajout de la date comme critère de filtrage pour les articles de blog et indexation du contenu "hero" pour des résultats plus pertinents.
- **Sécurité et expérience utilisateur** : renforcement de l'authentification à deux facteurs (2FA) [#592](https://github.com/numerique-gouv/sites-conformes/pull/592) et ajout d'une notification dans le backoffice pour inciter les utilisateurs à l'activer.
- **Navigation** : mise en avant de la FAQ dans la structure de navigation principale.

### Évolutions techniques
- **Performance** : optimisation de la configuration Gunicorn (gestion des workers, threads et du préchargement) pour une meilleure stabilité [#596](https://github.com/numerique-gouv/sites-conformes/pull/596).
- **Sécurité CI/CD** : renforcement des droits d'accès de la chaîne de CI [#584](https://github.com/numerique-gouv/sites-conformes/pull/584) et mise en place d'un contrôle automatique des vulnérabilités (CVE) lors des changements de dépendances.
- **Tests** : ajustement des tests de recherche pour mieux gérer les configurations personnalisées.

### Autres changements
- **Gestion des dépendances** : mise en place d'une période de latence ("cooldown") pour les mises à jour des dépendances Python et NPM [#588](https://github.com/numerique-gouv/sites-conformes/pull/588).
- **Documentation** : mise à jour de la documentation concernant la FAQ et les notifications, et retrait de guides techniques obsolètes.
- **Nettoyage** : corrections mineures de texte et de mise en forme.
