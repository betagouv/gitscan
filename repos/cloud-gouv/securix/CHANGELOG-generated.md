## Changelog : securix (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à securix au cours des 30 derniers jours. Les mises à jour se concentrent sur la correction de bugs, l'amélioration de la configuration du système, l'ajout de nouvelles fonctionnalités comme la prise en charge de qrencode et l'optimisation de la documentation.

### Évolutions fonctionnelles
- Correction d'un bug empêchant l'acceptation de mots de passe hachés vides [#109](https://github.com/cloud-gouv/securix/issues/109).
- Suppression du mode développeur et du flag associé, le rendant ainsi plus sécurisé.
- Ajout de la prise en charge de qrencode pour faciliter l'authentification et le partage de clés.
- Correction de la configuration VPN [#102](https://github.com/cloud-gouv/securix/issues/102).
- Suppression de la documentation Linux manuelle, simplifiant ainsi l'expérience utilisateur.
- Suppression de l'overlay g3proxy.
- Correction de fautes de frappe dans le fichier README.md [#99](https://github.com/cloud-gouv/securix/issues/99).

### Évolutions techniques
- Suppression de l'option `noexec` des options de montage du système de fichiers, améliorant potentiellement la flexibilité du système [#105](https://github.com/cloud-gouv/securix/issues/105).
- Amélioration de la fonction `readInventory2` pour supporter le mapping d'équipe.
- Amélioration de `mkTerminal` pour offrir un manuel.
- Refactoring partiel du fichier `lib/default`.

### Autres changements
- Ajout d'un dossier "communauté" et d'un script d'enregistrement Grist [#98](https://github.com/cloud-gouv/securix/issues/98).
- Ajout d'une commande pour mettre à jour la documentation [#110](https://github.com/cloud-gouv/securix/issues/110).
- Améliorations du style de code (rfc style) dans plusieurs commits.
- Corrections de linting.
