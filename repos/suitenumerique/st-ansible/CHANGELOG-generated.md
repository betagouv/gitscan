## Changelog : st-ansible (30 derniers jours, au 7 juillet 2026)

### Résumé
Les dernières mises à jour de st-ansible améliorent la configuration et la personnalisation des applications de la Suite Territoriale, notamment pour les services de messagerie (Rspamd), de stockage (Drive), de collaboration (Collabora) et de visioconférence (Meet). Des corrections ont également été apportées pour assurer la stabilité et la sécurité des déploiements.

### Évolutions fonctionnelles
- **Rspamd :** Ajout de scores `add_header` et `rewrite_subject` pour un contrôle plus fin du filtrage anti-spam. Désactivation du greylisting.
- **Drive :** Correction de la configuration Nginx et des valeurs par défaut. Ajout de nouvelles routes Nginx upstream.
- **Collabora :** Possibilité de personnaliser la police d'affichage.
- **Meet :** Ajout d'une configuration Nginx personnalisée. Correction d'un problème d'utilisateur dans le Dockerfile et de la configuration du port non privilégié pour les défis ACME de Caddy.

### Évolutions techniques
- **Meet :** Clarification des procédures de rollback dans la documentation.
- **Rspamd :** Ajout d'une variable `st_messages_mpa_rspamd_reject_score` pour configurer le score de rejet des messages. Désactivation du module `dkim_signing`.
