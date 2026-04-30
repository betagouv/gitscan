## Changelog : securix (30 derniers jours, au 28 avril 2026)

### Résumé
Ce mois-ci, les améliorations de securix se concentrent sur l'expérience utilisateur et la gestion des clés YubiKey, avec l'ajout d'un outil dédié pour la réinitialisation et la modification des utilisateurs. Des corrections ont également été apportées à la commande d'upgrade et à la configuration du système, notamment pour une meilleure compatibilité matérielle.

### Évolutions fonctionnelles
- Ajout d'un outil de réinitialisation et de modification des utilisateurs YubiKey [#1234](https://github.com/cloud-gouv/securix/issues/1234).
- Amélioration de l'interface utilisateur pour faciliter le copier-coller de valeurs dans l'outil YubiKey.
- Ajout de l'option `--securix-branch` à la commande d'upgrade pour spécifier la branche securix à utiliser [#1234](https://github.com/cloud-gouv/securix/issues/1234).
- Correction d'un bug empêchant l'option `--do-not-pull` de fonctionner correctement dans le script d'upgrade.
- Validation du verbe passé à la commande d'upgrade pour éviter des erreurs.
- Ajout du support matériel pour le ThinkPad X13 Gen 1 AMD (20UF/20UG).

### Évolutions techniques
- Refactorisation du code dans `permissionless-upgrade.nix` pour supprimer une ligne inutile.
- Suppression du parser Python dans l'outil YubiKey et remplacement par une fonction Nix pour une meilleure cohérence.
- Amélioration de l'organisation des fichiers et ajout de nouveaux fichiers pour une meilleure structure du projet.
- Mise à jour de l'attribut `postInstallScript` dans `mkTerminal` pour une plus grande flexibilité.

### Autres changements
- Mise à jour de la documentation README avec des informations plus claires et précises.
- Amélioration du rendu HTML de l'outil YubiKey.
- Suppression de l'importation de polices depuis internet pour une meilleure sécurité et performance.
- Ajout d'un générateur d'inventaire pour faciliter la gestion des configurations.
- Application du style `nixfmt-rfc` à plusieurs fichiers pour une meilleure cohérence du code.
- Correction de la définition du chemin Nix pour utiliser une valeur statique.
