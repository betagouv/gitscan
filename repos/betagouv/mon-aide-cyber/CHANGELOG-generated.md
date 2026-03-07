## Changelog : mon-aide-cyber (30 derniers jours)

### Résumé
Les dernières mises à jour de MonAideCyber se concentrent sur la sécurité du service, avec la correction de vulnérabilités identifiées par Dependabot. Des améliorations ont également été apportées à la gestion des aidants et à la mise en relation avec les demandeurs, ainsi qu'un ajout d'un encart de contact pour l'homologation.

### Évolutions fonctionnelles
- Amélioration de la mise en relation entre les aidants et les demandeurs, permettant de récupérer les aidants en fonction de leur SIRET et d'effectuer la mise en relation pour une organisation. [#2373273](https://github.com/betagouv/mon-aide-cyber/pull/2373273), [#0d63da4](https://github.com/betagouv/mon-aide-cyber/commit/0d63da4), [#d9c4157](https://github.com/betagouv/mon-aide-cyber/commit/d9c4157)
- Mise à jour du lien du mail de contact "Devenir aidant" pour rediriger vers la page des relais associatifs. [#5d80e72](https://github.com/betagouv/mon-aide-cyber/commit/5d80e72)
- Ajout d'un encart de contact pour les questions relatives aux fonctionnalités ou à la sécurité du service en phase d'homologation. [#619c732](https://github.com/betagouv/mon-aide-cyber/commit/619c732)

### Évolutions techniques
- Mise à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité : `minimatch` [#115](https://github.com/betagouv/mon-aide-cyber/security/dependabot/115), `basic-ftp` [#120](https://github.com/betagouv/mon-aide-cyber/security/dependabot/120), `axios` [#113](https://github.com/betagouv/mon-aide-cyber/security/dependabot/113), `cookie-session` [#101](https://github.com/betagouv/mon-aide-cyber/security/dependabot/101), `lodash` [#107](https://github.com/betagouv/mon-aide-cyber/security/dependabot/107).
- Mise à jour de `storybook` de la version 9.1.17 à la version 9.1.19. [#578c017](https://github.com/betagouv/mon-aide-cyber/commit/578c017)
- Mise à jour de `qs` de la version 6.14.1 à la version 6.14.2. [#06c8027](https://github.com/betagouv/mon-aide-cyber/commit/06c8027)
- Préparation de l'infrastructure pour la migration vers Clever Cloud en mettant à jour le bandeau de maintenance. [#b296192](https://github.com/betagouv/mon-aide-cyber/commit/b296192)
