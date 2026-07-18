## Changelog : st-ansible (30 derniers jours, au 8 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations à la configuration de l'application Drive, notamment au niveau des routes Nginx, et des ajustements fins à la configuration de l'antispam RSPAMD. De nouvelles variables de configuration sont également introduites pour personnaliser davantage le comportement de RSPAMD et de l'application Messages.

### Évolutions fonctionnelles
- Amélioration de la configuration de l'application Drive avec des routes Nginx mises à jour et des valeurs par défaut corrigées.
- Ajout de variables pour configurer le nombre de lignes d'historique et le nombre de redirecteurs pour l'application Messages (RSPAMD) : `st_messages_mpa_rspamd_history_nrows` et `st_messages_mpa_rspamd_redirectors`.
- Possibilité de désactiver la signature DKIM dans RSPAMD via la variable `st_messages_mpa_rspamd_reject_score`.
- Ajout de variables pour configurer les scores d'en-tête et de réécriture de sujet dans RSPAMD.
- Désactivation du greylisting dans RSPAMD.

### Évolutions techniques
- Ajustements de la configuration Nginx pour l'application Drive pour une meilleure stabilité et performance.

### Autres changements
- Aucun changement significatif à signaler.
