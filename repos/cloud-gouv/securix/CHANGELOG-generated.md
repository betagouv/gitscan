## Changelog : securix (30 derniers jours, au 18 juin 2026)

### Résumé
Les dernières mises à jour de Securix se concentrent sur l'amélioration de la compatibilité matérielle, la correction de bugs liés à la conformité aux recommandations ANSSI, et l'amélioration de la stabilité de l'installateur. Des ajustements ont également été apportés à la configuration par défaut pour désactiver certains services et améliorer la documentation.

### Évolutions fonctionnelles
- **Compatibilité matérielle:** Ajout de la prise en charge du matériel Qemu/KVM. [#184](https://github.com/cloud-gouv/securix/issues/184)
- **Plymouth:** Initialisation des modules pour l'affichage de l'écran de démarrage Plymouth. [#184](https://github.com/cloud-gouv/securix/issues/184)
- **KWallet:** Désactivation de KWallet par défaut. [#93](https://github.com/cloud-gouv/securix/issues/93)
- **Documentation:** Mise à jour du fichier README pour améliorer la clarté et l'information. [#191](https://github.com/cloud-gouv/securix/issues/191) et [#168](https://github.com/cloud-gouv/securix/issues/168)

### Évolutions techniques
- **Nixpkgs:** Mise à jour vers Nixpkgs 26.05. [#174](https://github.com/cloud-gouv/securix/issues/174)
- **Secure Boot:** Correction d'un problème dans la vérification du Secure Boot pour la conformité ANSSI R3, en utilisant une comparaison de chaînes de caractères plus robuste. [#187](https://github.com/cloud-gouv/securix/issues/187)
- **Disko:** Mise à jour de Disko. [#186](https://github.com/cloud-gouv/securix/issues/186)
- **Installateur:** Correction d'un problème d'idempotence de l'installateur, garantissant que les installations répétées ne causent pas de conflits. [#185](https://github.com/cloud-gouv/securix/issues/185) et [#2bce6c3](https://github.com/cloud-gouv/securix/commit/2bce6c3)
- **Sysctl:** Amélioration de la fonction `mkSysctlChecker` pour utiliser une comparaison de chaînes de caractères. [#11c84dd](https://github.com/cloud-gouv/securix/commit/11c84dd)

### Autres changements
- Diverses améliorations mineures. [#185](https://github.com/cloud-gouv/securix/issues/185)
- Ajout d'un test pour vérifier l'idempotence de l'installateur.
