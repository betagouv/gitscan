## Changelog : infra (30 derniers jours, au 03 juillet 2026)

### Résumé
Ce mois-ci, l'infrastructure a subi une vague de migrations de serveurs vers de nouvelles instances. Plusieurs accès ont été révoqués et un nouveau produit, Sentry, a été intégré pour le monitoring des erreurs. Des ajustements ont été faits aux workflows Ansible pour améliorer la gestion des accès et la configuration des serveurs.

### Évolutions fonctionnelles
- Ajout du produit Sentry pour le monitoring des erreurs et l'alerte. [#198](https://github.com/mission-apprentissage/infra/issues/198)
- Prise en charge du serveur Sentry dans les pipelines de déploiement.
- Mise à jour de la clé OpenPGP utilisée pour le workflow `all-servers-unban-ip.yml`. [#222](https://github.com/mission-apprentissage/infra/issues/222)

### Évolutions techniques
- Migrations des serveurs : api-production, lba-production, tdb-production, bal-production, lba-preview, tdb-recette, lba-recette, bal-recette.
- Suppression des sous-modules `authorizations` et `inventories`.
- Suppression du produit `sandbox`.
- Réversion d'une modification temporaire concernant le profil TLSClient de Certbot.
- Suppression des accès de Rémy aux projets mongodb, lba, api et bal.

### Autres changements
- Correction des conditions pour Sentry dans le workflow `install-app.yml`.
- Amélioration de la gestion des secrets avec SOPS pour le workflow `all-servers-unban-ip.yml`.
- Migration du serveur monitoring-production.
