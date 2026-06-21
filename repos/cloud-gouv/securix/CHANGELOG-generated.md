## Changelog : securix (30 derniers jours, au 19 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à la sécurité et à la configuration de SecurixOS. On note l'ajout de support pour Qemu/KVM, des corrections pour la conformité aux recommandations ANSSI (notamment Secure Boot), et des améliorations de l'installateur. L'intégration de Nixpkgs 26.05 permet également de bénéficier des dernières versions des logiciels.

### Évolutions fonctionnelles
- Ajout du support pour le matériel Qemu/KVM, permettant une virtualisation plus aisée. [#184](https://github.com/cloud-gouv/securix/issues/184)
- Désactivation de KWallet par défaut pour renforcer la sécurité. [#93](https://github.com/cloud-gouv/securix/issues/93)
- Amélioration de l'installateur pour garantir son idempotence (ré-exécution sans effet indésirable). [#174](https://github.com/cloud-gouv/securix/issues/174)
- Mise à jour de l'URL/chemin d'enregistrement Grist. [#192](https://github.com/cloud-gouv/securix/issues/192)

### Évolutions techniques
- Mise à jour de Nixpkgs vers la version 26.05, apportant les dernières versions des paquets. [#174](https://github.com/cloud-gouv/securix/issues/174)
- Correction d'un problème de regex dans la vérification du Secure Boot pour la conformité ANSSI R3. [#187](https://github.com/cloud-gouv/securix/issues/187)
- Amélioration de la comparaison de chaînes de caractères dans la configuration ANSSI. [#11c84dd](https://github.com/cloud-gouv/securix/commit/11c84dd)
- Correction d'un bug et amélioration mineure de `disko`. [#186](https://github.com/cloud-gouv/securix/issues/186) et [#185](https://github.com/cloud-gouv/securix/issues/185)

### Autres changements
- Mise à jour de la documentation README. [#191](https://github.com/cloud-gouv/securix/issues/191)
- Mise à jour de la documentation concernant la configuration. [#168](https://github.com/cloud-gouv/securix/issues/168)
- Ajout d'un test pour l'idempotence de l'installateur.
