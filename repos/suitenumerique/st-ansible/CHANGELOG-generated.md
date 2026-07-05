## Changelog : st-ansible (30 derniers jours, au 03 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations et des corrections concernant les applications Drive, Meet, Collabora et RSPAMD. Les changements incluent des configurations Nginx personnalisées, la résolution de problèmes d'utilisateurs Docker et l'ajout de variables pour un contrôle plus fin des paramètres.

### Évolutions fonctionnelles
- **Drive:** Correction de la configuration Nginx et des valeurs par défaut. Ajout de nouvelles routes Nginx upstream.
- **Meet:** Ajout d'une configuration Nginx personnalisée pour Meet. Correction d'un problème d'utilisateur dans le Dockerfile et résolution d'un problème lié au port non privilégié pour le challenge ACME de Caddy.
- **Collabora:** Possibilité de personnaliser la police d'écriture.
- **RSPAMD:** Ajout de la variable `st_messages_mpa_rspamd_reject_score` et désactivation du module `dkim_signing`.

### Évolutions techniques
- Amélioration de la documentation concernant les retours en arrière (rollbacks) pour Meet.

### Autres changements
- Aucun changement significatif à signaler.
