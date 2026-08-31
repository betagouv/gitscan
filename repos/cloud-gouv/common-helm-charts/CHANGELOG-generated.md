## Changelog : common-helm-charts (30 derniers jours, au 28 août 2026)

### Résumé
Les récentes évolutions se sont concentrées sur l'amélioration de la visibilité via les tableaux de bord (Coturn et interconnexion) et sur un meilleur contrôle des accès et des ressources. Le projet gagne en précision dans la gestion des utilisateurs au sein des projets et renforce la sécurité grâce à une correction de la liste noire des ressources.

### Évolutions fonctionnelles
- **Gestion des accès** : Ajout de la possibilité d'inclure des utilisateurs supplémentaires dans les projets d'applications ([#45](https://github.com/cloud-gouv/common-helm-charts/pull/45)).
- **Observabilité** : Amélioration et correction des tableaux de bord Grafana pour les services Coturn et l'interconnexion ([#49](https://github.com/cloud-gouv/common-helm-charts/pull/49)).
- **Sécurité** : Correction de la gestion de la liste noire des ressources (resource blacklist) au niveau du projet ([#41](https://github.com/cloud-gouv/common-helm-charts/pull/41)).

### Évolutions techniques
- **CI/CD** : Optimisation du pipeline d'intégration continue pour utiliser le champ "version" lors du processus de tagging ([#47](https://github.com/cloud-gouv/common-helm-charts/pull/47)).
