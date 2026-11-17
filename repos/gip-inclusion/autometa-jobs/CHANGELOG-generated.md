## Changelog : autometa-jobs (30 derniers jours, au 17 novembre 2026)

### Résumé
Les récentes évolutions améliorent la flexibilité du système en permettant l'utilisation de liens sécurisés pour le traitement des données, tout en renforçant la sécurité et la légèreté de l'infrastructure.

### Évolutions fonctionnelles
- Possibilité pour les workers d'accepter des URI en `https://` (notamment des URLs présignées) pour l'accès aux données [#155](https://github.com/gip-inclusion/autometa-jobs/pull/155).

### Évolutions techniques
- Mise à jour de sécurité de la bibliothèque `opentelemetry-api` pour corriger une vulnérabilité (CVE-2026-126360).

### Autres changements
- Nettoyage de l'orchestrateur par la suppression de la dépendance inutile `python-dateutil`.
