## Changelog : securix (30 derniers jours, au 11 avril 2026)

### Résumé
Ce changelog présente des améliorations concernant la configuration du système, notamment la gestion des scripts de mise à niveau et l'activation forcée de `boot.initrd.systemd.enable`. Des corrections ont également été apportées pour éviter des avertissements d'obsolescence et améliorer la documentation. Un module Openstack a été supprimé.

### Évolutions fonctionnelles
- Correction : Suppression du module Openstack, simplifiant la configuration par défaut et réduisant la surface d'attaque. [#112](https://github.com/cloud-gouv/securix/issues/112)
- Amélioration : Ajout d'une commande de mise à niveau documentée pour faciliter la maintenance du système. [#110](https://github.com/cloud-gouv/securix/issues/110)

### Évolutions techniques
- Modification : Utilisation de `mkDefault` pour une meilleure gestion des valeurs par défaut dans la configuration.
- Modification : Activation forcée de `boot.initrd.systemd.enable` à `true` pour garantir un démarrage correct du système.
- Correction : Reversion d'une modification précédente concernant la fonction `readInventory2` afin de corriger un problème potentiel.
- Amélioration : Mise à jour de `self.nix` pour refléter les dernières modifications.
- Refactoring : Application de suggestions de style pour améliorer la lisibilité du code.

### Autres changements
- Documentation : Ajout de valeurs par défaut pour certains paramètres de configuration.
- Nettoyage : Corrections mineures de style et de formatage du code.
