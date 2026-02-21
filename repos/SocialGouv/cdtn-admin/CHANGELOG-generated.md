## Changelog : cdtn-admin (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées à l'outil d'administration du Code du travail numérique au cours du dernier mois. Les changements incluent des corrections de bugs pour améliorer la publication de contenu (conventions collectives, infographies, contributions, export), l'ajout de nouvelles fonctionnalités comme le suivi des NOTA dans les articles Kali, et l'ajout d'icônes pour les thèmes. Des améliorations ont également été apportées aux notifications envoyées sur Mattermost lors des déploiements.

### Évolutions fonctionnelles
- Correction d'un bug empêchant la mise à jour des fichiers SVG ou PDF dans les infographies (#1639).
- Correction d'un problème lors de la publication des conventions collectives (#1638).
- Correction d'un bug lié au type de données lors de la publication d'une contribution.
- Correction d'un bug lors de l'export des suggestions (#7107, #1641).
- Ajout du suivi des NOTA dans les articles Kali (#1642).
- Ajout de nouvelles icônes pour les thèmes (#1635).
- Amélioration des messages de notification envoyés sur Mattermost lors des déploiements.

### Évolutions techniques
- Ajout de notifications Mattermost lors des déploiements en production (#1630).
- Modification de la génération des thèmes pour le nouveau design (#1628).
- Correction d'un problème lié aux migrations et utilisation de `triplet` au lieu de `couple` (#1631).

### Autres changements
- Mise en place des tests des widgets uniquement dans le projet `code-du-travail-numerique` (#1636).
