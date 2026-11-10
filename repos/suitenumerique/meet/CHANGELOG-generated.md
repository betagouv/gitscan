## Changelog : meet (30 derniers jours, au 07/11/2026)

### Résumé
Ce mois-ci, l'accent a été mis sur le renforcement massif de la sécurité et de la traçabilité grâce à l'implémentation d'un nouveau système complet de journaux d'audit. Les évolutions visent également à améliorer la fiabilité des connexions et à offrir une meilleure expérience utilisateur lors de la gestion des enregistrements et de la navigation.

### Évolutions fonctionnelles
- **Enregistrements** : possibilité de choisir l'encodage de l'enregistrement, réception de notifications par email à la fin d'un enregistrement, et autorisation pour tout utilisateur authentifié de lancer un enregistrement.
- **Expérience utilisateur (UX)** : affichage d'erreurs explicites en cas d'échec de connexion ou de réunion, notifications lors de l'interruption d'un enregistrement, et maintien de l'interface d'administration lors du changement de paramètres.
- **Accessibilité** : fermeture des dialogues d'invitation avec la touche Échap et annonce de la coupure du micro via des raccourcis.
- **Confidentialité & Support** : les salles de réunion sont désormais exclues des moteurs de recherche et l'outil de chat Crisp est remplacé par le formulaire de support officiel de La Suite.

### Évolutions techniques
- **Sécurité & Audit** : mise en place d'un système de journalisation d'audit structuré (actions administratives, échanges de tokens, opérations sur les enregistrements) et protection des données sensibles (masquage des secrets dans les logs, Sentry et les erreurs d'application).
- **Fiabilité & Performance** : amélioration de la gestion des reconnexions LiveKit (politique de backoff exponentiel), ajout de timeouts sur les appels API, et optimisation des performances via un pool de connexions PostgreSQL et un index sur les emails.
- **Maintenance & Sécurité** : correction de nombreuses vulnérabilités (CVE) sur les composants critiques (Python, Node, Nginx, etc.) et durcissement de l'accès aux salles (utilisation de endpoints POST pour les tokens).
- **Infrastructure & CI/CD** : optimisation des builds Docker pour l'architecture arm64, mise à jour des outils de scan de vulnérabilités (Trivy) et gestion des suppressions de salles (soft delete) avec purge automatique.

### Autres changements
- Documentation du nouveau système de journalisation d'audit.
