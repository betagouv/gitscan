## Changelog : infra (30 derniers jours, au 08 juillet 2026)

### Résumé
Ce mois-ci, l'infrastructure a connu une vague de migrations de serveurs vers de nouvelles instances, ainsi que des ajustements de sécurité et de gestion des accès. L'ajout de Sentry pour la supervision des erreurs est une nouvelle fonctionnalité importante.

### Évolutions fonctionnelles
- Ajout de l'outil Sentry pour la supervision des erreurs et la collecte d'informations sur les incidents. [#44ed292](https://github.com/mission-apprentissage/infra/commit/44ed292)
- Prise en charge du serveur Sentry dans les pipelines de déploiement. [#bb1ea1e](https://github.com/mission-apprentissage/infra/commit/bb1ea1e)
- Correction des conditions pour l'envoi des événements à Sentry dans le workflow `install-app.yml`. [#d9a8e66](https://github.com/mission-apprentissage/infra/commit/d9a8e66)

### Évolutions techniques
- Migrations de plusieurs serveurs de production et de recette (api, lba, tdb, bal) vers de nouvelles instances.
- Migration du serveur de monitoring de production. [#c70225b](https://github.com/mission-apprentissage/infra/commit/c70225b)
- Suppression des sous-modules `authorizations` et `inventories`. [#e2faa1d](https://github.com/mission-apprentissage/infra/commit/e2faa1d)
- Mise à jour des habilitations d'accès aux différents projets.
- Rotation du secret principal SOPS pour renforcer la sécurité. [#83b04fe](https://github.com/mission-apprentissage/infra/commit/83b04fe)
- Correction de l'utilisation de la clé OpenPGP dans le workflow `all-servers-unban-ip.yml`. [#c7f39b2](https://github.com/mission-apprentissage/infra/commit/c7f39b2) et [#f02bef8](https://github.com/mission-apprentissage/infra/commit/f02bef8)
- Suppression du produit "sandbox". [#099c7d9](https://github.com/mission-apprentissage/infra/commit/099c7d9)

### Autres changements
- Remplacement d'une ancienne adresse IP dans la configuration. [#2f14a66](https://github.com/mission-apprentissage/infra/commit/2f14a66)
- Suppression de l'utilisateur Rémy des habilitations des projets api, bal, lba et mongodb.
- Annulation d'une modification temporaire concernant l'utilisation du profil TLS client par Certbot. [#ad21ec7](https://github.com/mission-apprentissage/infra/commit/ad21ec7)
