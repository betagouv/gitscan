## Changelog : securix (30 derniers jours, au 20 avril 2026)

### Résumé
Cette mise à jour apporte des améliorations à l'outil d'upgrade de Securix, notamment la possibilité de spécifier une branche pour la mise à jour.  Le support matériel pour le ThinkPad X13 Gen 1 AMD a été ajouté, améliorant la compatibilité du système d'exploitation. Des corrections et ajustements de configuration ont également été effectués pour une meilleure stabilité et maintenabilité.

### Évolutions fonctionnelles
- Ajout de l'option `--securix-branch` à la commande d'upgrade pour spécifier la branche à utiliser. [#3157baf](https://github.com/cloud-gouv/securix/commit/3157baf)
- Support matériel ajouté pour le ThinkPad X13 Gen 1 AMD (20UF/20UG). [#f338bf5](https://github.com/cloud-gouv/securix/commit/f338bf5)
- Amélioration du script d'upgrade avec numéro de série dynamique. [#687994b](https://github.com/cloud-gouv/securix/commit/687994b)

### Évolutions techniques
- Correction : Suppression du module Openstack. [#f118112](https://github.com/cloud-gouv/securix/commit/f118112)
- Refactorisation de la configuration pour utiliser `mkDefault` et `mkForce` pour une meilleure lisibilité et cohérence. [#f29e66c](https://github.com/cloud-gouv/securix/commit/f29e66c), [#506f60d](https://github.com/cloud-gouv/securix/commit/506f60d)
- Correction du chemin Nix pour pointer vers une valeur statique. [#181ce4f](https://github.com/cloud-gouv/securix/commit/181ce4f)

### Autres changements
- Mise à jour du fichier README pour plus de clarté. [#8d9a055](https://github.com/cloud-gouv/securix/commit/8d9a055), [#f3819d3](https://github.com/cloud-gouv/securix/commit/f3819d3)
