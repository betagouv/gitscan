## Changelog : securix (30 derniers jours, au 26 mai 2026)

### Résumé
Ce changelog présente des améliorations concernant la validation des commandes d'upgrade, la correction d'un bug empêchant l'option `--do-not-pull` de fonctionner correctement lors des mises à jour, et une petite mise à jour de la documentation. Une modification technique a également été apportée pour exposer un attribut dans `mkTerminal`.

### Évolutions fonctionnelles
- Correction d'un bug : L'option `--do-not-pull` fonctionne désormais correctement lors des mises à jour du système [#1593f03](https://github.com/cloud-gouv/securix/commit/1593f03).
- Amélioration de la validation : Validation du verbe passé à la commande d'upgrade pour éviter des erreurs d'utilisation [#ff5c4de](https://github.com/cloud-gouv/securix/commit/ff5c4de).

### Évolutions techniques
- Refactoring : Suppression d'une ligne inutile dans `permissionless-upgrade.nix` [#64626fe](https://github.com/cloud-gouv/securix/commit/64626fe).
- Modification de l'API : `mkTerminal` expose désormais l'attribut `postInstallScript` [#aeee115](https://github.com/cloud-gouv/securix/commit/aeee115).

### Autres changements
- Documentation : Mise à jour du fichier README [#bd2039a](https://github.com/cloud-gouv/securix/commit/bd2039a).
