## Changelog : st-ansible (30 derniers jours, au 8 juillet 2026)

### Résumé
Les dernières mises à jour de st-ansible se concentrent sur l'amélioration de la configuration et des options de personnalisation des applications de La Suite Territoriale, notamment pour les services de messagerie (Rspamd), de stockage (Drive) et de visioconférence (Meet). Des corrections ont également été apportées pour résoudre des problèmes de configuration et d'exécution.

### Évolutions fonctionnelles
- **Rspamd :** Ajout de variables pour configurer le nombre de lignes d'historique et le nombre de redirecteurs, permettant un ajustement plus fin du comportement du filtre anti-spam.  Possibilité de désactiver le greylisting et d'ajouter des en-têtes et de modifier le sujet en fonction des scores Rspamd.
- **Drive :** Correction de la configuration Nginx et des valeurs par défaut pour améliorer la stabilité et la performance du service de stockage. Ajout de nouvelles routes upstream Nginx.
- **Meet :** Possibilité de personnaliser la police utilisée par le service de visioconférence.
- **Meet :** Correction d'un problème d'utilisateur dans le Dockerfile et d'un problème lié au port non privilégié pour le challenge ACME de Caddy.

### Évolutions techniques
- **Meet :** Ajout d'une configuration Nginx personnalisée pour Meet.
- **Meet :** Clarification de la documentation concernant les rollbacks.

### Autres changements
- Documentation mise à jour pour refléter les modifications apportées à la configuration de Meet.
