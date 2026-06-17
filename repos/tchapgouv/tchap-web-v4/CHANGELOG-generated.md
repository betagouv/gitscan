## Changelog : tchap-web-v4 (30 derniers jours, au 26 juin 2024)

### Résumé
Cette mise à jour apporte des améliorations à la gestion des invitations externes, la réactivation de la liste rouge des utilisateurs, et la possibilité de mise à jour automatique de l'application de bureau. Des corrections et ajustements internes ont également été effectués pour améliorer la robustesse et la configuration de l'application.

### Évolutions fonctionnelles
- Correction d'un problème de copie-coller d'invitations dans les salles externes [#1609](https://github.com/tchapgouv/tchap-web-v4/pull/1609).
- Réactivation de l'option de liste rouge des utilisateurs [#1612](https://github.com/tchapgouv/tchap-web-v4/pull/1612).
- Possibilité de mise à jour automatique de l'application de bureau [#1611](https://github.com/tchapgouv/tchap-web-v4/pull/1611).
- Amélioration du flux d'invitation externe pour une plus grande robustesse [#1609](https://github.com/tchapgouv/tchap-web-v4/pull/1609).
- Retour à la configuration par défaut des salles privées si aucune règle d'accès n'est définie et que la salle est chiffrée [#1610](https://github.com/tchapgouv/tchap-web-v4/pull/1610).

### Évolutions techniques
- Mise à jour des dépendances [#1603](https://github.com/tchapgouv/tchap-web-v4/pull/1603).
- Renommage du paramètre `im.vector.room.access_rules.encrypted` en `im.vector.room.access_rules.force_unencrypted_at_creation` pour une meilleure clarté [#1601](https://github.com/tchapgouv/tchap-web-v4/pull/1601).

### Autres changements
- Correction de problèmes de linter [#1601](https://github.com/tchapgouv/tchap-web-v4/pull/1601).
- Mises à jour de version : 4.19.8, 4.19.9 [#1603](https://github.com/tchapgouv/tchap-web-v4/pull/1603), [#1613](https://github.com/tchapgouv/tchap-web-v4/pull/1613).
