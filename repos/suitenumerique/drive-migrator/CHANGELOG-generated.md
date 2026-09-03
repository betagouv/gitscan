## Changelog : drive-migrator (30 derniers jours, au 28 août 2026)

### Résumé
Ce mois-ci, le projet a principalement porté sur la sécurisation des processus d'authentification et le renforcement des outils d'administration. L'expérience utilisateur a également été affinée grâce à une interface plus explicite et des communications (emails et messages d'erreur) plus claires.

### Évolutions fonctionnelles
- **Interface utilisateur** : ajout d'infobulles pour les titres tronqués [#195](https://github.com/suitenumerique/drive-migrator/issues/195), précision de la cible de migration (Fichiers/Drive) [#193](https://github.com/suitenumerique/drive-migrator/issues/193) et optimisation du parcours de téléchargement des archives ZIP [#194](https://github.com/suitenumerique/drive-migrator/issues/194).
- **Administration** : ajout de la possibilité de réinitialiser les connexions Resana ou Drive [#198](https://github.com/suitenumerique/drive-migrator/issues/198) et enrichissement de la recherche d'utilisateurs dans les espaces de travail (ajout du nom et de l'email).
- **Corrections** : correction de la formulation des messages d'erreur lors de la migration d'un espace de travail [#140](https://github.com/suitenumerique/drive-migrator/issues/140) et correction de fautes d'orthographe dans les modèles d'emails de notification.

### Évolutions techniques
- **Sécurité et Authentification** : migration vers le protocole PKCE pour l'authentification Resana, suppression du scraping HTML CSRF et amélioration de la gestion et de la sérialisation des jetons (tokens) et des sessions.
- **Optimisations Backend** : amélioration de la précision des logs (distinction entre les tentatives en INFO et les échecs finaux en ERROR) et suppression de l'en-tête `x-amz-acl` non signé lors des téléchargements S3 présignés.

### Autres changements
- Nettoyage du code et suppression de tests et de logs redondants.
