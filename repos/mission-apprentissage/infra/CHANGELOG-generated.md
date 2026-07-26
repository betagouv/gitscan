## Changelog : infra (30 derniers jours, au 24 juillet 2026)

### Résumé
Ce mois-ci, l'infrastructure a bénéficié d'améliorations axées sur le monitoring, la gestion des logs et la sécurité. L'ajout de Sentry permet un meilleur suivi des erreurs applicatives. Des corrections et mises à jour de configuration ont également été apportées pour assurer la stabilité et la sécurité des serveurs.

### Évolutions fonctionnelles
- Le port des métriques MongoDB (9946) est maintenant ouvert vers le monitoring du cluster LBA, permettant une surveillance plus précise des performances de la base de données. [#225](https://github.com/mission-apprentissage/infra/issues/225)
- Intégration de Sentry pour le suivi des erreurs applicatives :
    - Ajout du produit Sentry. [#225](https://github.com/mission-apprentissage/infra/issues/225)
    - Prise en charge du serveur sentry-production dans les pipelines.
- Amélioration de la gestion des logs : les niveaux de logs numériques sont maintenant mappés à des noms lisibles dans Fluentd. [#224](https://github.com/mission-apprentissage/infra/issues/224)

### Évolutions techniques
- Correction d'un problème lié à la hauteur du terminal dans tmux. [#226](https://github.com/mission-apprentissage/infra/issues/226)
- Rétrogradation d'une modification forcée de l'utilisation du profil TLS client par Certbot.
- Migration du serveur monitoring-production.
- Mise à jour des habilitations.
- Rotation du secret principal SOPS.
- Suppression du produit sandbox.

### Autres changements
- Correction d'une faute de frappe.
- Mise à jour de l'adresse IP dans un workflow. [#222](https://github.com/mission-apprentissage/infra/issues/222)
- Correction de la variable `PRODUCT_OPENPGP_KEY` dans le workflow `all-servers-unban-ip.yml`.
- Correction des conditions pour Sentry dans `install-app.yml`.
