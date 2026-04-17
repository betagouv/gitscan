## Changelog : securix (30 derniers jours, au 11 avril 2026)

### Résumé
Ce changelog présente les récentes améliorations apportées à Securix. Les modifications incluent des ajustements de configuration pour le script de mise à niveau, la suppression du module Openstack et des corrections concernant la gestion de l'initrd et de l'inventaire.

### Évolutions fonctionnelles
- Suppression du module Openstack [#1234](https://github.com/cloud-gouv/securix/issues/1234).

### Évolutions techniques
- Modification de la configuration de l'initrd pour forcer l'activation de systemd.
- Passage à `mkDefault` pour une meilleure gestion des valeurs par défaut.
- Amélioration du script de mise à niveau avec un numéro de série dynamique.
- Rétractation d'une modification précédente concernant la fonction `readInventory2` pour éviter des régressions.

### Autres changements
- Aucun changement significatif à signaler.
