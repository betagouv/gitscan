## Changelog : tchap-web-v4 (30 derniers jours, au 26 juin 2026)

### Résumé
Cette version apporte des améliorations significatives au flux d'invitation externe, notamment une correction pour le copier-coller des invitations et une gestion plus robuste du processus. De plus, la possibilité d'activer une liste rouge de domaines est réactivée et une option de mise à jour automatique pour la version desktop est ajoutée. Enfin, des corrections et améliorations internes ont été apportées pour une meilleure stabilité et conformité.

### Évolutions fonctionnelles
- **Invitations externes :** Correction d'un bug empêchant le copier-coller correct des liens d'invitation vers des salles externes [#1609](https://github.com/tchapgouv/tchap-web-v4/pull/1609).
- **Invitations externes :** Amélioration de la robustesse du flux d'invitation externe [#1609](https://github.com/tchapgouv/tchap-web-v4/pull/1609).
- **Liste rouge :** Réactivation de l'option permettant d'activer une liste rouge de domaines [#1612](https://github.com/tchapgouv/tchap-web-v4/pull/1612).
- **Mise à jour automatique (Desktop) :** Ajout de la possibilité de mettre à jour l'application desktop automatiquement [#1610](https://github.com/tchapgouv/tchap-web-v4/pull/1610).
- **Salles privées :** Retour à la configuration par défaut pour les salles privées si aucune règle d'accès n'est définie et que la salle est chiffrée [#1608](https://github.com/tchapgouv/tchap-web-v4/pull/1608).

### Évolutions techniques
- Mise à jour des dépendances.
- Renommage du paramètre `im.vector.room.access_rules.encrypted` en `im.vector.room.access_rules.force_unencrypted_at_creation` pour plus de clarté.

### Autres changements
- Correction de problèmes de linter.
- Amélioration de la vérification avant d'inviter un utilisateur.
- Mises à jour de version : 4.19.8 et 4.19.9.
