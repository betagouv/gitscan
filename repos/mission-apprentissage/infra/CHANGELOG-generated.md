## Changelog : infra (30 derniers jours, au 08 juillet 2026)

### Résumé
Ce mois-ci, l'infrastructure a connu une vague de migrations de serveurs vers de nouvelles instances, ainsi que des ajustements de sécurité et de gestion des accès. L'ajout de Sentry pour la surveillance des erreurs est également une évolution notable.

### Évolutions fonctionnelles
- Ajout de l'outil Sentry pour la surveillance des erreurs et la gestion des exceptions. [#198](https://github.com/mission-apprentissage/infra/issues/198)
- Prise en charge du serveur Sentry dans les pipelines de déploiement.
- Correction des conditions pour l'activation de Sentry dans le workflow `install-app.yml`.

### Évolutions techniques
- Migrations des serveurs suivants : `api-production`, `lba-production`, `tdb-production`, `bal-production`, `lba-preview`, `tdb-recette`, `lba-recette`, `bal-recette`, `monitoring-production`.
- Suppression des sous-modules `authorizations` et `inventories`.
- Rotation du secret principal SOPS pour renforcer la sécurité.
- Suppression du produit `sandbox`.
- Rétrogradation temporaire d'une modification forcée du profil TLS client pour Certbot.
- Mise à jour des habilitations pour certains utilisateurs.
- Correction de la variable `PRODUCT_OPENPGP_KEY` dans le workflow `all-servers-unban-ip.yml`.
- Amélioration de la gestion des secrets SOPS pour le workflow `all-servers-unban-ip.yml`.

### Autres changements
- Remplacement d'une ancienne adresse IP dans la configuration. [#222](https://github.com/mission-apprentissage/infra/issues/222)
- Suppression de l'utilisateur Rémy des habilitations des projets `mongodb`, `lba`, `api` et `bal`.
- Nettoyage des habilitations du projet.
