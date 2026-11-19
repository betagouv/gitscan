## Changelog : autometa-jobs (30 derniers jours, au 19 novembre 2026)

### Résumé
Les récentes mises à jour améliorent la capacité du système à traiter des données via des liens sécurisés et renforcent la sécurité ainsi que la légèreté de l'infrastructure.

### Évolutions fonctionnelles
- Les workers acceptent désormais les URIs en `https://`, permettant notamment l'utilisation d'URLs présignées pour l'accès aux ressources. [#155](https://github.com/gip-inclusion/autometa-jobs/issues/155)

### Évolutions techniques
- **Sécurité** : Mise à jour de `opentelemetry-api` vers la version 1.45.2 pour corriger une vulnérabilité (CVE-2026-126360).
- **Optimisation** : Nettoyage de l'orchestrateur par la suppression de la dépendance inutile `python-dateutil`.
