## Changelog : securix (30 derniers jours, au 21 juin 2026)

### Résumé
Ce changelog présente les améliorations apportées à securix au cours des 30 derniers jours. Les modifications incluent des corrections de bugs, des améliorations de la configuration système, et des ajustements pour une meilleure conformité aux recommandations ANSSI. Une tentative d'intégration du support Qemu/KVM a été annulée.

### Évolutions fonctionnelles
- **Grist:** Modification de l'URL/chemin d'enregistrement pour Grist [#192](https://github.com/cloud-gouv/securix/issues/192).
- **KWallet:** Désactivation de KWallet pour renforcer la sécurité [#93](https://github.com/cloud-gouv/securix/issues/93).
- **Plymouth:** Initialisation des modules de configuration de Plymouth (écran de démarrage) [#184](https://github.com/cloud-gouv/securix/issues/184).
- **Secure Boot:** Correction d'un problème dans la vérification du Secure Boot pour la conformité ANSSI R3 [#187](https://github.com/cloud-gouv/securix/issues/187).
- **Installation:** Correction d'un problème d'idempotence de l'installateur, assurant que les installations répétées ne causent pas de conflits ou d'erreurs [#186](https://github.com/cloud-gouv/securix/issues/186) et [#186](https://github.com/cloud-gouv/securix/issues/186).

### Évolutions techniques
- **Nixpkgs:** Mise à jour de Nixpkgs vers la version 26.05 [#174](https://github.com/cloud-gouv/securix/issues/174).
- **Sysctl:** Amélioration de la comparaison de chaînes de caractères dans `mkSysctlChecker` pour une meilleure fiabilité [#187](https://github.com/cloud-gouv/securix/issues/187).
- **Qemu/KVM:** Annulation de l'intégration du support matériel Qemu/KVM en raison de problèmes potentiels [#193](https://github.com/cloud-gouv/securix/issues/193).

### Autres changements
- **Documentation:** Mise à jour du fichier README [#191](https://github.com/cloud-gouv/securix/issues/191).
- **Documentation:** Mise à jour du fichier README concernant la configuration [#168](https://github.com/cloud-gouv/securix/issues/168).
- **Améliorations mineures:** Diverses améliorations mineures du code [#185](https://github.com/cloud-gouv/securix/issues/185).
- **Tests:** Ajout d'un test pour vérifier l'idempotence de l'installateur.
