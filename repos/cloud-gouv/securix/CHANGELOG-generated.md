## Changelog : securix (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'ajout d'un outil de réinitialisation de YubiKey, l'amélioration de l'interface utilisateur et de l'organisation du code, ainsi que l'ajout de support pour un nouveau modèle de laptop. Des corrections et des ajustements ont également été apportés pour améliorer la stabilité et la convivialité.

### Évolutions fonctionnelles
- Ajout du support matériel pour le ThinkPad X13 Gen 1 AMD (20UF/20UG) [#181ce4f](https://github.com/cloud-gouv/securix/commit/181ce4f).
- Introduction d'un nouvel outil de réinitialisation de YubiKey, facilitant la gestion des clés de sécurité.
- Ajout de l'option `--securix-branch` à la commande d'upgrade, permettant de spécifier la branche securix à utiliser [#3157baf](https://github.com/cloud-gouv/securix/commit/3157baf).

### Évolutions techniques
- Refonte de l'outil de réinitialisation YubiKey pour utiliser une fonction Nix au lieu d'un parser Python, améliorant ainsi la sécurité et la maintenabilité [#d718d98](https://github.com/cloud-gouv/securix/commit/d718d98).
- Amélioration de l'organisation du code avec l'ajout de nouveaux fichiers et la restructuration des modules existants [#46e9f8e](https://github.com/cloud-gouv/securix/commit/46e9f8e).
- Mise à jour de l'inventaire generator avec des améliorations de code [#4f7b82c](https://github.com/cloud-gouv/securix/commit/4f7b82c).
- Application du style `nixfmt-rfc` pour une meilleure cohérence du code.
- Suppression de l'importation de polices depuis internet pour améliorer la sécurité et la performance [#5ca4b56](https://github.com/cloud-gouv/securix/commit/5ca4b56).

### Autres changements
- Mise à jour de la documentation README pour plus de clarté [#8d9a055](https://github.com/cloud-gouv/securix/commit/8d9a055) et [#f3819d3](https://github.com/cloud-gouv/securix/commit/f3819d3).
- Amélioration de l'expérience utilisateur (UX) pour faciliter le collage de valeurs dans l'interface [#5856207](https://github.com/cloud-gouv/securix/commit/5856207).
- Modifications mineures de l'interface utilisateur pour un meilleur rendu visuel [#ea030a4](https://github.com/cloud-gouv/securix/commit/ea030a4).
- Ajout d'un outil de génération d'inventaire [#b573591](https://github.com/cloud-gouv/securix/commit/b573591).
