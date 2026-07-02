## Changelog : tchap-web-v4 (30 derniers jours, au 26 juin 2024)

### Résumé
Cette version apporte des améliorations de sécurité, des corrections de bugs concernant les invitations et le partage de messages, ainsi que des ajustements pour l'intégration avec la nouvelle version d'EC (Element Client). Des options de configuration ont également été réactivées et des mises à jour de dépendances ont été effectuées.

### Évolutions fonctionnelles
- Correction du partage de messages externes : amélioration de la robustesse du flux d'invitation externe et correction du copier-coller d'invitations dans les salles externes. [#1609](https://github.com/tchapgouv/tchap-web-v4/pull/1609)
- Amélioration de la gestion des invitations : correction d'un bug lié aux invitations internes dans le nouveau flux. [#1607-fix-invite-internal-new-flow](https://github.com/tchapgouv/tchap-web-v4/pull/1609)
- Réactivation de l'option de liste rouge : la possibilité de réactiver la liste rouge est de nouveau disponible dans la configuration. [#1612](https://github.com/tchapgouv/tchap-web-v4/pull/1612)
- Amélioration du comportement de téléchargement : le comportement de téléchargement a été mis à jour pour n'envoyer que le nom du fichier. [#1622](https://github.com/tchapgouv/tchap-web-v4/pull/1622)
- Acceptation automatique des permissions des widgets EC :  les permissions des nouveaux widgets EC sont maintenant acceptées automatiquement pour s'aligner avec la nouvelle version d'EC. [#1622](https://github.com/tchapgouv/tchap-web-v4/pull/1622)
- Valeur par défaut du badge : modification de la valeur par défaut du badge pour les salles privées. [#1608-change-default-badge-value](https://github.com/tchapgouv/tchap-web-v4/pull/1610)

### Évolutions techniques
- Mise à jour d'EC : intégration des dernières versions d'EC (0.19.0, 0.19.1, 0.20.2) et ajustements pour assurer la compatibilité. [#1618](https://github.com/tchapgouv/tchap-web-v4/pull/1618)
- Suppression d'un plugin Tauri inutilisé.
- Corrections de sécurité mineures sur la version desktop. [#1617](https://github.com/tchapgouv/tchap-web-v4/pull/1617)
- Suppression du service de l'IPC keyring et mise à jour du comportement de téléchargement sur la version desktop. [#1617](https://github.com/tchapgouv/tchap-web-v4/pull/1617)
- Mise à jour du message d'erreur. [#1620](https://github.com/tchapgouv/tchap-web-v4/pull/1620)

### Autres changements
- Mise à jour vers la version 4.20.0. [#1623](https://github.com/tchapgouv/tchap-web-v4/pull/1623)
- Mise à jour vers la version 4.19.9. [#1613](https://github.com/tchapgouv/tchap-web-v4/pull/1613)
- Correction de linting.
