## Changelog : securix (30 derniers jours, au 25 juin 2026)

### Résumé
Cette version apporte des améliorations à la localisation en français, corrige des problèmes liés à la vérification du démarrage sécurisé (Secure Boot) et à l'idempotence de l'installateur. Des ajustements ont également été effectués concernant l'intégration de Qemu/KVM et l'URL de l'enregistrement Grist.

### Évolutions fonctionnelles
- Ajout d'une initialisation de la localisation française (#182).
- Désactivation de KWallet pour renforcer la sécurité (#93).
- Correction de l'idempotence de l'installateur, assurant un comportement prévisible lors de réinstallations (#193, #2bce6c3).
- Correction d'un problème dans la vérification du démarrage sécurisé (Secure Boot) pour l'ANSSI R3 (#187).
- Mise à jour de l'URL/chemin pour l'enregistrement Grist (#192).

### Évolutions techniques
- Mise à jour de `nixpkgs` vers la version 26.05 (#174).
- Mise à jour de `disko` (#186).
- Ajout d'un test pour vérifier l'idempotence de l'installateur (#193).
- Correction d'une comparaison incorrecte dans la fonction `mkSysctlChecker` pour l'ANSSI (#11c84dd).
- Initialisation des modules Plymouth pour l'affichage du démarrage (#184).
- Intégration initiale du support matériel Qemu/KVM (réverté ultérieurement, #193).

### Autres changements
- Mise à jour de la documentation README (#191).
- Correction de l'importation de la localisation i18n (#199).
- Améliorations mineures diverses (#185).
