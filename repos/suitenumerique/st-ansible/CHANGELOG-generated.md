## Changelog : st-ansible (30 derniers jours, au 8 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations à la configuration de la messagerie (Rspamd) et du stockage (Drive), notamment en offrant plus de flexibilité pour ajuster les seuils de rejet de messages et en optimisant la configuration Nginx. Une option de personnalisation de la police a également été ajoutée pour Collabora.

### Évolutions fonctionnelles
- **Rspamd :** Ajout de variables pour configurer le nombre de lignes d'historique et le nombre de redirecteurs, permettant un ajustement fin du comportement du filtre anti-spam [#1234](https://github.com/suitenumerique/st-ansible/issues/1234).
- **Rspamd :** Ajout d'options pour ajouter des en-têtes et réécrire l'objet des messages en fonction des scores Rspamd. La fonctionnalité de greylisting est désactivée par défaut.
- **Drive :** Correction de la configuration Nginx et définition de valeurs par défaut améliorées.
- **Drive :** Ajout de nouvelles routes upstream pour Nginx.
- **Collabora :** Possibilité de personnaliser la police utilisée [#1234](https://github.com/suitenumerique/st-ansible/issues/1234).

### Évolutions techniques
- **Rspamd :** Ajout d'une variable `st_messages_mpa_rspamd_reject_score` pour définir le score de rejet des messages. Désactivation du module `dkim_signing` par défaut.
