## Changelog : euphrosyne (30 derniers jours, au 20 octobre 2026)

### Résumé
Ce mois-ci, les développements ont principalement porté sur le renforcement de la sécurité de l'application (protection contre les injections XSS et sécurisation des redirections), l'optimisation du processus d'authentification via ORCID et la finalisation de la migration vers Django 6.1.

### Évolutions fonctionnelles
- **Sécurité** : Protection contre les failles XSS (Cross-Site Scripting) sur les pages projets et les emails HTML [#2059](https://github.com/betagouv/euphrosyne/issues/2059).
- **Sécurité** : Sécurisation des segments d'URL de répertoire et refus des redirections non autorisées [#2044](https://github.com/betagouv/euphrosyne/issues/2044).
- **Sécurité** : Restriction des téléchargements d'images lors de l'export PDF aux origines de confiance [#2045](https://github.com/betagouv/euphrosyne/issues/2045).
- **Sécurité** : Renforcement de la validation des signatures pour les webhooks Tally [#2042](https://github.com/betagouv/euphrosyne/issues/2042).
- **Authentification** : Amélioration du flux d'inscription ORCID pour assurer une liaison correcte avec les invitations valides [#2034](https://github.com/betagouv/euphrosyne/issues/2034).
- **Utilisateurs** : Restauration du statut "staff" pour les nouveaux utilisateurs invités dans un projet [#2033](https://github.com/betagouv/euphrosyne/issues/2033).
- **Permissions** : Renforcement de l'application des permissions de projet sur l'ensemble des routes de l'API [#2035](https://github.com/betagouv/euphrosyne/issues/2035).

### Évolutions techniques
- **Migration** : Finalisation de la migration vers Django 6.1.
- **Refactoring** : Suppression de l'export PDF des notebooks et de composants de rendu inutilisés pour alléger le code.
- **Correction** : Résolution des problèmes de compatibilité de l'administration des logs d'emails avec Django 6.1 [#2053](https://github.com/betagouv/euphrosyne/issues/2053).
- **Correction** : Sécurisation des redirections de retour dans l'administration des groupes d'objets.
- **Correction** : Liaison des types pour le mixin de permission de participation.

### Autres changements
- **Documentation** : Ajout et mise à jour du Document d'Architecture Technique (DAT), incluant la localisation des ressources Azure [#2052](https://github.com/betagouv/euphrosyne/issues/2052) et [#2054](https://github.com/betagouv/euphrosyne/issues/2054).
- **Documentation** : Documentation du processus de génération des traductions.
