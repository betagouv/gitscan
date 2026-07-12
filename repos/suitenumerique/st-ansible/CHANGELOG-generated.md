## Changelog : st-ansible (30 derniers jours, au 8 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations et des corrections concernant les applications de la Suite Territoriale, notamment pour les services de messagerie (Rspamd), de stockage (Drive) et de visioconférence (Meet). Des options de configuration supplémentaires sont également disponibles pour Collabora et Rspamd.

### Évolutions fonctionnelles
- **Rspamd :** Ajout de variables pour configurer le nombre de lignes d'historique et le nombre de redirecteurs. Possibilité de désactiver le greylisting et de configurer des en-têtes et la réécriture du sujet en fonction des scores Rspamd.
- **Collabora :** Possibilité de personnaliser la police utilisée.
- **Drive :** Correction de la configuration Nginx et des valeurs par défaut. Ajout de nouvelles routes upstream Nginx.
- **Meet :** Correction d'un problème d'utilisateur dans le Dockerfile et correction du port de démarrage non privilégié pour le challenge ACME de Caddy.

### Évolutions techniques
- **Meet :** Ajout d'une configuration Nginx personnalisée.
- **Meet :** Clarification des procédures de rollback dans la documentation.

### Autres changements
- Documentation mise à jour pour refléter les changements apportés à Meet.
- Correction de divers problèmes de configuration pour Meet et Drive.
