## Changelog : securix (30 derniers jours, au 27 octobre 2026)

### Résumé
Les dernières mises à jour de SecurixOS renforcent la stabilité du processus de mise à jour automatique, améliorent la configuration des navigateurs web et introduisent de nouveaux outils communautaires, notamment pour la gestion des clés de sécurité Yubikey.

### Évolutions fonctionnelles
- **Navigation web** : Firefox est désormais maintenu par défaut ; pour Chromium, l'utilisation du mode PAC requiert désormais la présence d'un script PAC.
- **Réseau** : Amélioration de la fiabilité des connexions VPN via une meilleure gestion de l'ordre des DN dans les profils IPsec [#279](https://github.com/cloud-gouv/securix/issues/279).
- **Outils communautaires** : Ajout d'un module permettant la réinitialisation des clés Yubikey [#302](https://github.com/cloud-gouv/securix/issues/302).

### Évolutions techniques
- **Mises à jour automatiques** : Optimisation de la fiabilité avec la correction des temporisateurs de récupération [#277](https://github.com/cloud-gouv/securix/issues/277) et la suppression automatique des anciennes générations du système une fois la mise à jour terminée [#276](https://github.com/cloud-gouv/securix/issues/276).
- **Sécurité CI/CD** : Durcissement de la sécurité des GitHub Actions en appliquant des permissions vides par défaut [#306](https://github.com/cloud-gouv/securix/issues/306).
- **Télémétrie** : Implémentation d'un système de rapport de télémétrie de base (incluant le nom d'hôte et le temps de démarrage).
- **Boot & Installation** : Amélioration de la génération et des tests du script `netbootIpxe` pour l'installateur réseau.
- **Maintenance du code** : 
    - Correction du générateur d'inventaire [#303](https://github.com/cloud-gouv/securix/issues/303).
    - Correction de la gestion des commandes `sudo` en cas d'utilisateur vide [#284](https://github.com/cloud-gouv/securix/issues/284).
    - Nettoyage des tests obsolètes concernant les raccourcis clavier Sway [#274](https://github.com/cloud-gouv/securix/issues/274).

### Autres changements
- **Documentation** : Correction de diverses coquilles et erreurs de typographie dans le README [#297](https://github.com/cloud-gouv/securix/issues/297).
- **Gouvernance & Conformité** : Désignation d'un nouveau responsable de code (*code owner*) [#305](https://github.com/cloud-gouv/securix/pull/305) et uniformisation des en-têtes de licence SPDX [#308](https://github.com/cloud-gouv/securix/issues/308).
