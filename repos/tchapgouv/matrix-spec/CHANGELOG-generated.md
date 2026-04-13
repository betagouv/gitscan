## Changelog : matrix-spec (30 derniers jours, au 2026-03-20)

### Résumé
Ce changelog présente les récentes mises à jour de la spécification du protocole Matrix. Les changements se concentrent sur l'ajout de support pour de nouvelles fonctionnalités d'autorisation d'appareil (Device Authorization Grant) et de serveurs de politiques, ainsi que sur des corrections de typographie et de définitions en doublon pour améliorer la clarté et la cohérence de la spécification.

### Évolutions fonctionnelles
- Ajout de la spécification pour le support de la méthode d'autorisation d'appareil RFC 8628 (Device Authorization Grant) [#2320](https://github.com/tchapgouv/matrix-spec/issues/2320).
- Spécification des serveurs de politiques (Policy Servers) [#2332](https://github.com/tchapgouv/matrix-spec/issues/2332).

### Évolutions techniques
- Correction d'une définition en doublon pour le code d'erreur `M_THREEPID_IN_USE` et réorganisation des codes d'erreur [#2336](https://github.com/tchapgouv/matrix-spec/issues/2336).
- Correction d'une typographie dans le champ `origin_server_ts` pour les événements de vérification en salle [#2337](https://github.com/tchapgouv/matrix-spec/issues/2337).

### Autres changements
- Correction de problèmes liés aux fragments de nouvelles (newsfragments) [#2338](https://github.com/tchapgouv/matrix-spec/issues/2338).
