## Changelog : cdtn-admin (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à l'outil d'administration du Code du travail numérique au cours des 30 derniers jours. Les mises à jour incluent de nouvelles fonctionnalités pour le suivi des NOTA dans les articles, l'ajout d'icônes pour les thèmes, ainsi que des corrections de bugs concernant la publication de conventions collectives, la mise à jour d'infographies et la gestion des contributions. Une migration vers l'outil de gestion de paquets pnpm a également été effectuée.

### Évolutions fonctionnelles
- Ajout du suivi des NOTA dans les articles Kali, permettant une meilleure gestion de l'information. ([#1642](https://github.com/SocialGouv/cdtn-admin/issues/1642))
- Ajout de nouvelles icônes pour la personnalisation des thèmes. ([#1635](https://github.com/SocialGouv/cdtn-admin/issues/1635))
- Correction d'un bug empêchant la publication des conventions collectives. ([#1638](https://github.com/SocialGouv/cdtn-admin/issues/1638))
- Correction d'un problème empêchant la mise à jour des fichiers SVG ou PDF dans les infographies. ([#1639](https://github.com/SocialGouv/cdtn-admin/issues/1639))
- Correction d'un problème lié au type de données lors de la publication d'une contribution.

### Évolutions techniques
- Migration de Yarn vers pnpm pour la gestion des dépendances, améliorant potentiellement la performance et la sécurité. ([#1644](https://github.com/SocialGouv/cdtn-admin/issues/1644))
- Amélioration des tests pour les widgets, en limitant leur exécution au projet `code-du-travail-numerique`. ([#1636](https://github.com/SocialGouv/cdtn-admin/issues/1636))

### Autres changements
- Correction d'un bug concernant les messages de notification de déploiement sur Mattermost.
- Publication de nouvelles versions : 2.68.1, 2.68.0, 2.67.3, 2.67.2, 2.67.1, 2.67.0, 2.66.6, 2.66.5, 2.66.4.
